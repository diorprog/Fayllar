import smtplib
import time
from email.message import EmailMessage

# set your email and password
# please use App Password
email_address = "diyorbekdilmurodov1@gmail.com"
email_password = "lapwnmmecvxrakiy"

d="""saidakbaruraimov7@gmail.com
mohirmirahmadov@gmail.com
zoirbekergashev4567@gmail.com
khayrullo.devs@gmail.com
imonqulovf1234@gmail.com
samidilloravshanov13@gmail.com
shahrizodaxakimova12@gmail.com
9140380@gmail.com
shohjahonobruyev3@gmail.com
diyorbekdilmurodov1@gmail.com
suratovdoniyor@gmail.com
dilshodbekakhmatov@gmail.com
nurillayevezozbek@gmail.com
saidakbaruraimov7@gmail.com
mohirmirahmadov@gmail.com
zoirbekergashev4567@gmail.com
azamovshahboz06082001@gmail.com"""
arr=d.split()

start=time.time()
# create email
for i in arr:
    msg = EmailMessage()
    msg['Subject'] = "Email subject"
    msg['From'] = email_address
    msg['To'] = i
    msg.set_content("Salom")

    # send email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)
print(time.time()-start)