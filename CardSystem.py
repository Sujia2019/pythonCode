
cardList=[]
choose=''
def update():                            # 第一种情况修改
    dName = input("请输入要修改名片人的名字")
    for i in cardList:
        if i["name"]==dName:
            key=keys()
            val=input("请输入要修改的内容")
            i[key]=val
            print("修改完成")
            CardSystem()
    print("未找到该人")
    CardSystem()

def search():                            # 第二种情况查询
    isAll = input("你需要打印全部吗?y/n")
    if isAll =='y' or 'Y':
        for c in cardList:
            print("姓名:%s \t 电话:%s \t 地址:%s \t QQ号:%s \t 兴趣爱好:%s \t" % (
                c["name"], c["phoneNumber"], c["address"], c["QQ"], c["hobby"]))
    else:
        dName = input("请输入要查找名片人的名字")
        for i in cardList:
            if cardList[i]["name"]==dName:
                print("姓名:%s \t 电话:%s \t 地址:%s \t QQ号:%s \t 兴趣爱好:%s \t" % (
                    i["name"], i["phoneNumber"], i["address"], i["QQ"], i["hobby"]))
        print("未找到该人")
    CardSystem()

def delete():                            # 第三种情况删除
    dName=input("请输入要删除名片人的名字")
    for i in cardList:
        if i["name"]==dName:
            sure=input("确认要删除吗?y/n")
            if sure == 'y' or 'Y':
                cardList.remove(i)
                print("已删除")
                CardSystem()
            else:
                print("删除失败")
                CardSystem()
    print("未找到该人")
    CardSystem()

def keys():
    key = input("请输入要修改的key:\n1->姓名\n2->电话号\n3->地址\n4->QQ\n5->爱好\n")
    switch={
        "1":"name",
        "2":"phoneNumber",
        "3":"address",
        "4":"QQ",
        "5":"hobby",
    }
    return switch.get(key)

def add():                          # 添加
    card = {"name": "", "phoneNumber": "", "address": "", "QQ": "", "hobby": ""}
    card["name"] = input("请输入姓名:")
    card["phoneNumber"] = input("请输入电话:")
    card["address"] = input("请输入地址:")
    card["QQ"] = input("请输入QQ号:")
    card["hobby"] = input("请输入兴趣爱好:")
    save = input("是否确认保存？Y/N")
    if save=='n' or save=='N':
        print("保存失败")
    if save=='y' or save=='Y':
        cardList.append(card)
        print("姓名:%s \t 电话:%s \t 地址:%s \t QQ号:%s \t 兴趣爱好:%s \t"%(card["name"],card["phoneNumber"],card["address"],card["QQ"],card["hobby"]))
    CardSystem()

def ex():
    exit()
def CardSystem():
    choose = input("请输入你的操作>>>>\n添加:a\n删除:d\n更新:u\n查找:s\n退出:e\n")
    switch = {
        'a':add,
        'd':delete,
        'u':update,
        's':search,
        'e':ex
    }
    switch.get(choose,CardSystem)() #默认情况下重新操作


CardSystem()   # 调用入口

