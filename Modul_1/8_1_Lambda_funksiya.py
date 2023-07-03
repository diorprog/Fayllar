            #
            
# add=lambda x,y:x+y
# print(add(5,6))

            #

# def multiple(x):
#     return lambda y: x*y

# double=multiple(2)
# print(double(3))

# triple=multiple(3)
# print(triple(4))

            #
            
# is_even=lambda n: False if n%2 else True
# arr=list(map(int,input().split()))

# print([i for i in arr if is_even(i)])

                #Mukammal son
                
# def mukammal(n):
#         s=0
#         t=False
#         for i in range(1,n):
#                 if n%i==0:
#                         s+=i
#         if s==n:
#                 t=True
#         return t

# n=int(input('n='))
# print(mukammal(n))

                #kamchiligi bor

# def mukammal(son):
#         arr1=[]
#         s=0
#         for i in son:
#                 for j in range(1,i):
#                         if i%j==0:
#                                 s+=j
#                 if s==i:
#                         arr1.append(i)
#                 s=0
#         return(arr1)

# arr=list(map(int,input().split()))

# print(mukammal(arr))

                # 1dan n gacha mukammal son

# def mukammal(n):
#         arr=[]
#         s=0
#         for i in range(1,n):
#                 for j in range(1,i):
#                         if i%j==0:
#                                 s+=j
#                 if s==i:
#                         arr.append(s)
#                 s=0
#         return arr

# n=int(input('n= '))
# print(mukammal(n))