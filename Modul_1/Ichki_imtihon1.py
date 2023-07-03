                #4

# str=input('Satr: ')

# s=str.split()
# arr=[]

# for i in s:
#     s1=i[::-1]
#     arr.append(s1)
    
# s2=' '.join(arr)

# print(s2)

                #5
                
# n=int(input('n='))
# arr=[]

# for i in range(n):
#     s=int(input(f'{i+1}-son: '))
#     arr.append(s)
    
# summ=0

# for i in arr:
#     if i%2==0 or i%3==0 or i%5==0:
#         summ+=i
        
# print(summ)

                #6

# arr=list(map(int,input().split()))

# maxx,minn=arr[0],arr[0]
# m1=m2=0
# for i in range(len(arr)):
#     if minn>arr[i]:
#         minn=arr[i]
#         m1=i
        
#     if maxx<arr[i]:
#         maxx=arr[i]
#         m2=i

# arr[m2],arr[m1] = arr[m1],arr[m2]

# print(arr)

                #1
                
str=input('satr: ')
s=''
s1=''
for i in range(len(str)):
    if str[i]=='(' and str[i+1]!=')':
        s=str[i]+s
    else:
        s+=str[i]
s=s.replace('(','')
s=s.replace(')','')
print(s)

# str=input('satr: ')
# s=''
# s1=''
# for i in range(len(str)):
#     if str[i]=='(':
#         i1=i
#     if str[i]==')':
#         i2=i
#     if str[i]=='(' or str[i]==')':
#         for i in range(i1,i2):
#             s=str[i]+s
#     else:
#         s+=str[i]
#         s1=''
    
    
# print(s)

                #2

# n=int(input('n='))
# k=int(input('k='))
# t=0

# while n>k:
#     n=n-k
#     t+=1
    
# print(t,n)

                #3
                
# n=int(input('n='))
# k=i=1
# s=1
# while n>=k:
#     i+=1
#     k=i*i
# print(i)