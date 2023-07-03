            #1

# def son(n):
#     s=0
#     summ=0
#     while n>0:
#         m=n%10
#         n=n//10
#         s+=1
#         summ+=m
#     return (f'{s} {summ}')

# n=int(input('Son: '))
# print(son(n))

            #2
            
# str=input('Son: ')

# s=str[0]
# str=str.replace(s,'',1)

# str=str+s
# son=int(str)

# print(son)

            #3
            
# str=input('Satr: ')

# arr=str.split()

# n=len(arr[0])

# for i in arr:
#     if n>=len(i):
#         minn=i
#         break
# print(minn)

            #4
            
# def Fib(n):
#     i1=1
#     i2=1
#     if n==1 or n==2:
#         i3=1
#     else:
#         for i in range(n-2):
#             i3=i1+i2
#             i1=i2
#             i2=i3
#     return i3
    
# n=int(input('n='))

# print(Fib(n))


            #5
            
# a,b=input('a b :').split()
# a,b=b,a

# print(a,b)

            #6
            
# a,b,c=input('3 ta son: ').split()
# a=int(a)
# b=int(b)
# c=int(c)

# arr=[a,b,c]

# m=arr[0]

# for i in range(len(arr)):
#     if arr[i]<=m:
#         minn=i+1

# print(minn)

            #7  kamchiligi bor
            
# def tub(n):
#     arr=[]
#     for i in range(1,n+1):
#         s=0
#         for j in range(1,i+1):
#             if i%j==0:
#                 s+=1
#         if s==2:
#             arr.append(i)
#     return arr

# n=int(input('n='))
# print(tub(n))

            #8

# arr=list(map(float,input().split()))
# arr2=[]
# summ=0
# for i in arr:
#     m=int(i)
#     arr2.append(m)
# for i in arr2:
#     summ+=i            

# print(f'{arr2}    {summ}')

            #9

# tpl=tuple(map(int,input().split()))

# arr=list(tpl)
# s=0
# for i in arr:
#     if i%2==1:
#         s+=i
# print(s)

            #10
            
str=input("Satr kiriting: ")

str=str.upper()
satr=str.split()
s=0
for i in satr:
    ii=i[::-1]
    if i==ii:
        s+=1
print(s)