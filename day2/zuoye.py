# 8.求1-100的所有数的和
# count = 0
# for i in range(1,101):
#     count += i
# print(count)

# 9.输出 1-100 内的所有奇数

# for i in range(1,101):
#     if i % 2 == 1:
#         print(i)

# 13. ⽤户输⼊⼀个数. 判断这个数是否是⼀个质数
# import math
# def isprime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(math.sqrt(num))+1):   #也可以用num**0.5
#         if num % i == 0:
#             return False
#
#     return True
# for i in  range(1,100):
#     if isprime(i) == True:
#         print(i)


# 14. 输⼊⼀个数. 判断这个数是⼏位数
# num = int(input("输入一个数："))
# count = 1
# while num != 0:
#     num = num//10
#     if num > 0:
#         count += 1
# print(count)
#
# # 999//10
# # Out[1]: 99
# # count =2
# #
# # 99//10
# # Out[3]: 9
# # count =3
# # 9//10
# # Out[4]: 0

