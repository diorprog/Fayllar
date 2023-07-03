                #
                  
# class Human:
#     full_name='Muminov Isomiddin'
#     age=19
#     address='Andijon viloyati'

# print(Human().full_name,Human().address)


                #

# class Human:
#     def __init__(self,full_name,age,address):                      #konstruktor yozilishi class konstruktor      __init__    ------> dunder metod
#         self.full_name=full_name                                   #self._____     class maydoni   ...=______    biz bergan parametrlar
#         self.age=age
#         self.address=address
        
# obj1=Human('Ibrohimov Saidakbar',19,'Andijon viloyati')

# print(obj1.full_name,obj1.age,obj1.address)


                #
                
# class Human:
#     def __init__(self,full_name,age,address):
#         self.full_name=full_name
#         self.age=age
#         self.address=address
    
#     def __str__(self):
#         return f'{self.full_name} | {self.age} | {self.address}'

# n=int(input('n='))
# objects=[]

# for i in range(n):
#     print(f'{i+1}-shaxs ')
#     full_name=input('Full name: ')
#     age=int(input('Age: '))
#     address=input('Address: ')
#     obj1=Human(full_name,age,address)
#     objects.append(obj1)

# for element in objects:
#     print(element)


                #
                
                
                
class Human:
    def __init__(self,full_name,age,address):
        self.full_name=full_name
        self.age=age
        self.address=address
    
    def __str__(self):
        return f'{self.full_name} | {self.age} | {self.address}'
    

class Student(Human):
    def __init__(self, full_name, age, address, university):
        super().__init__(full_name, age, address)
        self.university=university


n=int(input('n='))
objects=[]

for i in range(n):
    print(f'{i+1}-shaxs ')
    full_name=input('Full name: ')
    age=int(input('Age: '))
    address=input('Address: ')
    university=input('University: ')
    obj1=Student(full_name,age,address,university)
    objects.append(obj1)

objects = sorted(objects,key=lambda x: x.age)                               # yosh bo'yicha sortirovka qilish tartiblash

for element in objects:                                                     #element oddiy o'zgaruvchi asosiy kod elementi emas
    print(element)
