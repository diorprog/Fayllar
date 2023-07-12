import threading
import time

        #
# def a():
#     time.sleep(3)
#
# def b():
#     time.sleep(3)
#
# start=time.time()
# a()
# b()
#
# print(time.time()-start)

        #

# def a():
#     time.sleep(3)
#
# def b():
#     time.sleep(3)
#
# start=time.time()
# a()
# b()
#
#
# thread1=threading.Thread(target=a)
# thread2=threading.Thread(target=b)
#
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# print(time.time()-start)


            #

# def a():
#     time.sleep(3)
#
# def b():
#     time.sleep(3)
#
# start=time.time()
# a()
# b()
#
# start=time.time()
# l=[]
#
# for i in range(1_000_000):
#     thread=threading.Thread(target=a)
#     thread.start()
#     l.append(thread)
# for i in l:
#     i.join()
# print(time.time()-start)


            #

import smtplib
import time
from email.message import EmailMessage

email_address = "diyorbekdilmurodov1@gmail.com"
email_password = "lapwnmmecvxrakiy"

start=time.time()

arr = ["saidakbaruraimov7@gmail.com",
"mohirmirahmadov@gmail.com",
"zoirbekergashev4567@gmail.com",
"khayrullo.devs@gmail.com",
"imonqulovf1234@gmail.com",
"samidilloravshanov13@gmail.com",
"shahrizodaxakimova12@gmail.com",
"shohjahonobruyev3@gmail.com",
"diyorbekdilmurodov1@gmail.com",
"suratovdoniyor@gmail.com",
"dilshodbekakhmatov@gmail.com",
"nurillayevezozbek@gmail.com",
"saidakbaruraimov7@gmail.com",
"mohirmirahmadov@gmail.com",
"zoirbekergashev4567@gmail.com",
"azamovshahboz06082001@gmail.com",
"doniyorbek068@gmail.com",
"ahmatovdilshodbek@gmail.com",
"isomiddinwtu@gmail.com",
"kodirovadilfuza9706@gmail.com",
"turgunovjamshid32@gmail.com",
"nabiyevadilnavoz736@gmail.com"]



# create email
def send_mail(mail):
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        msg = EmailMessage()
        msg['Subject'] = "Email subject"
        msg['From'] = email_address
        msg['To'] = mail
        msg.set_content("This is email message")
        smtp.login(email_address,email_password)
        smtp.send_message(msg)
        print('Send email!')
l=[]
for i in arr:
    t=threading.Thread(target=send_mail,args=(i,))
    t.start()
    l.append(t)
for j in l:
    j.join()
print(time.time()-start)