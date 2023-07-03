#           #1
# def sign(x):
#     if x<0:
#         t=-1
#     elif x==0:
#         t=0
#     else:
#         t=1
#     return t

# n=int(input('n='))
# print(sign(n))

            #2
            
# def rc(a,b,c):
#     if b*b-4*a*c>0:
#         t=2
#     elif b*b-4*a*c==0:
#         t=1
#     else:
#         t=0
#     return (t)

# a,b,c=input(' 3 ta son kiriting: ').split()
# a=int(a)
# b=int(b)
# c=int(c)
# print(rc(a,b,c))

            #3
            
# def circle(r):
#     pi=3.14
#     s=pi*r**2
#     return s

# m=int(input('Radiusni kiriting: '))
# print(circle(m))

            #6

# def calc(a,b,opp):
#     if opp==1:
#         t=a-b
#     elif opp==2:
#         t=a*b
#     elif opp==3:
#         t=a/b
#     else:
#         t=a+b
    
#     return t

# a,b,opp=input('1-son 2-son va amal(sonda): ').split()
# a=int(a)
# b=int(b)
# opp=float(opp)
# print(calc(a,b,opp))

            #7

# def quarter(x,y):
#     if x>0 and y>0:
#         t='I'
#     elif x<0 and y>0:
#         t='II'
#     elif x<0 and y<0:
#         t='III'
#     elif x>0 and y<0:
#         t='IV'
#     return t

# x,y=input('koordinatalarni kiriting(x y): ').split()
# x=float(x)
# y=float(y)
# print(quarter(x,y))

            #8

# def event(k):
#     t=0
#     for i in range(1,k+1):
#         if i%2==0:
#             t+=1
#     return t

# m=int(input('m= '))
# print(event(m))

            #9
            
# def issquade(k):
#     t=0
#     for i in range(1,k+1):
#         for j in range(1,i):
#             if i!=j:
#                 if pow(i,1/2)==j:
#                     t+=1
#     return t

# n=int(input('n='))
# print(issquade(n))

            #10
            
# def ispowern(k):
#     t=0
#     for i in range(1,k+1):
#         for j in range(i):
#             if i==pow(5,j):
#                 t+=1
#     return t

# n=int(input('n='))
# print(ispowern(n))

            #11
            
# def ispowern(a,k):
#     t=0
#     for i in range(1,k+1):
#         for j in range(i):
#             if i==pow(a,j):
#                 t+=1
#     return t

# a,n=input('a n: ').split()
# a=int(a)
# n=int(n)
# print(ispowern(a,n))

            #12
            
# def isprime(n):
#     t=0
#     countt=0
#     for i in range(1,n+1):
#         for j in range(i):
#             if i%j==0:
#                 t+=1
#         if t==2:
#             countt+=1
#         t=0
#     return(countt)

# k=int(input('k='))
# print(isprime(k))

            #13

# def digitn(n):
#     arr=[]
#     s=0
#     while i>=0:
        
        
            #15
# def ispalindrom(k):
#     m=len(k)
#     for i in range(m):

            #16

# def degtorad(son):
#     arr1=[]
#     for i in son:
#         arr1.append(i*3.14/180)
#     return arr1

# arr=[0,90,360,180]
# print(degtorad(arr))

            #17
            
# def degtorad(son):
#     arr1=[]
#     for i in son:
#         arr1.append(i*180/3.14)
#     return arr1

# arr=[0,1,57,6,28,3.14]
# print(degtorad(arr))

            #14
            
            # 1ta un

# def digitn(k,n):
#     return (k//(10**(n-1)))%10

# k=int(input('k= '))
# n=int(input('n= '))

# print(digitn(k,n))

            #ko'p son un
            
def digitn(k,n):
    return (k//(10**(n-1)))%10

k=int(input('k= '))
n=int(input('n= '))

for i in k:
    m=digitn(i,n)
    print(m,end=' ')
print()