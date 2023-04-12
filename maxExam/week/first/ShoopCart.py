# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/9 07:48
# 文件名称: ShoopCart.py


def getGoodsInfo(goodsPath):
    """
    获取商品信息
    :return:
    """
    goods = []
    with open(goodsPath, encoding="utf-8") as f:
        for i in f:
            k, v = i.strip().split("|")
            goods.append({"name":k, "price":v})
        f.close()
    return goods

def queryGoodsInfo(goods: list):
    """
    商品信息列表
    :param goods:商品信息
    :return:
    """
    for i in enumerate(goods, 1):
        id, good = i
        print(f"{id} {good['name']} {good['price']}")

def addGoodsToShopCart(goods: list):
    """
    :param goods: 商品信息
    :return: shopCart
    """
    shopCart = [] # 购物车信息
    while True:
        id = input("请选择要添加到购物车中的商品id(按q退出程序，按n进入结算页面): ")
        if id.isdigit() and int(id) <= len(goods) and int(id) >= 1:
            id = int(id) - 1  # 商品编号
            name = goods[id]["name"]
            price = goods[id]["price"]
            number = 1
            for i in range(len(shopCart)):
                good = shopCart[i]
                if good['name'] == goods[id]['name']:
                    shopCart[i]["number"] += 1
                    print(f"购物车中的商品: {name},数量更新为: {shopCart[i]['number']}")
                    break
            else:
                shopCart.append({"name": name, "price": price, "number": number})
                print(f"商品名称: {name}，价格: {price}, 数量: {number}，已添加到购物车")
        elif id.upper() == "N":
            print("欢迎进入购物车结算页面".center(100, "*"))
            return shopCart
        elif id.upper() == "Q":
            print("退出程序!")
            return
        else:
            print("参数非法，请重新输入!")

def showShopCartInfo(shopCart: list):
    """
    遍历购物车信息
    :param shopCart: 购物车中商品
    :param balance 账户余额
    :return: countMoney 购物车中的商品总额
    """
    countMoney = 0.0
    for goods in enumerate(shopCart, 1):
        id, good = goods
        countMoney += float(good['price']) * good['number']
        print(f"{id} {good['name']} {good['price']} {good['number']}")

    return countMoney

def savaMoney():
    """
    存款
    :return:
    """
    while True:
        money = input("请输入存款金额: ")
        if money.replace(".", "").isdigit():
            if float(money) > 0:
                money = float(money)
                break
        else:
            print("参数非法,存款金额应大于0")
    return money

def deleteGoodsInShopCart(shopCart: list, accBalance: float, countMoney: float):
    """
    账户余额小于商品总额时，删除购物车中的商品，直到账户余额大于等于商品总额，并返回更新后的购物车中的商品
    :param shopcart: 购物车
    :param accBalance: 客户账户余额
    :param countMoney: 购物车中的商品总额
    :return:
    """
    while accBalance - countMoney < 0:
        id = input(f"账户余额不足，当前账户余额: {accBalance}, 购物车中商品总额: {countMoney},请选择要删除的商品信息:")
        if id.isdigit() and int(id) >= 1 and int(id) <= len(shopCart):
            id = int(id) - 1 # 商品id在购物车中的索引位置
            shopCart[id]['number'] -= 1
            name = shopCart[id]['name']
            if shopCart[id]['number'] < 1: # 购物车中商品数量小于1，删除改商品
                shopCart.pop(id)
                print(f"商品:{name}，已从购物车中删除!")
            countMoney = showShopCartInfo(shopCart=shopCart) # 计算当前购物总额
        else:
            print("参数错误，请重新输入!")

    return shopCart, countMoney

def saveShoppingInfo(shopCart:list, checkInfo: str):
    """
    保存购物信息至本地文件
    :param shopCart:
    :param checkInfo:
    :return:
    """
    with open("checkShoppingInfo", mode="a", encoding="utf-8") as f:
        for goods in enumerate(shopCart, 1):
            id, good = goods
            f.write(f"{id}, {good['name']} {good['price']} {good['number']}\n")
        f.write(checkInfo)
        f.write("\n")
        f.write("\n")
        f.flush()
        f.close()

    print("请收好购物小票～～～")



def main():
    goodsPath = "goods" # 商品信息文件
    accBalance = savaMoney()  # 存款
    goods = getGoodsInfo(goodsPath=goodsPath)
    queryGoodsInfo(goods=goods)
    shopCart = addGoodsToShopCart(goods=goods) # 添加商品到购物车
    if shopCart == None: # 用户在购物车页面退出程序
        return
    countMoney = showShopCartInfo(shopCart=shopCart) # 展示购物车中信息，并计算购物车总金额
    if countMoney > accBalance:
        shopCart, countMoney = deleteGoodsInShopCart(shopCart=shopCart, accBalance=accBalance, countMoney=countMoney)

    checkInfo = f"您本次共消费:{countMoney}元, 账户余额为:{accBalance - countMoney}元!"
    print(checkInfo)
    saveShoppingInfo(shopCart=shopCart, checkInfo=checkInfo)


if __name__ == '__main__':
    main()