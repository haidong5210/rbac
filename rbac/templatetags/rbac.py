#生成菜单
import re
from django.conf import settings
from django.template import Library

register = Library()


@register.inclusion_tag("server.html")    #下面的函数返回什么都传给这个html用！
def menu(request):
    current_url = request.path_info
    menu_list = request.session.get(settings.MENU_PERMISSION)
    #放到一个字典里：
    """
    {
    1: {'id': 1, 'menue_id': 1, 'menu_gp_id': None, 'menu_title': '菜单一', 'title': '用户列表', 'url': '/userinfo/', 'active': True},
     5: {'id': 5, 'menue_id': 2, 'menu_gp_id': None, 'menu_title': '菜单二', 'title': '订单列表', 'url': '/order/'}
     }

    """
    #先把两个是菜单的放到一个字典里
    menu_dict = {}
    for item in menu_list:
        if not item['menu_gp_id']:
            menu_dict[item['id']] = item

    for item in menu_list:
        regex = "^{0}$".format(item['url'])
        if re.match(regex, current_url):
            menu_gp_id = item['menu_gp_id']
            if menu_gp_id:
                menu_dict[menu_gp_id]['active'] = True
            else:
                menu_dict[item['id']]['active'] = True
    result={}
    for item in menu_dict.values():
        active=item.get("active")
        if item["menue_id"] in result:
            result[item["menue_id"]]["children"].append({"title":item["title"],"url":item["url"],"active":active})
            if active:
                result[item["menue_id"]]["active"]=True
        else:
            result[item["menue_id"]]={
                "menu_id":item["menue_id"],
                "menu_title":item["menu_title"],
                "active":active,
                "children":[
                    {"title":item["title"],"url":item["url"],"active":active}
                ]
            }
    return {"menu_dict":result}