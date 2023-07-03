            #1.
# a=int(input('a='))
# b=int(input('b='))
# c=int(input('c='))

# if a>b:
#     m=a
# else:
#     m=b
# if m>c:
#     m=m
# else:
#     m=c
# print(f'Natija: {m}')

            #2.

# a=int(input('a='))
# b=int(input('b='))

# a=a+b
# b=a-b
# a=a-b

# print(f'a={a}')
# print(f'b={b}')

            #3.

# a=int(input('a='))
# b=int(input('b='))
# c=int(input('c='))

# #1-usul

# if a>b and b>c or c>b and b>a:
#     n=b
# elif b>a and a>c or c>a and a>b:
#     n=a
# else:
#     n=c
# print(f"O'rtadagi {n}")

# #2-usul

# maxx=max(a, b, c)
# minn=min(a, b, c)

# d=a+b+c;
# print(d-maxx-minn)

            #4.

# a=int(input('a='))

# if a>99 and a<1000:
#     b=a//100
#     o=a//10%10
#     y=a%10
#     print(b+o+y)

            #5.
    
a=int(input('a='))

t1=a//1000
j1=a//100%10
t2=a//10%10
j2=a%10

d=t2*1000+j2*100+t1*10+j1

print(d)