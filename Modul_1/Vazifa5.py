            #31

# n=int(input('n='))
# arr=[]
# arr1=[]
# t=0

# for i in range(n):
#     m=int(input(f'arr[{i+1}]='))
#     arr.append(m)
# for i in range(n-1):
#     if arr[i]<arr[i+1]:
#         arr1.append(i+2)
#         t+=1
# arr1.sort()
# arr1[::-1]
# print(arr1,t)

            #32
        
# n=int(input('n='))
# arr=[]
# arr1=[]
# for i in range(n):
#     s=int(input(f'a[{i+1}]='))
#     arr.append(s)
# for i in range(n-2):
#     if arr[i]<arr[i+1] and arr[i+1]<arr[i+2]:
#         arr1.append(i+1)
# print(arr1)

            #33
            
# n=int(input('n='))
# arr=[]
# arr1=[]
# for i in range(n):
#     s=int(input(f'a[{i+1}]='))
#     arr.append(s)
# for i in range(n-2):
#     if arr[i]>arr[i+1] and arr[i+1]>arr[i+2]:
#         arr1.append(i+1)
# print(arr1)

            #34

# n=int(input('n='))
# arr=[]
# arr1=[]
# for i in range(n):
#     s=int(input(f'a[{i+1}]='))
#     arr.append(s)
# for i in range(n-2):
#     if arr[i]<arr[i+1] and arr[i+1]<arr[i+2]:
#         arr1.append(arr[i+1])
# for i in range(len(arr1)):
#     if arr[1]>=arr1[i]:
#         maxx=arr[1]
#     else:
#         maxx=arr[i]
# print(arr1)

            #37
            
# n=int(input('n='))
# arr=[]
# t=0

# for i in range(n):
#     m=int(input(f'arr[{i+1}]='))
#     arr.append(m)
# for i in range(n-1):
#     if arr[i]<=arr[i+1]:
#         t+=1
# print(t)

            #38
            
# n=int(input('n='))
# arr=[]
# t=0

# for i in range(n):
#     m=int(input(f'arr[{i+1}]='))
#     arr.append(m)
# for i in range(n-1):
#     if arr[i]>=arr[i+1]:
#         t+=1
# print(t)

            #39
            
# n=int(input('n='))
# arr=[]
# t=0
# t1=0
# for i in range(n):
#     m=int(input(f'arr[{i+1}]='))
#     arr.append(m)
# for i in range(n-1):
#     if arr[i]<=arr[i+1]:
#         t+=1
#     else:
#         t1+=1
# print(t+t1)

            #40
            
# a=float(input('a='))
# n=int(input('n='))
# arr=[]
# arr1=[]

# for i in range(n):
#     m=float(input(f'arr[{i+1}]='))
#     arr.append(m)
# for i in range(n):
#     arr1.append(arr[i]-a)
# for i in range(n):
#     if arr1[1]>=arr1[i]:
#         t=1
#     else:
#         t=i
# print(arr[t])

            #41
            
# tpl=tuple((6,1,3,2,4,3))
# arr=list(tpl)
# n=len(arr)

# for i in range(n-3):
#     if arr[i]+arr[i+1]>arr[i+2]+arr[i+3]:
#         t1=i
#         t2=i+1
#     else:
#         t1=i+2
#         t2=i+3
# print(t1+1,t2+1)

            #42
            
# tpl=tuple((5,1,2,1,3,7))
# arr=list(tpl)
# arr1=[]
# arr2=[]
# r=float(input('r:'))

# for i in range(len(arr)/2-1):
#     arr1.append(arr[i]+arr[i+1])
#     arr2.append(arr1-r)
#     if arr2[1]<arr2[i]:
#         t1=i+1
#         t2=i+2
# print(t1,t2)

            #43
            
# tpl=((1,3,4,6,7,9))
# arr=list(tpl)

# for i in range(len(arr)):
#     if i%2==0:
#         print(i+1)

            #44
            
# tpl=((5,1,2,1,3,7))
# arr=list(tpl)

# for i in range(len(arr)):
#     for j in range(len(arr)):
#         if arr[i]==arr[j] and i!=j:
#             t1=i+1
#             t2=j+1
# print(t1,t2)

            #49
            
# n=int(input('n='))
# tpl=((5,1,2,3,5,6))
# arr=list(tpl)

# for i in range(len(arr)):
#     if arr[i]>n:
#         t=arr[i]
#         break
#     else:
#         t=0
# print(t)

            