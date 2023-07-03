            #1
            
# n=int(input('n='))
# arr=[]

# for i in range(n*2):
#     if i%2==1:
#         arr.append(i)
# print(arr)

            #2

# n=int(input('n='))
# arr=[]

# for i in range(1,n+1):
#     arr.append(2**i)
# print(arr)

            #3

# a,b,c=input('3 ta son kiriting: ').split()
# a=int(a)
# b=int(b)
# c=int(c)

# arr=[b]

# for i in range(a-1):
#     b+=c
#     arr.append(b)
# print(arr)

            #4

# a,b,c=input('3 ta son kiriting: ').split()
# a=int(a)
# b=int(b)
# c=int(c)

# arr=[b]

# for i in range(a-1):
#     b*=c
#     arr.append(b)
# print(arr)

            #5

# n=int(input('n='))
# a1=1
# a2=1

# arr=[a1,a2]

# for i in range(n-2):
#     a3=a1+a2
#     a1=a2
#     a2=a3
    
#     arr.append(a3)
# print(arr)

            #6

# a,b,c=input('3 ta son: ').split()
# a=int(a)
# b=int(b)
# c=int(c)
# s=b+c
# arr=[b,c,s]

# for i in range(a-3):
#     s+=s
#     arr.append(s)
# print(arr)
            #7
            
# import random


# n=int(input('n='))
# arr=[]

# for i in range(n):
#     s=int(input(f'arr[{i+1}]='))
#     arr.append(s)
# print(arr)
# print(arr[::-1])

            #8

# n=int(input('n='))
# arr=[]
# arr1=[]
# t=0
# for i in range(1,n+1):
#     s=int(input(f'a[{i}]='))
#     arr.append(s)
# s=0
# for i in range(1,n+1):
#     arr[i]=s
#     if s%2==0:
#         arr1.append(s)
#         t+=1
# print(arr1,t)

            #9

# n=int(input('n='))
# arr=[]
# arr1=[]
# t=0
# for i in range(n):
#     s=int(input(f'a[{i+1}]='))
#     arr.append[s]
    
# for i in range(n):
#     if arr[i]%2==1:
#         arr1.append(arr[i])
#         t+=1
# arr1.sort
# print(arr1,t)

            #10
            
# n=int(input('n='))

# arr=[]
# arr1=[]
# arr2=[]

# for i in range(n):
#     s=int(input(f'a[{i+1}]='))
#     arr.append(s)
# for i in range(n):
#     if arr[i]%2==0:
#         arr1.append(i+1)
#     else:
#         arr2.append(i+1)
# arr1.sort
# arr2.sort
# arr2[::-1]

# print(arr1,arr2)

            #11
            
# n,m=input('2 ta son: ').split()
# n=int(n)
# m=int(m)
# arr=[]
# arr1=[]

# for i in range(n):
#     s=int(input(f'a[{i+1}]='))
#     arr.append(s)
# for i in range(m):
#     arr1.append(arr[i])
# arr1[::-1]
# print(arr,arr1)

#             #12

# n=int(input('n='))
# arr=[]
# arr1=[]

# for i in range(n):
#     s=int(input(f'a[{i+1}]='))
#     arr.append(s)
# for i in range(n):
#     if i%2==1:
#         arr1.append(arr[i])
# print(arr,arr1)

            #13

# n=int(input('n='))
# arr=[]
# arr1=[]

# for i in range(n):
#     s=int(input(f'a[{i+1}]='))
#     arr.append(s)
# for i in range(n):
#     if i%2==0:
#         arr1.append(arr[i])

# arr1[::-1]
# print(arr,arr1)

           #14

# n=int(input('n='))
# arr=[]
# arr1=[]
# arr2=[]

# for i in range(n):
#     s=int(input(f'a[{i+1}]='))
#     arr.append(s)
# for i in range(n):
#     if i%2==1:
#         arr1.append(arr[i])
#     else:
#         arr2.append(arr[i])

# arr1.sort
# arr2.sort
# print(arr1,arr2)

            #15
            
# n=int(input('n='))
# arr=[]
# arr1=[]
# arr2=[]

# for i in range(n):
#     s=int(input(f'a[{i+1}]='))
#     arr.append(s)
# for i in range(n):
#     if i%2==1:
#         arr1.append(arr[i])
#     else:
#         arr2.append(arr[i])

# arr1.sort
# arr2.sort
# arr1[::-1]
# arr2[::-1]
# print(arr1,arr2)

            #16
            
# n=int(input('n='))
# arr=[]
# arr1=[]
# arr2=[]

# for i in range(n):
#     s=int(input(f'a[{i+1}]='))
#     arr.append(s)
#     arr1.append(arr[i])
# arr1.reverse()
# m=n//2
# for i in range(m):
#     arr2.append(arr[i])
#     arr2.append(arr1[i])
    
# print(arr2)

            #18
            
# n=int(input('n='))
# arr=[]
# arr1=[]
# arr2=[]

# for i in range(n):
#     s=int(input(f'a[{i+1}]='))
#     arr.append(s)
# m=arr[1]
# for i in range(n):
#     if arr[i]<m:
#         minn=i
#     else:
#         minn=i
# arr.pop(i,1)

# m=arr[1]
# for i in range(n-1):
#     if arr[i]<m:
#         minn=i
#     else:
#         minn=i
    
# print(arr2)

            #21

# n=int(input('n='))
# a,b=input('Qaysi index dan qaysi index gacha(a,b): ').split()
# a=int(a)
# b=int(b)
# arr=[]
# summ=0
# t=0
# for i in range(n):
#     s=int(input(f'a[{i+1}]='))
#     arr.append(s)
# for i in range(a,b):
#     summ+=arr[i]
#     t+=1 
# print(summ/t)

            #22

# n=int(input('n='))
# a,b=input('Qaysi index dan qaysi index gacha(a,b): ').split()
# a=int(a)
# b=int(b)
# arr=[]
# summ=0
# t=0
# for i in range(n):
#     s=int(input(f'a[{i+1}]='))
#     arr.append(s)
# for i in range(a+1):
#     summ+=arr[i]
# for i in range(b+1,n):
#     summ+=arr[i]

# print(summ)

            #23

# n=int(input('n='))
# a,b=input('Qaysi index dan qaysi index gacha(a,b): ').split()
# a=int(a)
# b=int(b)
# arr=[]
# summ=0
# t=0
# for i in range(n):
#     s=int(input(f'a[{i+1}]='))
#     arr.append(s)
# for i in range(a+1):
#     summ+=arr[i]
#     t+=1 
# for i in range(b+1,n):
#     summ+=arr[i]
#     t+=1 

# print(summ/t)

            #24

# n=int(input('n='))
# arr=[]
# for i in range(n):
#     s=int(input(f'a[{i+1}]='))
#     arr.append(s)
# for i in range(n-2):
#     if arr[i+1]-arr[i]==arr[i+2]-arr[i+1]:
#         t=arr[i+1]-arr[i]
#     else:
#         t=0
#         break

# print(t)

           #25

# n=int(input('n='))
# arr=[]
# for i in range(n):
#     s=int(input(f'a[{i+1}]='))
#     arr.append(s)
# for i in range(n-2):
#     if arr[i+1]/arr[i]==arr[i+2]/arr[i+1]:
#         t=arr[i+1]/arr[i]
#     else:
#         t=0
#         break

# print(t)

           #26

# n=int(input('n='))
# arr=[]
# for i in range(n):
#     s=int(input(f'a[{i+1}]='))
#     arr.append(s)
# for i in range(n):
#     if arr[i]%2==1 and arr[i+1]==0 or arr[i]%2==0 and arr[i+1]==1:
#         t=0
#     else:
#         t=arr[i]
#         break

# print(t)

           #27

# n=int(input('n='))
# arr=[]
# for i in range(n):
#     s=int(input(f'a[{i+1}]='))
#     arr.append(s)
# for i in range(n):
#     if arr[i]>0 and arr[i+1]<0 or arr[i]<0 and arr[i+1]>1:
#         t=0
#     else:
#         t=arr[i]
#         break

# print(t)

#             #28

# n=int(input('n='))
# arr=[]
# for i in range(n):
#     s=int(input(f'a[{i+1}]='))
#     arr.append(s)
# m=arr[1]
# for i in range(n):
#     if i%2==1:
#         if m<arr[i]:
#             minn=m
#         else:
#             minn=arr[i]
# print(minn)

             #29

# n=int(input('n='))
# arr=[]
# for i in range(n):
#     s=int(input(f'a[{i+1}]='))
#     arr.append(s)
# m=arr[1]
# for i in range(n):
#     if i%2==0:
#         if m<arr[i]:
#             maxx=arr[i]
#         else:
#             maxx=m
# print(maxx)

             #30

# n=int(input('n='))
# arr=[]
# arr1=[]
# t=0
# for i in range(n):
#     s=int(input(f'a[{i+1}]='))
#     arr.append(s)
# for i in range(n-2):
#     if arr[i]<arr[i+1]:
#         arr1.append(i+1)
#         t+=1
# arr1.sort()
# print(arr1,t)

            #31
            
# n=int(input('n='))
# arr=[]
# arr1=[]
# t=0
# for i in range(n):
#     s=int(input(f'a[{i+1}]='))
#     arr.append(s)
# for i in range(n-2):
#     if arr[i]>arr[i+1]:
#         arr1.append(i+1)
#         t+=1
# arr1.sort()
# arr1.reverse()
# print(arr1,t)

            #32
            
# n=int(input('n='))
# arr=[]
# arr1=[]
# t=0
# for i in range(n):
#     s=int(input(f'a[{i+1}]='))
#     arr.append(s)
# for i in range(n-2):
#     if arr[i]<arr[i+1] and arr[i+1]<arr[i+2]:
#         arr1.append(i+1)
#         t+=1
# arr1.sort()
# arr1.reverse()
# print(arr1,t)

            #33
            
# n=int(input('n='))
# arr=[]
# arr1=[]
# t=0
# for i in range(n):
#     s=int(input(f'a[{i+1}]='))
#     arr.append(s)
# for i in range(n-2):
#     if arr[i]>arr[i+1] and arr[i+1]>arr[i+2]:
#         arr1.append(i+1)
#         t+=1
# print(arr1,t)
