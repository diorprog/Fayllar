

# import pandas

# txt=pandas.read_csv('D:\Python\Modul_3\2_test_file\example.csv')                #system fayllarni o'qish uchun 

# print(txt.values[3])



#



# import pandas as pd

# data={
#     'name':['Amirxon','Doniyor','Yodgorbek','Doniyorbek'],
#     'age':[23,17,21,27],
#     'address':['Samarqand','Andijon','Andijon','Toshkent'],
# }

# dt = pd.DataFrame(data)
# print(dt)


#


# import pandas as pd

# data={
#     'name':['Amirxon','Doniyor','Yodgorbek','Doniyorbek'],
#     'age':[23,17,21,27],
#     'address':['Samarqand','Andijon','Andijon','Toshkent'],
# }

# dt = pd.DataFrame(data)

# dt.to_csv('example2.csv',index=False)



#



# import csv

# f=open('example2.csv','r')
# reader=csv.reader(f)
# for row in reader:
#     print(row)



#



# import csv

# f=open('example2.csv','r')
# f2=open('example3.csv','w')
# reader=csv.reader(f)
# writer=csv.writer(f2)
# for row in reader:
#     writer.writerow(row)



#



# import csv

# f=open('example2.csv','r')
# f2=open('example3.csv','w', newline='')
# reader=csv.reader(f)
# writer=csv.writer(f2)
# for row in reader:
#     try:
#         if row[1].isdigit() and int(row[1])>=20:
#          writer.writerow(row)
#     except:
#         pass



#



import pandas as pd

xlsx=pd.read_excel('D:\Python\Modul_3\2_test_file\example.xlsx')

f=open('input.txt','w')
f.write(xlsx.to_string(index=False))