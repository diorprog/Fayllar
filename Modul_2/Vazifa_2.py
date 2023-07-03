            #1

# class Vektor_xy:
#     def __init__(self,x1,x2,y1,y2):
#         self.x1=x1
#         self.x2=x2
#         self.y1=y1
#         self.y2=y2
#     def __str__(self):
#         return f'({self.x1},{self.y1})   ({self.x2},{self.y2})'
    
# class Vektor_xy_amal(Vektor_xy):
#     def __init__(self, x1, x2, y1, y2):
#         super().__init__(x1, x2, y1, y2)
    
#     def vektor(x1,x2,y1,y2):
#         v=float(v)
#         v=((x1**2+x2**2)*(y1**2+y2**2))**0.5
#         return v

# objj=[]

# for i in range(2):
#     print(f'{i+1}-vektor uchun: ')
#     x1=int(input('x1= '))
#     y1=int(input('y1= '))
#     x2=int(input('x2= '))
#     y2=int(input('y2= '))
#     obj1=Vektor_xy_amal(x1,x2,y1,y2)
#     objj.append(obj1)

# for elemen in objj:
#     print(elemen)

            #3
            
# class Kitob:
#     def __init__(self,name,writer,publisher,year):
#         self.name=name
#         self.writer=writer
#         self.publisher=publisher
#         self.year=year
#     def __str__(self):
#         return f'Nomi: {self.name}  Yozgan: {self.writer}  Nashriyoti: {self.publisher}  Yili: {self.year}'
    
# class Uy_kutubxonasi(Kitob):
#     def __init__(self, name, writer, publisher, year):
#         super().__init__(name, writer, publisher, year)
# objj=[]

            #4
            
# class Satr:
#     def __init__(self,a,b,f,s):
#         self.a=a
#         self.b=b
#     def __str__(self):
#         return f'Natija: {s}'

# class Arif_amal(Satr):
#     def __init__(self, a, b, f, s):
#         super().__init__(a, b, f, s)
        
#         if f=='+':
#             s=a+b
#         elif f=='-':
#             s=a-b
#         elif f=='*':
#             s=a*b
# a=input('a= ')
# b=input('b= ')
# f=input('Qaysi amal: ')

# calll=Arif_amal(a,b,f,0)

            #5
            
# class Shaxs:
#     def __init__(self,full_name,age,address,call_num):
#         self.full_name=full_name
#         self.age=age
#         self.address=address
#         self.call_num=call_num
    
#     def __str__(self):
#         return f'{self.full_name} | {self.age} | {self.address} | {self.call_num}'
    

# class Talaba(Shaxs):
#     def __init__(self, full_name, age, address, call_num):
#         super().__init__(full_name, age, address, call_num)


# n=int(input('n='))
# objects=[]

# for i in range(n):
#     print(f'{i+1}-shaxs ')
#     full_name=input('Full name: ')
#     age=int(input('Age: '))
#     address=input('Address: ')
#     call_num=input('University: ')
#     obj1=Talaba(full_name,age,address,call_num)
#     objects.append(obj1)

# objects = sorted(objects,key=lambda x: x.age)                               # yosh bo'yicha sortirovka qilish tartiblash

# for element in objects:                                                     #element oddiy o'zgaruvchi asosiy kod elementi emas
#     print(element)
