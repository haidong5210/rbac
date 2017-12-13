import re
from django.shortcuts import redirect,HttpResponse
from django.conf import settings
class MiddlewareMixin(object):
    def __init__(self, get_response=None):
        self.get_response = get_response
        super(MiddlewareMixin, self).__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response


class Md(MiddlewareMixin):

    def process_request(self,request):
        current_url = request.path_info
        # print(current_url)
        #设置白名单：
        url = settings.WURL
        for i in url:
            if re.match(i,current_url):
                return None
        permission_dict = request.session.get(settings.USER_PERMISSION)
        # print(user_url)
        if not permission_dict:
            return redirect("/login/")
        else:
            flag=False
            for group_id,code_url in permission_dict.items():
                for url in code_url["url"]:
                    regax = "^{0}$".format(url)
                    if re.match(regax,current_url):
                        #给请求信息赋值code，在vies显示是否有那几个按钮
                        request.permission_code=code_url["code"]
                        flag=True
                        break
                if flag:
                    break

            if not flag:
                return HttpResponse("无权访问！！")


