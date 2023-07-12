# iterator  -> a = [1,2,3,4,5] , "dsfgdgdf"
# generator ->
# def test_generator():
#     yield 1
#     yield 2
#     yield 3
#
# print(list(test_generator()))

# Decorator

# def decorator(func):
#     def wrapper(*args):
#         if args[0] >= 10 and args[1] >= 10:
#             return func(*args)
#         else:
#             return "Bad arguments"
#     return wrapper
#
#
# @decorator
# def add_num(num1 , num2):
#     return num1 + num2
#
# print(add_num(10, 14))


#


# def my_decorator(n1): 
#     def inner(func): 
#         def wrapper(n2): 
#             return func(n2)  * n1  
#         return wrapper
#     return inner

# @my_decorator(3) 
# def multiple_num(num): 
#     return num 

# print(multiple_num(10))


#
#
#
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print('Enter dekorator')
#         response = func(*args, **kwargs)
#         print('Exit decorator1')
#         return response
#
#     return wrapper()
#
#
# def decorator2(func):
#     def wrapper(*args, **kwargs):
#         print('enter decorate2')
#         response = func(*args, **kwargs)
#         print('exit decorator2')
#         return response
#
#     return wrapper()
#
#
# @decorator2
# @decorator
# def test(n: int):
#     print('Enter test funktion')
#     return n
#
# print(test(18))


#


#
# def summ(nums):
#     arr = []
#     s = 0
#     for i in nums:
#         s += i
#         arr.append(s)
#     return arr
#
# nums = [1, 2, 3, 4, 5]
# result = summ(nums)
# print(result)


#

#
# sentences = ["alice and bob love leetcode",
#              "i think so too",
#              "this is great thanks very much"]
# max_=float('-inf')
#
# print(max([len(i.split()) for i in sentences]))
# print(max(map(lambda x: len(x.split()), sentences)))
# print(len(sorted(sentences,key=lambda x: len(x.split()))[-1].split()))


# grid = [
#     [1, 2, 4, 8],
#     [1, 3, 3, 9]
# ]
#
# a = list(zip(*grid))
#
# print(*a)


#


#
# def maximumValue(strs):
#     max_value = 0
#
#     for string in strs:
#         if string.isdigit():
#             max_value = max(max_value, int(string))
#         else:
#             max_value = max(max_value, len(string))
#
#     return max_value
#
#
# s=['0000','alic3','bob','3','4']
# print(maximumValue(s))



#



# import os

# while True:
#     current_dir = os.getcwd()
#     command = input(current_dir + "$ ").split()
#     match command[0]:
#         case "cd":
#             os.chdir(command[1])

#



#

import os

c=0
for i in os.listdir():
    if os.path.isfile():
        c+=1
print(c)