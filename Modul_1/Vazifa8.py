            #1
            
# import zeroconf


# n=int(input('n='))
# str=input('Satr: ')

# if n<len(str):
#     str.split('!','@','#','$','%','^',"&","*",'(',')','=','+','-','_')
# else:
#     str='....'+str

# print(str)

            #2

# n1=int(input('n1='))
# n2=int(input('n2='))
# s1=input('Satr1: ')
# s2=input('Satr2: ')

# s=s1[:n1]+s2[n2:]

# print(s)

            #3

# s=input('Satr: ')
# c=input('Simvol: ')

# s=s.replace(c,f'{c}{c}')

# print(s)

            #4
            
# s1=input('Satr1: ')
# s2=input('Satr2: ')
# c=input('Simvol: ')

# s=s1.replace(c,f'{s2}{c}')

# print(s)

            #5
            
# s1=input('Satr1: ')
# s2=input('Satr2: ')
# c=input('Simvol: ')

# s=s1.replace(c,f'{c}{s2}')

# print(s)

            #6

# s1=input('s1= ')
# s2=input('s2= ')
# start_index=0
# t=False

# for i in range(len(s1)):
#     j=s1.find(s2,start_index)
#     if j!=-1:
#         start_index=j+1
#         t=True
#         break
# print(t)

            #7
            
# s1=input('s1= ')
# s2=input('s2= ')
# start_index=0
# counter=0

# for i in range(len(s1)):
#     j=s1.find(s2,start_index)
#     if j!=-1:
#         start_index=j+1
#         counter+=1
# print(counter)

            #8

# s1=input('Satr1: ')
# s2=input('Satr2: ')

# s=s1.replace(s2,'',1)

# print(s)

            #9
            
# s1=input('Satr1: ')
# s2=input('Satr2: ')

# s1[::-1]
# s2[::-1]

# s1=s1.replace(s2,'',1)
# s1[::-1]
# print(s1)

            #10

# s1=input('Satr1: ')
# s2=input('Satr2: ')

# s=s1.replace(s2,'')

# print(s)

            #11
            
# s=input('satr1= ')
# s1=input('satr2= ')
# s2=input('satr3: ')

# s=s.replace(s1,s2,1)

# print(s)

            #12

# s=input('satr1= ')
# s1=input('satr2= ')
# s2=input('satr3: ')

# s[::-1]
# s1[::-1]
# s2[::-1]
    
# s=s.replace(s1,s2,1)
# s[::-1]
# print(s)

            #13
            
# s=input('satr1= ')
# s1=input('satr2= ')
# s2=input('satr3: ')

# s=s.replace(s1,s2)

# print(s)

            #14
            
s=input('satr= ')

print(s.split()[1])                 #split massiv element qabul qiladi massivga aylantirib o'zlashtiradi