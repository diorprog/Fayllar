                #1

# a,b=input('2 ta son kiriting: ').split()
# a=int(a)
# b=int(b)

# while a>b:
#     a-=b
# print(a)

                #2

# a,b=input('2 ta son kiriting: ').split()
# a=int(a)
# b=int(b)
# s=0
# while a>b:
#     a-=b
#     s+=1
# print(s)

                #3

# a,b=input('2 ta son kiriting: ').split()
# a=int(a)
# b=int(b)
# s=0
# while a>b:
#     a-=b

# print(a,b)

                #4

# n=int(input('n='))
# while n>1:
#     n/=3

# if n==1:
#     print('True')
# else:
#     print('False')

                #5

# n=int(input('n='))
# s=0
# m=n
# while m>1:
#     m/=2
#     s+=1
# if m==1:
#     print(s)
# else:
#     print('2ning darajasi emas.')

                #6

# n=int(input('n='))
# s=0
# k=1

# while n>0:
#     n-=2
#     k*=n
# print(k)

                #7

# n=int(input('n='))
# k=1

# while k**2<n:
#     k+=1
# print(k)

                #8

# n=int(input('n='))
# k=1

# while k**2<n:
#     n-=k
#     k+=1
    
# print(k)

                #9

# n=int(input('n='))
# k=1

# while k**3<n:
#     k+=1
# print(k)

                #10

# n=int(input('n='))
# k=1

# while k**3<n:
#     n-=k
#     k+=1
    
# print(k)

                #16

# p=int(input('k='))
# s=10
# k=1
# ss=10

# while ss<=40:
#     s=s*p/100
#     k+=1
#     ss+=s
# print(ss)

                #

n=int(input('n='))
q=False
while n>0:
    if (n%10)%2:
        q=True
        break
    n//=10
print(q)