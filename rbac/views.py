from django.shortcuts import render, HttpResponse, redirect
from django.forms import Form, fields, widgets
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from rbac import models
from rbac.server.begin import begin


class Login(Form):
    username = fields.CharField(
        required=True,
        widget=widgets.TextInput(attrs={"placeholder": "用户名"}),
        error_messages={"required": "用户名不能为空！"}
    )
    password = fields.CharField(
        required=True,
        min_length=3,
        max_length=6,
        error_messages={"required": "密码不能为空！",
                        "min_length": "最小为3位！",
                        "max_length": "最大为6位！"},
        validators=[RegexValidator("\d+", "只能是数字！！")],
        widget=widgets.PasswordInput(attrs={"placeholder": "密码"})
    )

    def clean_username(self):
        user = self.cleaned_data.get("username")
        is_exit = models.User.objects.filter(username=user)
        if not is_exit:
            raise ValidationError("用户名不存在！！")
        return user


def login(request):
    if request.method == "GET":
        form = Login()
        return render(request, "login.html", {"form": form})
    else:
        form = Login(request.POST)
        if not form.is_valid():
            return render(request, "login.html", {"form": form})
        user = models.User.objects.filter(**form.cleaned_data).first()

        if not user:
            form.add_error("password", ValidationError("用户名密码不匹配！！"))
            return render(request, "login.html", {"form": form})
        #初始化数据 设置session
        begin(user, request)
        return redirect("/index/")
