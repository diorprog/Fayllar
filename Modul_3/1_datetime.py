#vaqt ni chiqarish


#


# import datetime

# now=datetime.datetime.now()

# print(now)


#


# import datetime

# now=datetime.datetime.now()

# print(now.year)


#


# import datetime

# now=datetime.datetime.now()

# print(now.strftime('%j'))
# print(now.timestamp())   #---sekund                      # aniq ishlash uchun stamp bn ishlanadi
# print(now.timestamp()*1000)  #---millisekund


#


# import datetime

# now=datetime.datetime.now()

# print(now + datetime.timedelta(hours=5))             # hozirgi vaqtdan 5 soat kngi vaqtni topish


#


import datetime

now=datetime.datetime.now()
dt=now+datetime.timedelta(days=12)

print(dt.strftime('%A'))
