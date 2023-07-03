# car= {
#     'name': 'BMW',
#     'model': 'x6',
#     'year': 2023,
#     'color': 'black',
#     'is_electric': True
# }
#     #element qo'shish
# car['h_p']=1000
#     #
# print(car['name'], car['model'],car['h_p'])

# print(car)


            #qo'lda kiritish:

# name=input('Name: ')
# model=input('Model: ')
# year=int(input('Year: '))
# color=input('Color: ')
# is_electric=bool(int(input('is_electric: ')))

# car= {
#     'name': name,
#     'model': model,
#     'year': year,
#     'color': color,
#     'is_electric': is_electric
# }

# print(car)

            #boshqa usulda{ Kamchiligi bor to'g'irlanishi kerak!!!}
            
# k=0
# car={}
# keys=['name', 'model', 'year', 'color', 'is_electric']

# for i in (name,model,year,color,is_electric):
#     car.update({keys[k]:i})
#     k+=1
# car.update(({'h_p':1000}))

# if car['year']>2020:
#     print(car)
# else:
#     print("yo'q!!!")

        #

# n=int(input('n='))
# cars=[]

# for i in range(n):
#     print(f'{i+1}-mashina ')
#     name=input('name: ')
#     model=input('model: ')
#     year=int(input('year: '))
#     color= input('color: ')
#     is_electric=bool(int(input('is_electric: ')))
    
#     car={
#         'name': name,
#         'model': model,
#         'year': year,
#         'color': color,
#         'is_electric': is_electric
#     }
    
#     cars.append(car)

# print(cars)

# for i in cars:
#     if i['year']>2020:
#         print(i)

            # Sorted keys and values
            
variable={
    'key1':'value1',
    'key2':'value2'
}
print(variable)
print(variable.keys())
print(variable.values())

print(sorted(variable.keys()))
print(sorted(variable.values()))