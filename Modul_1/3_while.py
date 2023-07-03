            #1

# n=int(input('n='))
# s=0
# k=1

# while k<=n:
#     s+=k
#     k+=1

# print(s)

            #2

# n=int(input('n='))
# s=0

# while n!=0:
#     s+=n%10
#     n=n//10

# print(s)

            #3

# n=int(input('n='))
# s=0

# while n!=0:
#     m=n%10
#     s=s*10+m
#     n=n//10
# print(s)
    
            #4 10 likdan 2 likka o'tish  1-usul

# n=int(input('n='))
# s=0

# while n!=0:
#     q=n%2
#     s=s*10+q
#     n=n//2
# print(s)

# ss=0

# while s!=0:
#     m=s%10
#     ss=ss*10+m
#     s=s//10

# print(ss)

            # 2-usul

n=int(input('n='))
s=0
k=0

while n>=1:
    r=n%2
    s+=r*10**k
    k+=1
    n//=2
print(s)