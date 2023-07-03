# 2

# f=open('D:\Python\Modul_2\Vazifa_1\input.txt')
# n=int(f.read())
# f.close()
# f=open('D:\Python\Modul_2\Vazifa_1\output.txt','w')

# for i in range(1,n+1):
#     if i%2==0:
#         f.write(f'{i} ')

# 3

# f=open('D:\Python\Modul_2\Vazifa_1\input.txt')
# a,d=f.read().split()
# a=int(a)
# d=int(d)
# f.close()
# f=open('D:\Python\Modul_2\Vazifa_1\output.txt','w')
# summ=a
# for i in range(9):
#     f.write(f'{summ} ')
#     summ+=d

# 6

# f=open('D:\Python\Modul_2\Vazifa_1\input.txt')
# k=3
# arr=list(map(int,f.read().split()))
# f.close()
# f=open('D:\Python\Modul_2\Vazifa_1\output.txt','w')

# for i in range(len(arr)):
#     if k==i:
#         m=arr[k]
#         break
#     else:
#         m=-1

# f.write(f'{m}')

# 7

# f=open('D:\Python\Modul_2\Vazifa_1\input.txt')
# arr=list(map(int,f.read().split()))
# f.close()
# f=open('D:\Python\Modul_2\Vazifa_1\output.txt','w')

# for i in range(len(arr)):
#     f.write(f'{i+1}-elementi: {arr[i]} ')

# 8

# f=open('D:\Python\Modul_2\Vazifa_1\input.txt')
# arr=list(map(int,f.read().split()))
# f.close()
# f=open('D:\Python\Modul_2\Vazifa_1\output.txt','w')

# f.write(f'{arr[0]}  {arr[len(arr)-1]} ')

# 9

# f=open('D:\Python\Modul_2\Vazifa_1\input.txt')
# arr=list(map(int,f.read().split()))
# f.close()
# f=open('D:\Python\Modul_2\Vazifa_1\output.txt','w')
# arr2=[arr[len(arr)-1],arr[0]]

# f.write(f'{arr2} ')

# 10

# f=open('D:\Python\Modul_2\Vazifa_1\input.txt')
# arr=list(map(int,f.read().split()))
# f.close()
# f=open('D:\Python\Modul_2\Vazifa_1\output.txt','w')
# arr2=arr[::-1]

# f.write(f'{arr2} ')

# 11

# f=open('D:\Python\Modul_2\Vazifa_1\input.txt')
# arr=list(map(int,f.read().split()))
# f.close()

# f=open('D:\Python\Modul_2\Vazifa_1\output.txt','w')
# m=open('D:\Python\Modul_2\Vazifa_1\output2.txt','w')

# for i in range(len(arr)):
#     if i%2==0:
#         f.write(f'{arr[i]} ')
#     else:
#         m.write(f'{arr[i]} ')

# 12

# f=open('D:\Python\Modul_2\Vazifa_1\input.txt')
# arr=list(map(int,f.read().split()))
# f.close()

# f=open('D:\Python\Modul_2\Vazifa_1\output.txt','w')
# m=open('D:\Python\Modul_2\Vazifa_1\output2.txt','w')

# for i in range(len(arr)):
#     if i%2==0:
#         m.write(f'{arr[i]} ')
#     else:
#         f.write(f'{arr[i]} ')

# 13

# f=open('D:\Python\Modul_2\Vazifa_1\input.txt')
# arr=list(map(int,f.read().split()))
# f.close()

# f=open('D:\Python\Modul_2\Vazifa_1\output.txt','w')
# m=open('D:\Python\Modul_2\Vazifa_1\output2.txt','w')

# for i in arr:
#     if i>0:
#         f.write(f'{i} ')
#     else:
#         m.write(f'{i} ')

# 14

# f=open('D:\Python\Modul_2\Vazifa_1\input.txt')
# arr=list(map(float,f.read().split()))
# f.close()
# f=open('D:\Python\Modul_2\Vazifa_1\output.txt','w')

# summ=0
# for i in arr:
#     summ+=i
# n=len(arr)

# o=summ/n

# f.write(f'{o} ')

# 15

# f=open('D:\Python\Modul_2\Vazifa_1\input.txt')
# arr=list(map(float,f.read().split()))
# f.close()
# f=open('D:\Python\Modul_2\Vazifa_1\output.txt','w')
# n=0
# summ=0
# for i in range(len(arr)):
#     if i%2==1:
#         summ+=arr[i]
#         n+=1

# o=summ/n

# f.write(f'{o} ')

# 18

# f=open('D:\Python\Modul_2\Vazifa_1\input.txt')
# arr=list(map(int,f.read().split()))
# f.close()
# f=open('D:\Python\Modul_2\Vazifa_1\output.txt','w')
# n=0
# summ=0
# for i in range(1,len(arr)-1):
#     if arr[i-1]>arr[i] and arr[i]<arr[i+1]:
#         f.write(f'{arr[i]} ')

# 19

# f=open('D:\Python\Modul_2\Vazifa_1\input.txt')
# arr=list(map(int,f.read().split()))
# f.close()
# f=open('D:\Python\Modul_2\Vazifa_1\output.txt','w')
# n=0
# summ=0
# arr=arr[::-1]
# for i in range(1,len(arr)-1):
#     if arr[i-1]<arr[i] and arr[i]>arr[i+1]:
#         m=arr[i]
#         break

# f.write(f'{m} ')

# 20

# f=open('D:\Python\Modul_2\Vazifa_1\input.txt')
# arr=list(map(int,f.read().split()))
# f.close()
# f=open('D:\Python\Modul_2\Vazifa_1\output.txt','w')
# n=0
# summ=0
# for i in range(1,len(arr)-1):
#     if arr[i-1]>arr[i] and arr[i]<arr[i+1] or arr[i-1]<arr[i] and arr[i]>arr[i+1]:
#         f.write(f'{arr[i]} ')

# 21

# f=open('D:\Python\Modul_2\Vazifa_1\input.txt')
# arr=list(map(int,f.read().split()))
# f.close()
# f=open('D:\Python\Modul_2\Vazifa_1\output.txt','w')
# n=0
# summ=0
# for i in range(1,len(arr)-1):
#     if arr[i-1]<arr[i] and arr[i]>arr[i+1]:
#         f.write(f'{i+1} ')

# 22

# f=open('D:\Python\Modul_2\Vazifa_1\input.txt')
# arr=list(map(int,f.read().split()))
# f.close()
# f=open('D:\Python\Modul_2\Vazifa_1\output.txt','w')
# arr2=[]
# n=0
# summ=0
# for i in range(1,len(arr)-1):
#     if arr[i-1]>arr[i] and arr[i]<arr[i+1] or arr[i-1]<arr[i] and arr[i]>arr[i+1]:
#         arr2.append(i+1)
# arr2.sort()
# arr2[::-1]        
# f.write(f'{arr2} ')

# 25

# f=open('D:\Python\Modul_2\Vazifa_1\input.txt')
# arr=list(map(int,f.read().split()))
# f.close()
# f=open('D:\Python\Modul_2\Vazifa_1\output.txt','w')
# arr2=[]

# for i in arr:
#     arr2.append(pow(i,2))

# f.write(f'{arr2}')

# 26

# f=open('D:\Python\Modul_2\Vazifa_1\input.txt')
# arr=list(map(int,f.read().split()))
# f.close()
# f=open('D:\Python\Modul_2\Vazifa_1\output.txt','w')

# maxx=minn=0
# for i in range(len(arr)):
#     if arr[maxx]<arr[i]:
#         maxx=i
#     if arr[minn]>arr[i]:
#         minn=i
# arr[minn],arr[maxx]=arr[maxx],arr[minn]

# f.write(f'{arr}')

# 27

# f=open('D:\Python\Modul_2\Vazifa_1\input.txt')
# arr=list(map(int,f.read().split()))
# f.close()
# f=open('D:\Python\Modul_2\Vazifa_1\output.txt','w')

# for i in range(int(len(arr)/2)):
#     arr[i],arr[len(arr)-i-1]=arr[len(arr)-i-1],arr[i]

# f.write(f'{arr}')

# 28

# f=open('D:\Python\Modul_2\Vazifa_1\input.txt')
# arr=list(map(float,f.read().split()))
# f.close()
# f=open('D:\Python\Modul_2\Vazifa_1\output.txt','w')

# for i in range(1,len(arr)-1):
#     o=(arr[i-1]+arr[i]+arr[i+1])/3
#     f.write(f'{o} ')

# 29

# f=open('D:\Python\Modul_2\Vazifa_1\input.txt')
# arr=list(map(int,f.read().split()))
# f.close()
# f=open('D:\Python\Modul_2\Vazifa_1\output.txt','w')
# if len(arr)>5:
#     for i in range(5,len(arr)):
#         arr.pop(5)
# f.write(f'{arr}')

# 30

# f=open('D:\Python\Modul_2\Vazifa_1\input.txt')
# arr=list(map(int,f.read().split()))
# f.close()
# f=open('D:\Python\Modul_2\Vazifa_1\output.txt','w')
# m=int(len(arr)/2)
# for i in range(m,len(arr)):
#     arr.pop(m)
# f.write(f'{arr}')


# iyun3

import json
import re


class File:
    def __init__(self, filepath, data):
        self.filepath = filepath
        self.data = data

    def read(self):
        with open(self.filepath, 'r') as f:
            self.data = json.load(f)
        return self.data

    def write(self):
        with open(self.filepath, 'w') as f:
            json.dump(self.data, f, indent=4)


class Cards(File):
    def separate(self):
        arr1 = []
        arr2 = []
        for i in self.data:
            if re.match(r'^8600[0-9]{12}$', i):
                arr1.append(i)
            elif re.match(r'^9860[0-9]{12}$', i):
                arr2.append(i)
            else:
                raise Exception('Incorrect card_number format')
        return arr1, '\n', arr2


filepath = 'separate.json'
while True:
    obj = File("users.json", [])
    data = input('Enter card numbers (space bilann ajrating): ')
    card_numbers = data.split()
    obj.data = card_numbers
    obj.write()

    cards = Cards(filepath, card_numbers)
    arr1, separator, arr2 = cards.separate()
    print("uzcard:", arr1)
    print("humo:", arr2)
