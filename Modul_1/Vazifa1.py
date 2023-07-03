            #31
# x, y = input("2 ta son kiriting probel orqali: ").split()
# x = int(x)
# y = int(y)

# if x > y:
#     print(x, y)
# else:
#     print(y, x)

            #32

# x, y, z=input('3 ta son probel orqali kiriting: ').split()
# x=int(x)
# y=int(y)
# z=int(z)

# if x>y:
#     maxx=x
# else:
#     maxx=y
# if maxx>z:
#     maxx=maxx
# else:
#     maxx=z

# if x>y:
#     minn=y
# else:
#     minn=x
# if minn>z:
#     minn=z
# else:
#     minn=minn

# print(maxx, minn)

            #33

# x, y, z=input('3 ta son probel orqali kiriting: ').split()
# x=int(x)
# y=int(y)
# z=int(z)

# d1=x+y+z
# d2=x+y/2

# if x>y:
#     maxx=x
# else:
#     maxx=y
# if maxx>z:
#     maxx=maxx
# else:
#     maxx=z
# if maxx>d1:
#     maxx=maxx
# else:
#     maxx=d1

# if x>y:
#     minn=y
# else:
#     minn=x
# if minn>z:
#     minn=z
# else:
#     minn=minn
# if minn<d2:
#     minn=minn
# else:
#     minn=d2

# print(maxx, minn**2)

            #34

# a, b, c=input('3 ta son probel orqali kiriting: ').split()
# a=int(a)
# b=int(b)
# c=int(c)

# if a<b and b<c:
#     print('Yes')
# else:
#     print('No')

            #35

# a, b, c=input('3 ta son probel orqali kiriting: ').split()
# a=int(a)
# b=int(b)
# c=int(c)

# if a>=b and b>=c:
#     a=a*2
#     b=b*2
#     c=c*2
# else:
#     a=abs(a)
#     b=abs(b)
#     c=abs(c)

# print(a, b, c)

            #36

# a, b=input('2 ta son kiriting: ').split()

# a=int(a)
# b=int(b)

# if a>b:
#     print(a)
# else:
#     print(a, b)

            #37

# a,b=input('2 ta son kiriting: ').split()

# a=int(a)
# b=int(b)

# if a>b:
#     print(a, b)
# else:
#     a=0
#     print(a,b)

            #38

# a,b,c=input('3 ta son kiriting: ').split()
# a=float(a)``
# b=float(b)
# c=float(c)

# if a>=1 and a<=3:
#     print(a)
# if b>=1 and b<=3:
#     print(b)
# if c>=1 and c<=3:
#     print(c)

            #39

# a,b=input('2 ta son kiriting: ').split()
# a=float(a)
# b=float(b)

# if a<b:
#     a=(a+b)/2
#     b=a*2*b*2
# else:
#     a=a*2*b*2
#     b=(a+b)/2
# print(a,b)

            #40

# a,b,c=input('3 ta son kiriting: ').split()
# a=int(a)
# b=int(b)
# c=int(c)

# if a>0:
#     a=a**2
# if b>0:
#     b=b**2
# if c>0:
#     c=c**2

# print(a,b,c)

            #41

# a,b,c=input('3 ta son kiriting: ').split()
# a=float(a)
# b=float(b)
# c=float(c)

# if a<1 and a>0:
#     if b<1 and b>0:
#         if c<1 and c>0:
#             if a>b:
#                 minn=b
#             else:
#                 minn=a
#             if minn<c:
#                 minn=minn
#             else:
#                 minn=c
#             if minn==a:
#                 a=(b+c)/2
#             if minn==b:
#                 b=(a+c)/2
#             if minn==c:
#                 c=(a+b)/2

# print(a,b,c)                

            #42

# a,b,c,d=input('4 ta son kiriting: ').split()
# a=float(a)
# b=float(b)
# c=float(c)
# d=float(d)

# if a<=b and b<=c and c<=d:
#     if a>=b:
#         maxx=a
#     else:
#         maxx=b
#     if maxx>=c:
#         maxx=maxx
#     else:
#         maxx=c
#     if maxx>=d:
#         maxx=maxx
#     else:
#         maxx=d
#     a=maxx
#     b=maxx
#     c=maxx
#     d=maxx
# else:
#     if a>=b:
#         minn=b
#     else:
#         minn=a
#     if minn>=c:
#         minn=c
#     else:
#         minn=minn
#     if minn>=d:
#         minn=d
#     else:
#         minn=minn
#     a=minn
#     b=minn
#     c=minn
#     d=minn

# print(a,b,c,d)
    
            #43

# x,y=input('2 ta son kiriting: ').split()
# x=float(x)
# y=float(y)

# if x<0 and y<0:
#     x=abs(x)
#     y=abs(y)
# elif x>0 and y>0:
#     x=x
#     y=y
# elif x>0 and y<0 or x<0 and y>0:
#     x=x+0.5
#     y=y+0.5

# print(x,y)

            #44

# x,y,z=input('3 ta son kiriting: ').split()
# x=float(x)
# y=float(y)
# z=float(z)

# if x+y>z and x+z>y and y+z>x:
#     print('Yes')
# else:
#     print('No')

            #45

# a,b,c=input('3 ta son kiriting: ').split()
# a=float(a)
# b=float(b)
# c=float(c)

# if b**2-4*a*c>=0:
#     x1=(-b+(b**2-4*a*c)**(1/2))/(2*a)
#     x2=(-b-(b**2-4*a*c)**(1/2))/(2*a)
#     print(x1,x2)
# else:
#     print('No')

            #46

# a=float(input('a='))

# if a<-1:
#     y=1/a**2
# elif a>=-1 and a<2:
#     y=a**2
# else:
#     y=4
# print(y)

            #47

# x=float(input('x='))
# if x<=-1:
#     y=abs(x)
# elif 1<x and x<=2:
#     y=1
# else:
#     y=-2*x+5

            #48

# a=float(input('a='))

# if a<0:
#     y=-a
# else:
#     y=-a**2
# print(y)

            #49

# x=float(input('x='))
# if x<=-1:
#     y=abs(x)


            #50

# x,y=input('2 ta son kiriting: ').split()

# x=float(x)
# y=float(y)

# if x>=-0.7 and x<=0.7:
#     if y>=-1 and y<=2:
#         print('yes')
#     else:
#         print('no')
# else:
#     print('NO')

            #51

x,y=input('2 ta son kiriting: ').split()
x=float(x)
y=float(y)

if x>=-1 and x<0 or x<=1 and x>0:
    if y<=abs(x) and y>=-2:
        print('Yes')
    else:
        print('No')
else:
    print('No')

            #52

# x,y=input('2 ta son kiriting: ').split()

# x=float(x)
# y=float(y)

# if x>=-2 and x<=1:
#     if y>=-1 and y<=1:
#         print('Yes')
#     else:
#         print('No')
# else:
#     print('No')

