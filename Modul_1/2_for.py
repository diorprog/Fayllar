            #1

# n=int(input('n='))
# summ=0
# for i in range(n+1):
#     if i%2==1:
#         summ+=i
# print(summ)

            #2 n!!  2 ta factoriallik masala

# n=int(input('n='))

# d=1

# if n%2:
#     h=1
# else:
#     h=2

# for i in range(h,n+1,2):
#     d*=i
# print(d)

n=int(input('n='))

for i in range(1,n+1):
    for j in range(1,n+1):
        s1=0
        s2=0
        for k in range(1,(i//2)+1):
            if i%k==0:
                s1+=k
            if j%k==0:
                s2+=k
            if s1==j and s2==i and i!=j:
                print(i,j)