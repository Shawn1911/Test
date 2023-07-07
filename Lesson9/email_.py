import smtplib
import threading
import time
from email.message import EmailMessage

email_address = "azamovshahboz06082001@gmail.com"
email_password = "qcwebndhymyiyddb"

email_list = ["saidakbaruraimov7@gmail.com",
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

def send_email(recipient):
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        msg = EmailMessage()
        msg['Subject'] = "Milliy turizm agentligi"
        msg['From'] = email_address
        msg['To'] = recipient
        msg.set_content("Qoqindiq come to Tashkent")
        smtp.login(email_address, email_password)
        smtp.send_message(msg)
        print("send mail !")

l = []
start = time.time()
for i in email_list:
    t = threading.Thread(target=send_email, args=(i,))
    t.start()
    l.append(t)

for i in l:
    i.join()

print(time.time() - start)

