import re
from rbac import models
from django.conf import settings

#初始化函数，模块
def begin(user, request):
    pressions_list = user.roles.values("permissions__id",                           #权限ID
                                        "permissions__title",                       #权限标题
                                        "permissions__group__id",                  #分组ID
                                        "permissions__code",                        #权限组的编码 用来是否显示操作按钮
                                        "permissions__url",                         #权限url
                                        "permissions__menu_gp_id",                 #组内ID
                                        "permissions__group__menue__title",       #菜单标题
                                        "permissions__group__menue_id"           #菜单ID
                                        ).distinct()      #

    # 菜单相关
    menu_list = []
    for item in pressions_list:
        tpl = {
            "id":item["permissions__id"],                              #权限ID
            "menue_id": item["permissions__group__menue_id"],       #菜单ID
            "menu_gp_id":item["permissions__menu_gp_id"],           #组内ID
            "menu_title":item["permissions__group__menue__title"], #菜单标题
            "title": item["permissions__title"],                      #权限标题
            "url": item["permissions__url"],                          #权限的URL
        }
        menu_list.append(tpl)
    request.session[settings.MENU_PERMISSION] = menu_list

    # 权限相关
    pressions_dict = {}
    for item in pressions_list:
        if item['permissions__group__id'] in pressions_dict:
            pressions_dict[item['permissions__group__id']]['code'].append(item['permissions__code'])
            pressions_dict[item['permissions__group__id']]['url'].append(item['permissions__url'])
        else:
            pressions_dict[item['permissions__group__id']] = {
                "code": [item['permissions__code']],
                "url": [item['permissions__url']]
            }
    print(pressions_dict)
    request.session[settings.USER_PERMISSION] = pressions_dict
