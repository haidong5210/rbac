import re
menu_list = [
    {'id': 1, 'menue_id': 1, 'menu_gp_id': None, 'menu_title': '菜单一', 'title': '用户列表', 'url': '/userinfo/'},
    {'id': 2, 'menue_id':1, 'menu_gp_id': 1, 'menu_title': '菜单一', 'title': '添加用户', 'url': '/userinfo/add/'},
    {'id': 3, 'menue_id': 1, 'menu_gp_id': 1, 'menu_title': '菜单一', 'title': '删除用户', 'url': '/userinfo/del/(\\d+)/'},
    {'id': 4, 'menue_id': 1, 'menu_gp_id': 1, 'menu_title': '菜单一', 'title': '修改用户', 'url': '/userinfo/edit/(\\d+)/'},
    {'id': 5, 'menue_id': 2, 'menu_gp_id': None, 'menu_title': '菜单二', 'title': '订单列表', 'url': '/order/'},
    {'id': 6, 'menue_id': 2, 'menu_gp_id': 5, 'menu_title': '菜单二', 'title': '添加订单', 'url': '/order/add/'},
    {'id': 7, 'menue_id': 2, 'menu_gp_id': 5, 'menu_title': '菜单二', 'title': '删除订单', 'url': '/order/del/(\\d+)/'},
    {'id': 8, 'menue_id': 2, 'menu_gp_id': 5, 'menu_title': '菜单二', 'title': '修改订单', 'url': '/order/edit/(\\d+)/'}]

current_url = "/userinfo/"
"""
目标：
{
 {'id': 1, 'title': '用户列表', 'url': '/userinfo/', 'menu_gp_id': None, 'menu_id': 1, 'menu_title': '菜单管理',"active':True},
 {'id': 5, 'title': '订单列表', 'url': '/order/', 'menu_gp_id': None, 'menu_id': 2, 'menu_title': '菜单2'},
}
"""


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

print(menu_dict)
