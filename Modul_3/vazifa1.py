# String-1

# 1

# def hello_name(name):
#   return f'Hello {name}'
#
#
# strr=input('str=')
# print(hello_name(strr))


# 2


# def make_abba(a,b):
#   str=a+b+b+a
#   return str
#
# str1=input('Satr1: ')
# str2=input('Satr2= ')
# print(make_abba(str1,str2))


# 3


# def make_abba(a,b):
#   str='<'+a+'>'+b+'</'+a+'>'
#   return str
#
# str1=input('Satr1: ')
# str2=input('Satr2= ')
# print(make_abba(str1,str2))


# 4


# def make_abba(a,b):
#   if a[0]==a[1] and a[2]==a[3]:
#     return f'{a[0]+a[1]+b+a[2]+a[3]}'
#   else:
#     return 'Xtolik bor'
#
# str1=input('Satr1: ')
# str2=input('Satr2= ')
# print(make_abba(str1,str2))


# 5


# def extra_end(str:str):
#   s=str[::-1]
#   s=s[0]+s[1]
#   s=s[::-1]
#   return s+s+s
#
# str=input('Str: ')
# print(extra_end(str))


# 6


# def first_two(str:str):
#   s=str[0]+str[1]
#   return s+s+s
#
# str=input('Str: ')
# print(first_two(str))


# 7


# def first_half(str:str):
#     s=''
#     for i in range(int(len(str)/2)):
#         s+=str[i]
#     return s
#
# str=input('Str: ')
# print(first_half(str))


# 8


# def without_end(str: str):
#     s=''
#     for i in range(1,len(str)-1):
#         s += str[i]
#     return s
#
# str = input('str=')
# print(without_end(str))


# 9


# def combo_string(a,b):
#     return b+a+b
#
# a=input('s1=')
# b=input('s2=')
#
# print(combo_string(a,b))


# 10


# def non_start(a,b):
#     s1=''
#     s2=''
#     for i in range(1,len(a)):
#         s1+=a[i]
#     for i in range(1,len(b)):
#         s2+=b[i]
#     return s1+s2
# a=input('s1=')
# b=input('s2=')
#
# print(non_start(a,b))


# String-2

# 1


# def doublechar(string:str):
#     s=''
#     for i in range(len(str)):
#         s+=str[i]+str[i]
#     return s
# str=input('s=')
# print(doublechar(str))


# 2


# def doublechar(string:str):
#     count=0
#     for i in range(1,len(str)):
#         if str[i-1]+str[i]=='hi':
#             count+=1
#     return count
# str=input('s=')
# print(doublechar(str))


# 3


# def doublechar(string:str):
#     c=False
#     for i in range(2,len(str)):
#         if str[i-2]+str[i-1]+str[i]=='cat':
#             for j in range(2, len(str)):
#                 if str[j - 2] + str[j - 1] + str[j] == 'dog':
#                    c=True
#     return c
# str=input('s=')
# print(doublechar(str))


# 4

# def countcode(string:str):
#     count=0
#     for i in range(1,len(str)):
#         if str[i-3]+str[i-2]+str[i-1]+str[i]=='code':
#             count+=1
#     return count
# str=input('s=')
# print(countcode(str))


# 5


# a=input('s1=')
# b=input('s2=')
# c=False
# a.upper()
# b.upper()
# if a.find(b):
#     c=True
# print(c)


# 6

# s=input('s1=')
#
# c=True
# if s.find('.xyz'):
#     c=False
# print(c)


# 7


# s=input('s1=')
# b=False
# for i in range(2,len(s)):
#     if s[i]=='b' and s[i-2]=='b':
#         b=True
# print(b)


# 8


# 9

# s1 = input('s1=')
# s2 = input('s2=')
#
# m = max(len(s1), len(s2))
# s = ''
# for i in range(m):
#     if len(s1)==0 or len(s2)==0:
#         break
#     else:
#         s += s1[i] + s2[i]
#
# if len(s1)==0:
#     s+=s2
# elif len(s2)==0:
#     s+=s1
# print(s)


# 10

# s=input('s=')
# n=int(input('n='))
# s=s[::-1]
# str=''
# for i in range(n):
#     str+=s[i]
# str=str[::-1]
# s1=''
# for i in range(n):
#     s1+=str
# print(s1)


# 11


# List-1

# 1


# arr=list(map(int,input('Massiv elementlari: ').split()))
# n=False
# if arr[0]==6 or arr[len(arr)-1]==6:
#     n=True
#
# print(n)


# 2


# arr=list(map(int,input('Massiv elementlari: ').split()))
# n=False
# if arr[0]==arr[len(arr)-1]:
#     n=True
#
# print(n)


# 3

# 4


# arr1=list(map(int,input('1-Massiv elementlari: ').split()))
# arr2=list(map(int,input('2-Massiv elementlari: ').split()))
# n=False
# if arr1[0]==arr2[0] or arr1[len(arr1)-1]==arr2[len(arr2)-1]:
#     n=True
#
# print(n)


# 5


# arr=list(map(int,input('Massiv elementlari: ').split()))
# s=0
# for i in range(len(arr)):
#     s+=arr[i]
# print(s)


# 6


# def rotate_left3(nums:list):
#     arr2=[]
#     arr2.append(nums[1])
#     arr2.append(nums[2])
#     arr2.append(nums[0])
#     return arr2
# arr=list(map(int,input('uzunligi 3 bo\'lgan massiv elementlari: ').split()))
# print(rotate_left3(arr))


# 7


# def reverse3(nums:list):
#     nums[0],nums[2]=nums[2],nums[0]
#     return nums
# arr=list(map(int,input('uzunligi 3 bo\'lgan massiv elementlari: ').split()))
# print(reverse3(arr))


# 8


# def max_end3(nums:list):
#     n=nums[0]
#     for i in nums:
#         if n<=i:
#             m=i
#     nums[0],nums[1],nums[2]=m,m,m
#     return nums
# arr=list(map(int,input('uzunligi 3 bo\'lgan massiv elementlari: ').split()))
# print(max_end3(arr))


# 9


# def sum2(nums:list):
#     return nums[0]+nums[1]
# arr=list(map(int,input('Massiv elementlari: ').split()))
# print(sum2(arr))


# 10


# def middle_way(a,b):
#     arr=[]
#     arr.append(a[1])
#     arr.append(b[1])
#     return arr
#
# arr1=list(map(int,input('uzunligi 3 bo\'lgan 1-Massiv elementlari: ').split()))
# arr2=list(map(int,input('uzunligi 3 bo\'lgan 2-Massiv elementlari: ').split()))
# print(middle_way(arr1,arr2))


# 11


# def make_ends(a):
#     arr=[]
#     arr.append(a[0])
#     arr.append(a[len(a)-1])
#     return arr
#
# arr=list(map(int,input('uzunligi 3 bo\'lgan 1-Massiv elementlari: ').split()))
# print(make_ends(arr))


# 12


# def has23(a):
#     if len(a)==2:
#         n=False
#         for i in a:
#             if i==2 or i==3:
#                 n=True
#         return n
#     else:
#         return 'Uzunlik xato kiritildi...'
#     return arr
#
# arr=list(map(int,input('uzunligi 2 bo\'lgan Massiv elementlari: ').split()))
# print(has23(arr))


# List-2

# 1


# def count_evens(nums:list):
#     s=0
#     for i in nums:
#         if i%2==0:
#             s+=1
#     return s
#
# arr=list(map(int,input('Massiv elementlari: ').split()))
# print(count_evens(arr))


# 2


# def big_diff(nums: list):
#     maxx = minn = nums[0]
#     for i in nums:
#         if maxx <= i:
#             maxx = i
#     for i in nums:
#         if minn >= i:
#             minn = i
#     return maxx - minn
#
#
# arr = list(map(int, input('Massiv elementlari: ').split()))
# print(big_diff(arr))


#3

#4    chalasi bor

# def sum13(nums: list):
#     s=0
#     find=-1
#     for i in range(len(nums)):
#         if i==find:
#             continue
#         if nums[i]==13:
#             find=i+1
#             continue
#
#     return s
#
# arr = list(map(int, input('Massiv elementlari: ').split()))
# print(sum13(arr))


#5 xatoligi bor
#
# def sum67(nums: list):
#     s=0
#     for i in range(len(nums)):
#         if nums[i]==6:
#             i+=1
#
#             if nums[i]!=7
#     return s
#
# arr = list(map(int, input('Massiv elementlari: ').split()))
# print(sum67(arr))


#6


# def has22(nums: list):
#     n=False
#     for i in range(len(nums)):
#         if nums[i]==2 and nums[i+1]==2:
#             n=True
#     return n
#
#
# arr = list(map(int, input('Massiv elementlari: ').split()))
# print(has22(arr))


#

# s = "is2 sentence4 This1 a3"
# # print(' '.join(map(lambda x : x[:-1] ,sorted(s.split() , key=lambda x : int(x[-1])))))
#
# s = s.split()
# re = []
# for i in sorted(s, key=lambda x: x[-1]):
#     re.append(i[:-1])
# print(' '.join(re))

#Leetcode


#1

# n=input('Satr: ')
# arr=n.split()
# m=len(arr[0])
# for i in range(len(arr)):
#     if len(arr[i]>m:
#         m=arr[i]
# print(m)