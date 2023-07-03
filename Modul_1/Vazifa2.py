            #if17

# a,b,c=input('3 ta son kiriting: ').split()
# a=int(a)
# b=int(b)
# c=int(c)

# if a>b and b>c or a<b and b<c:
#     a*=2
#     b*=2
#     c*=2
# else:
#     a*=-1
#     b*=-1
#     c*=-1
# print(a,b,c)

            #if18

# a,b,c=input('3 ta son kiriting: ').split()
# a=int(a)
# b=int(b)
# c=int(c)

# if a==b:
#     d=3
# elif a==c:
#     d=2
# elif b==c:
#     d=1
# else:
#     d=0
# print(d)

            #if19

# a,b,c,d=input('4 ta son kiriting: ').split()
# a=int(a)
# b=int(b)
# c=int(c)
# d=int(d)

# if a==b and b==c:
#     n=4
# elif a==b and b==d:
#     n=3
# elif a==c and c==d:
#     n=2
# elif b==c and c==d:
#     d=1
# else:
#     d=0
# print(n)

            #if20

# a,b,c=input("3 nuqta o'rnini kiriting: ").split()
# a=int(a)
# b=int(b)
# c=int(c)

# if a-b>a-c:
#     print(a-c)
# else:
#     print(a-b)

            #if21

# x,y=input('(x,y) ni kiriting: ').split()
# x=int(x)
# y=int(y)

# if y==0 and (x>0 or x<0):
#     n=1
# elif x==0 and (y>0 or y<0):
#     n=2
# elif x==0 and y==0:
#     n=0
# else:
#     n=3
# print(n)

            #if22

# x,y=input('(x,y) ni kiriting(koordinata boshida yotmagan son): ').split()
# x=int(x)
# y=int(y)

# if x>0 and y>0:
#     print('1-chorakda')
# elif y>0 and x<0:
#     print('2-chorak')
# elif x<0 and y<0:
#     print('3-chorak')
# elif x>0 and y<0:
#     print('4-chorak')

            #if23

            #if24

# from cmath import sin


# x=float(input('x='))

# if x>0:
#     y=2*sin(x)
# else:
#     y=x-6
# print(y)

            #if25

# x=float(input('x='))

# if x<-2 or x>2:
#     y=2*x
# else:
#     y=-3*x
# print(y)

            #if26

# x=float(input('x='))

# if x<=0:
#     y=-1*x
# elif 0<x and x<2:
#     y=x**2
# else:
#     y=4
# print(y)

            #if27

# x=float(input('x='))

# if x<0:
#     y=0
# elif x%2==0:
#     y=1
# else:
#     y=-1
# print(y)

            #if28

# a=int(input('a='))

# if a%4==0 and a%400==0:
#     n=366
# else:
#     n=365
# print(n)

            #if29

# a=int(input('a='))

# if a>0:
#     if a%2==0:
#         print('Musbat juft son')
#     else:
#         print('Musbat toq son')
# elif a<0:
#     if a%2==0:
#         print('Manfiy juft son')
#     else:
#         print('Manfiy toq son')
# else:
#     print('Nol')

            #if30

# a=int(input('a='))

# if a>0 and a<10:
#     if a%2==0:
#         print('1 xonali juft son')
#     else:
#         print('1 xonali toq son')
# elif a>9 and a<100:
#     if a%2==0:
#         print('2 xonali juft son')
#     else:
#         print('2 xonali toq son')
# elif a>99 and a<1000:
#     if a%2==0:
#         print('3 xonali juft son')
#     else:
#         print('3 xonali toq son')


        # Mustaqil yechish uchun masalalardan

            #1

# n=int(input('n='))

# for i in range(1,n+1):
#     if n%i==0:
#         print(i)

            #2

# n=int(input('n='))
# summ=0
# for i in range(1,n+1):
#     if n%i==0:
#         summ+=i
# print(summ)

            #3

# n=int(input('n='))
# summ=0
# for i in range(1,n):
#     if n%i==0:
#         summ+=i
# if summ==n:
#     print('Mukammal son')
# else:
#     print('Mukammal son emas')

            #4

# n=int(input('n='))
# summ=0

# for i in range(1,n+1):
#     for j in range(1,i):
#         if i%j==0:
#             summ+=j
#     if summ==i:
#         print(i)
#     summ=0

            #5

# n=int(input('n='))

# for i in range(n):
#     if i%3==0 and i%5!=0:
#         print(i)

            #6

# n=int(input('n='))
# summ=0

# for i in range(1,n+1):
#     if n%i==0:
#         summ+=1
# if summ==2:
#     print('Tub')
# else:
#     print('Tub emas')

            #7

# n=int(input('n='))
# summ=0

# for i in range(1,n):
#     for j in range(i):
#         if i%j==0:
#             summ+=1
#     if summ==2:
#         print(j)
#     summ=0

            #8

            #10
            #a
# n=int(input('n='))
# m=1

# for i in range(1,n+1):
#     m*=2
# print(m)

            #b

# n=int(input('n='))
# m=1

# for i in range(1,n+1):
#     m*=i
# print(m)

            #c

# n=int(input('n='))
# m=1

# for i in range(1,n+1):
#     m*=1+(1/i**2)
# print(m)

            #d

# n=int(input('n='))
# m=1

# for i in range(1,n+1):
#     m*=pow(2+)
# print(m)

            #f

# from cmath import sin


# n=int(input('n='))
# m=0

# for i in range(1,n+1):
#     m+=1/(sin(1)+sin(n))
# print(m)

            #g

# from cmath import cos, sin


# n=int(input('n='))
# m=0

# for i in range(1,n+1):
#     m+=(cos(1)+cos(n))/(sin(1)+sin(n))
# print(m)

            #11
            #a

# n=int(input('n='))
# m=0

# for i in range(1,n+1):
#     m+=1/(i**2)
# print(m)

            #b

# n=int(input('n='))
# m=0

# for i in range(1,n+1):
#     m+=1/(i**3)
# print(m)

            #c

# n=int(input('n='))
# m=0
# f=1

# for i in range(1,n+1):
#     for j in range(i):
#         f*=j
#     m+=1/f
# print(m)

            #d

# n=int(input('n='))
# m=0

# for i in range(1,n+1):
#     m+=1/pow(2*i,2)
# print(m)

            #e

# n=int(input('n='))
# m=1

# for i in range(2,n+1):
#     m*=(i+1)/(i+2)
# print(m)

            #f

# n=int(input('n='))
# m=1
# f=1

# for i in range(2,n+1):
#     for j in range(i):
#         f*=j
#     m*=pow(1+1/f,2)
# print(m)

            #12
            #a

# a=int(input('a='))
# n=int(input('darajasi: '))
# m=a

# for i in range(1,n):
#     m*=a
# print(m)

            #b

# a=int(input('a='))
# n=int(input('darajasi: '))
# m=1

# for i in range(1,n):
#     m*=a*(a+n)
# print(m)

            #c

# a=int(input('a='))
# n=int(input('darajasi: '))
# m=0
# t=a

# for i in range(1,n):
#     for j in range(i):
#         m+=1/t
#         t*=a+n
# print(m)
