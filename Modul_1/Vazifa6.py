            #1
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

# print(car.values)

            #4
            

# phone1={
#     'name': 'Samsung',
#     'model': 'S23 Ultra',
# }

# phone2={
#     'name2': 'Iphone',
#     'model2': '14 pro max'
# }

# phone3={
#     'name3': 'Huawei',
#     'model3': 'Y22'
# }

# phone1.update(phone2)
# phone1.update(phone3)

# print(phone1)

            #6
            
# n=int(input('n='))
# nums={}
# s=0

# for i in range(1,n):
#     num={
#         i: pow(i,2)
#     }
#     nums.update(num)
    
# print(nums)

            #7
            
n=int(input('n='))
nums={}
s=0

for i in range(1,n):
    num={
        i: i
    }
    nums.update(num)
    
for i in nums:
    s+=nums[i]

print(s)