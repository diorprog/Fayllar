            #
# def add(a,b):
#     a=5
#     b=8
#     print(a+b)

# a,b=0,0
# add(a,b)

            #
            
# def convert_usd_to_uzs(n):
#     return n*11450

# def convert_uzs_to_usd(n):
#     return n/11390

# summ=float(input('summ='))

# q=bool(int(input('Qaysi amalni bajarmoqchisiz?(0/1) ')))

# if q:
#     print(convert_usd_to_uzs(summ))
# else:
#     print(convert_uzs_to_usd(summ))

            # args
            
# def summ(*args, **kwargs):
#     s=0
#     for i in args:
#         s+=i
#     return s

# p=summ(1,5,2,8,10,2.2)
# print(p)

            # kwargs

# def summ(*args, **kwargs):
#     s=0
#     for i in kwargs['massiv']:
#         s+=i
#     return s

# p=summ(a=1,b=5,c=2)
# print(p)


            # 1ta un

# def digitn(k,n):
#     return (k//(10**(n-1)))%10

# k=int(input('k= '))
# n=int(input('n= '))

# print(digitn(k,n))

            #ko'p son un
            
# def digitn(k,n):
#     return (k//(10**(n-1)))%10

# k=int(input('k= '))
# n=int(input('n= '))

# for i in k:
#     m=digitn(i,n)
#     print(m,end=' ')
# print()

                            #
                            
def fact(n):
    p=1
    for i in range(1,n+1):
        p*=i
    return p

def t(x):
    s1,s2=0,0
    for k in range(0,11):
        s1+=((x**(2*k+1)) / fact(2*k+1))
        s2+=((x**(2*k)) / fact(2*k))
    return s1/s2

y=float(input('y= '))

s=(1.7*t(0.25)+2*t(1+y)) / (6-t(y*y-1))

print(s)