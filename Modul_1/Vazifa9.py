            #147

# str=input('Satr: ')
# t1=0
# t2=0
# for i in range(len(str)):
#     if str[i]=='A':
#         t1+=1
#     elif str[i]=='Y':
#         t2+=1
# print(t1,t2)

            #148
            
# str=input('Satr: ')

# s=str.split()

# for i in s:
#     s2=' '.join(i)
#     for j in range(len(s2)):
#         if s2[1]=='A':
#             print(s2)

            #151
            
# str=input('Satr: ')
# t=0
# for i in range(len(str)):
#     if str[i]=='A' or str[i]=='a' or str[i]=='O' or str[i]=='o' or str[i]=='I' or str[i]=='i' or str[i]=='U' or str[i]=='u' or str[i]=='E' or str[i]=='e':
#         t+=1
# print(t)

            #152
            
# str=input('Satr: ')

# str=str[::-1]

# print(str)

            #153
            
# str=input('Satr: ')

# s=str.split()

# for i in s:
#     print(i,len(i))

            #154
            
# str=input('Son kiriting: ')
# n=0

# for i in range(len(str)):
#     n+=int(str[i])
# print(n)

            #156
            
# str=input('Satr: ')
# n1=int(input('1-son: '))
# n2=int(input('2-son: '))

# s=str.split()

# for i in  len(s):
#     if n1==i+1:
#         s1=s[i]
#         t1=i
#     if n2==i+1:
#         s2=s[i]
#         t2=i

# s[t1],s[t2]=s2,s1

# str=' '.join(s.split())

# print(str)

            #157
            
str=input('Satr: ')
n1=int(input('1-son: '))

s=str.split()

for i in  len(s):
    if n1==i+1:
        s1=s[i]
        t1=i

str=' '.join(s.split())
str=str.replace(s1,'TATU')
print(str)