# 2、name = input(“>>>”)
# name变量量是什什么数据类型？
# string

# name = input(">>>>>>>")
# print(type(name))

# 4.⽤print打印出下⾯内容：
# ⽂能提笔安天下,
# 武能上⻢定乾坤.
# ⼼存谋略何⼈胜,
# 古今英雄唯是君.

# print("""
# 文能提笔安天下,
# 武能上马定乾坤.
# 心存谋略略何人胜,
# 古今英雄唯是君.
# """)

# 5.利⽤if语句写出猜⼤⼩的游戏：
# 设定⼀个理想数字⽐如：66，让⽤户输⼊数字，如果⽐66⼤，则显示猜测的结果⼤了；如果⽐66⼩，则显示猜测的结果⼩了;只有等于66，
# 显示猜测结果正确。

# import re
# while True:
#     num = input("请输入一个数字,按Q退出:")
#     if not re.match("[qQ0-9]", num):
#         print("输入错误")
#     elif num.upper() == "Q" :
#         break
#     elif int(num) >66:
#         print("猜大了")
#     elif int(num) < 66:
#         print("猜小了")
#     else:
#         print("猜对了")
#         break

