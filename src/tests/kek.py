import random
import string

el = "213690 stars"
# x = [66,22,33]
# print(x[1])
print(int(el.split()[0]) >= 20000)
# # print(int(el.split()[0]))
# #
# # a =[20,30,50,50]
# # b = [50,30,20]
# # print(set(a)==set(b))
# # print(set(a))
# print(set(el))
b = (1, 2)
# def summ(a, b):
#     return a+b
# summ(2,3)
# print(summ(2,3))
# print(summ(*b))


print("".join(random.choice(string.ascii_lowercase + string.digits) for _ in range(5)))


el = [1, 3, 4, 3]
print(set(el))
el1 = [3, 1, 4]
print(set(el) == set(el1))
