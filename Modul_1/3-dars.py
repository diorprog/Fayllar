            #f4

# a,b,c=input('3 ta son kiriting: ').split()
# a=int(a)
# b=int(b)
# c=int(c)
# summ=0
# if a>0:
#     summ+=1
# if b>0:
#     summ+=1
# if c>0:
#     summ+=1
# print(summ)

            #f15

# a,b,c=input('3 ta son kiriting: ').split()
# a=float(a)
# b=float(b)
# c=float(c)

# if a>b:
#     maxx=a
# else:
#     maxx=b
# if maxx>c:
#     maxx=maxx
# else:
#     maxx=c

# if a<b:
#     minn=a
# else:
#     minn=b
# if minn<c:
#     minn=minn
# else:
#     minn=minn

# o=a+b+c-minn-maxx

# print(maxx,o)

            #f16

a,b,c=input('3 ta son kiriting: ').split()
a=float(a)
b=float(b)
c=float(c)

if a<b and b<c:
    a*=2
    b*=2
    c*=2
else:
    a*=-1
    b*=-1
    c*=-1
print(a,b,c)