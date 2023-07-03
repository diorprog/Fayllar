# a=int(input("a="))
# b=int(input("b="))

# print(a+b)

            #fibonachi
            
# n=int(input('n='))
# i1,i2=1,1
# s=0
# arr=[]

# for _ in range(3,n+1):
#     arr.append(i1)
#     print(i1)
#     i3=i1+i2
#     i1=i2
#     i2=i3
# print(arr)


            #fibonachi tupleda
            
# n=int(input('n='))
# a1=1
# a2=1
# s=a1+a2
# arr=[a1,a2]

# for i in range(n-2):
#     s=a1+a2
#     a1=a2
#     a2=s
#     arr.append(s)
# tpl=tuple(arr)

# print(tpl)

        #fibonachi osonroq
        
# n=int(input('n='))
# arr=[1,1]

# for i in range(2,n):
#     s=arr[i-2]+arr[i-1]
#     arr.append(s)

# tpl=tuple(arr)
# print(tpl)

        #

# n=int(input('n='))
# st=set()
# m=0
# k=0
# while n>=k:
#     for i in range(n):
#         if n%i==0:
#             m+=1
#     if m==2:
#         st.add(m)
#     m=0
#     k+=1
# print(st)

        #

# n=int(input('n='))
# humans=[]

# for i in range(n):
#     print(f'{i+1}-odam ')
#     name=input('name: ')
#     surname=input('surname: ')
#     year=int(input('year: '))
    
#     human={
#         'name': name,
#         'surname': surname,
#         'year': year,
#     }
    
#     humans.append(human)

# for i in humans:
#     if 2023-i['year']>20:
#         print(i)

            #

# n=int(input('n='))
# nums={}

# for i in range(1,n):
#     num={
#         i: pow(i,2)
#     }
    
#     nums.update(num)

# print(nums)

            #
            

# n=int(input('n='))
# nums={}
# s=0

# for i in range(1,n):
#     num={
#         i: pow(i,2)
#     }
#     nums.update(num)
    
# for i in nums:
#     s+=nums[i]

# print(s)

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

                # matndagi probellar sonini 1 ta probel qilish
                
# str=input('Satr: ')
#                         #1-usul
# # for i in range(len(str)):
# #         if str.find('  '):
# #                 str=str.replace('  ',' ')
                       
#                         #2-usul
# str=' '.join(str.split())

# print(str)

                #
                
# cars=[
#         {
#                 'name': 'BMW',
#                 'year': 2023
#         },
#         {
#                 'name': 'Damas',
#                 'year': 2018
#         },
#         {
#                 'name': 'Chevrolet',
#                 'year': 2020
#         }
# ]

# print(sorted(cars, key=lambda x: x['name']))

                #

# str=input('Satr: ')

# m=str.split()

# for i in m:
#         if i==i[::-1]:
#                 print(i)

                #
                
# str=input('Satr: ')

# arr=str.split()

# str2=str
# str2=str2[::-1]

# arr2=str2.split()

# for i in arr:
#         for j in arr2:
#                 if i==j:
#                         print(i)

                #
                
# str=input('Satr: ')

# arr=str.split()
# t=len(arr[0])

# for i in arr:
#         if t>len(i):
#                 m=t
#         else:
#                 m=len(i)
# print(m)

        #

# s=input('str= ')

# s2=s.split()

# m=len(s2[0])
# for i in s2:
#     if len(i)>m:
#         m=len(i)
#         j=i
# print(j)

                #
                
# s=input('str= ')

# s2=s.split()

# m=len(s2[0])
# for i in s2:
#     if len(i)>m:
#         m=len(i)
#         maxx=i

# for i in s2:
#     if len(i)<m:
#         m=len(i)
#         minn=i



# print(maxx, minn)


                        #
                #1-
                        
# def form(t,s):
#         a=1.2
#         b=s
#         m1=(a*a+b*b)/(a*a+2*a*b+3*b*b+4)
#         a=t
#         b=s
#         m2=(a*a+b*b)/(a*a+2*a*b+3*b*b+4)
#         a=2*s-1
#         b=s*t
#         m3=(a*a+b*b)/(a*a+2*a*b+3*b*b+4)
#         return m1+m2+m3

# t,s=input('2 ta son: ').split()
# t=float(t)
# s=float(s)

# print(form(t,s))

                #2-
                
# def G(a,b):
#         p=(a*a+b*b)/(a*a+2*a*b+3*b*b+4)
#         return G

# t,s=input('2 ta son: ').split()
# t=float(t)
# s=float(s)

# ss=G(1.2,s)+G(t,s)+G(2*s-1,t*s)

# print(round(ss,2))

                        #
                        
# def h(a,b):
#         m=(a/(1+b*b))+(b/(1+a*a))-((a-b)**3)
#         return m
# s=float(input('n1='))
# t=float(input('n2='))

# ss=h(s,t)+max(h(s-t,s*t),h(s-t,s+t))+h(1,1)

# print(round(ss,2))

                        #
                       
# def func(n):
#         ss=0
#         for i in range(10**n,10**(n+1)):
#                 m=i
#                 s=1
#                 while m>0:
#                         a=m%10
#                         s*=a
#                         m=m//10
#                 ss+=s
#         return ss
         
# n=int(input('n='))

# print(func(n-1))