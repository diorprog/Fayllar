#

# f=open('D:\Python\Modul_2\main\input.txt','r')
# m=open('D:\Python\Modul_2\main\output.txt','a')
# n=int(f.read())

# for i in range(2,n+1):
#     s=0
#     for j in range(1,i+1):
#         if i%j==0:
#             s+=1
#     if s==2:
#         st=str(i)
#         m.write(f'{st} ')

#
# f=open('D:\Python\Modul_2\main\input.txt','r')
# n=int(f.read())
# f=open('D:\Python\Modul_2\main\output.txt','w')

# i1=1
# i2=1
# arr=[i1,i2]
# for i in range(n-2):
#     i3=i1+i2
#     i1=i2
#     i2=i3
#     arr.append(i3)

# for i in arr:
#     f.write(f'{str(i)} ')

# n inputdan olib fibonachi sonlarni outputga chiqaradi

# f=open('D:\Python\Modul_2\main\input.txt')
# n=int(f.read())
# f.close()
# f=open('D:\Python\Modul_2\main\output.txt','w')

# a1=a2=1
# while a1<=n:
#     a3=a1+a2
#     f.write(f'{a1} ')
#     a1,a2=a2,a3
# f.close

#             # chiqarilgan outputdagi qiymatni dictga yuklab printda chiqaradi

# f=open('D:\Python\Modul_2\main\output.txt','r')
# arr=list(map(int,f.read().split()))
# f.close()

# arr2=[]

# for i,j in enumerate(arr):
#     arr2.append(
#         {
#             'index':  i+1,
#             'valuse': j
#         }
#     )

# print(arr2)


#
#
# class Folloer:
#     def __init__(self):
#         pass
#
# f=open('D:\Python\Modul_2\main\input.txt', 'r')
# arr=f.read().split('\n')
# f.close()
# f=open('output.txt','w')
#
# n=len(arr)
# arr2=[]
# c=0
# for i in arr:
#     c+=1
#     print(f'{c}-odam: ')
#     arr2.append(list(tuple(i.split(',')))[len(i.split())])
#
# maxx=0
#
# for i in range(len(arr2)):
#     if arr2[maxx]<arr2[i]:
#         maxx=0
#
# print(arr[i])


#


# import re
#
# with open('/media/dior_prog/New Volume/Python/Modul_2/main/input.txt') as f:
#     txt = f.read().split('\n')
#
# for i in txt:
#     pattern = '[+]998(90|91|88|93|94|77)[0-9]{7}'
#     match = re.fullmatch(pattern, i)
#
#     if match:
#         print(match.group())
#     else:
#         print('not found')


#


# import  re
#
# with open('/media/dior_prog/New Volume/Python/Modul_2/main/input.txt') as f:
#     txt = f.read().split('\n')
#
# print(txt)
# for i in txt:
#     pattern = '^[A-Z][a-z]+(va|v) ([A-Z][a-z]+)'
#     match = re.fullmatch(pattern, i)
#
#     if match:
#         print(match.group())
#     else:
#         print('Xatosi bor')


#

# 1-usul

# import re
#
#
# def solution(a, s):
#     result = re.fullmatch(a, s)
#
#     if result:
#         return True
#     else:
#         return False
#
#
# s = input('s=')
# pattern = input('a=')
#
# print(solution(pattern, s))


# 2-usul

# import re
#
# print(True if re.fullmatch(input('Pattern: '),input('Text: ')))


#


import re


def solution(s):
     arr=[]
     for i in range(len(s)):
         arr.append(s[i])
     for i in range(len(s)):

s=input('s=')