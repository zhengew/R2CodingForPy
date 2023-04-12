
menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}


def show_menu(menu: dict):
    """
    三级菜单
    :param menu:
    :return:
    """
    while True:
        for city in menu:
            print(city)
        key = input('>>>')
        if menu.get(key):
            dic = menu[key]
            flag = show_menu(dic)
            if not flag:
                return False
        elif key.upper() == 'Q':
            return False
        elif key.upper() == 'B':
            return True

show_menu(menu)

# menu_func(menu)
# print('wahaha')

