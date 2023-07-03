#

# class Human:
#     def __init__(self,full_name,age,address):
#         self.full_name=full_name
#         self.age=age
#         self.address=address

#     def __str__(self):
#         return f'{self.full_name} | {self.age} | {self.address}'


# class Student(Human):
#     def __init__(self, full_name, age, address, university):
#         super().__init__(full_name, age, address)
#         self.university=university


# class Old_age(Student):
#     def __init__(self, full_name, age, address, university):
#         super().__init__(full_name, age, address, university)


# n=int(input('n='))
# objects=[]

# for i in range(n):
#     print(f'{i+1}-shaxs ')
#     full_name=input('Full name: ')
#     age=int(input('Age: '))
#     address=input('Address: ')
#     university=input('University: ')
#     obj1=Old_age(full_name,age,address,university)
#     objects.append(obj1)

# for element in objects:
#     if element.age>20:
#         print(element)

#

# import random


# class Tuplam_AB:

#     def __init__(self, set1: set):
#         self.set1 = set1

#     def pechat(self):
#         print(self.set1)


# class Tuplam_Amallari(Tuplam_AB):

#     def add_item(self, new_item):
#         self.set1.add(new_item)

#     def pop_item(self, item):
#         self.set1.discard(item)

#     def konyunksiya(self, set2: set):
#         return set2.intersection(self.set1)

#     def dizyunksiya(self, set2: set):
#         return set2.union(self.set1)

#     def minus(self, set2: set):
#         return set2.difference(self.set1)


# set1 = set(map(int, [random.randrange(1, 10) for _ in range(10)]))
# obj = Tuplam_Amallari(set1)
# obj2 = Tuplam_Amallari({1, 2, 3, 15, 18, 12, 0})

# obj.pechat()
# obj2.pechat()

# print(obj.dizyunksiya(obj2.set1))
# print(obj.konyunksiya(obj2.set1))
# print(obj.minus(obj2.set1))
# # obj.pechat()


#

# class Tarif()
#     def __init__(self):

#


# class Bank:

#     def __init__(self, a: list, b: list):
#         self.a=a
#         self.b=b

#     def Foyda(self):
#         arr=[]
#         for i in range(len(self.a)):
#             arr.append(self.a[i]*self.b[i]/100)
#         return sum(arr)

# a=list(map(float,input('Massiv1: ').split()))
# b=list(map(float,input('Massiv2: ').split()))

# res=Bank(a, b)

# print(res.Foyda())


#

# class Human:
#     def __init__(self, n: list, k: int):
#         self.n=n
#         self.k=k

#     def Left(self):
#         arr=[]
#         for i in range(len(self.n)):
#             if len(self.arr) != 1:
#                 if i==self.k:
#                     arr=self.n.pop(i)
#             else:
#                 return arr


# n=list(map(int,input().split()))
# k=int(input('k='))

# res=Human(n, k)

# print(res.Left())


#


# class Circle:
#     def __init__(self, arr: list):
#         self.arr=arr

#     def operation(self, k: int):
#         i = 0
#         while len(self.arr) != 1:
#             self.arr.pop(k-1)
#             self.arr.insert(self.arr[k-1 : ],0)
#             del self.arr[k-1:]
#             if i == len(self.arr)-1:
#                 i == k
#         print(self.arr[0])

#

# class UY_kutubxonasi:
#     def __init__(self,name:str,year_of_publish:int,author:str):
#         self.name=name
#         self.year_of_publish=year_of_publish
#         self.author=author
#     def pechat(self):
#         print(self.name,self.year_of_publish,self.author)


# list=[]
# n=int(input('kitoblar sonini kiriting:'))
# for i in range(n):
#     print(f'{i+1}  - kitob ')
#     name=input('kitob nomi : ')
#     year_of_publish=int(input('chiqarilgan yili : '))
#     author=input('Muallifi : ')
#     tuplam=UY_kutubxonasi(name,year_of_publish,author)
#     list.append(tuplam)
# sear_one=input('enter your choice : ')
# query = True

# for i in list:
#     m1=i.name.find(sear_one)
#     m2=str(i.year_of_publish).find(sear_one)
#     m3=i.author.find(sear_one)
#     if m1!=-1 or m2!=-1 or m3!=-1:
#         i.pechat()
#         query = False
# if query:
#     print('wrong choice')

# search   qidiruv

# class Book:
#     def __init__(self, name: str, year: int, author: str):
#         self.name=name
#         self.year=year
#         self.author=author

#     def printt(self):
#         print(self.name, self.year, self.author)

# arr=[]
# n=int(input('n= '))

# for i in range(n):
#     print(f'{i+1}-book: ')
#     name=input('Name: ')
#     year=int(input('Year: '))
#     author=input('Author: ')

#     books=Book(name, year, author)
#     arr.append(books)

# search=input("Izlanayotgan kitob nomi: ")

# for i in arr:
#     if search.upper() in i.name.upper() or \
#        search in str(i.year) or \
#        search.upper() in i.author.upper():
#         i.printt()


#

# class Insta:
#     def __init__(self, name: str, arr: tuple):
#         self.name=name
#         self.arr=arr
#
#     def prnt(self):
#         print(self.name, self.arr)
#
# tpl=tuple()
# n=int(input('n= '))
#
# for i in range(n):
#     print(f'{i+1}-odam: ')
#     name=input('Ismi: ')
#     tpl=tuple(input('Podpischiklari(1 4 5 3 n): ').split())
#     podp=Insta(name,tpl)
#
# print(podp.prnt())

#

# import random
# print('6 imkoniyat 1-40')
# arr_tanlov = []
# i = 0
# while len(arr_tanlov) < 6:
#     i += 1
#     d = int(input(f'{i}-son'))
#     if d > 40:
#         Exception('son 40dan oshib ketdi...')
#         continue
#     arr_tanlov.append(d)
#
# arr2 = set(arr_tanlov)
# set1 = set(map(int, [random.randrange(1,40) for _ in range(7)]))
#
# print(f'Tanlovlaringiz: {arr_tanlov}')
# print(f'kombinatsiya: {set1}')
#
# n = arr2.intersection(set1)
# if len(n) == 6:
#     print('Jackpot')
# elif len(n) == 5:
#     print('2-kategoriyada g\'olib bo\'ldingiz')
# elif len(n) == 4:
#     print('3-kategoriyada g\'olib bo\'ldingiz')


#

# def num(i: tuple):
#     for j in i:
#         yield j
#
#
# arr = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
# arr2 = []
#
# for i in arr:
#     m = num(i)
#     for k in m:
#         arr2.append(k)
# tpl = tuple(arr2)
# print(tpl)


#


#1-usul

# def count(arr):
#     k = {}
#     for i in arr:
#         if i in k:
#             k[i] += 1
#         else:
#             k[i] = 1
#     return k
#
#
# arr = list(map(int, input('Massiv: ').split()))
# print(count(arr))

#2-usul

# arr = list(map(int, input('Massiv: ').split()))
# for i in set(arr):
#     print(f"{i} son {arr.count(i)} marta")


#


# arr = list(map(int,input('Massiv: ').split()))
# t=int(len(arr)/2)
# arr2 = []
#
# for i in range(t):
#     arr2.append(arr[i])
#
# arr2.sort()
# arr3=[]
#
# for i in range(t,t+t):
#     arr3.append(arr[i])
# arr3.sort()
# arr3.reverse()
# for i in arr3:
#     arr2.append(i)
#
# print(arr2)


#


# import re

# s=input('Gmail: ')

# pattern='\w(@gmail.com)'

# result=re.search(pattern,s)
# print(result)


#



# def num2word(m):
#     s1 = m // 100
#     s2 = (m // 10) % 10
#     s3 = m % 10

#     birlik = {
#         0: '',
#         1: 'bir',
#         2: 'ikki',
#         3: 'uch',
#         4: "to'rt",
#         5: 'besh',
#         6: 'olti',
#         7: 'yetti',
#         8: 'sakkiz',
#         9: "to'qqiz",
#     }
#     onlik = {
#         0: '',
#         1: "o'n",
#         2: "yigirma",
#         3: "o'ttiz",
#         4: "qirq",
#         5: "ellik",
#         6: "oltmish",
#         7: "yetmish",
#         8: "sakson",
#         9: "to'qson",
#     }

#     if s1 != 0:
#         son1 = birlik[s1] + ' yuz'
#     else:
#         son1 = ''
#     son2 = onlik[s2]
#     son3 = birlik[s3]
#     son = son1 + ' ' + son2 + ' ' + son3
#     return son.strip()


# n = int(input("n="))
# print(num2word(n))

# nollar = {
#     '0': 'yuz',
#     '1': 'ming',
#     '2': 'million',
#     '3': 'milliard',
#     '4': 'trillion'
# }


#


def num2word(m):
    s1 = m // 100
    s2 = (m // 10) % 10
    s3 = m % 10

    birlik = {
        0: '',
        1: 'bir',
        2: 'ikki',
        3: 'uch',
        4: "to'rt",
        5: 'besh',
        6: 'olti',
        7: 'yetti',
        8: 'sakkiz',
        9: "to'qqiz",
    }
    onlik = {
        0: '',
        1: "o'n",
        2: "yigirma",
        3: "o'ttiz",
        4: "qirq",
        5: "ellik",
        6: "oltmish",
        7: "yetmish",
        8: "sakson",
        9: "to'qson",
    }

    if s1 != 0:
        son1 = birlik[s1] + ' yuz'
    else:
        son1 = ''
    son2 = onlik[s2]
    son3 = birlik[s3]
    son = son1 + ' ' + son2 + ' ' + son3
    return son.strip()


n = int(input("n="))

nollar = {
    0: 'yuz',
    1: 'ming',
    2: 'million',
    3: 'milliard',
    4: 'trillion'
}
arr=[]

while n>0:
    arr.append(n%1000)
    n//=1000

print(num2word(n))
ss=''
for i in range(1,len(arr)):
    if arr[i]!=0:
        ss=' '+num2word(arr[i])+' '+nollar[i]+ss
ss+=' '+num2word(arr[0])

print(ss)