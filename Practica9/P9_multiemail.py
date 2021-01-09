#!/usr/bin/env python

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import ssl
import json
import sys

m = []
data = {}
with open("data.json") as f:
    data = json.load(f)
    data = data["data"]

message = MIMEMultipart()
message["From"] = data["user"]
message["Subject"] = str(sys.argv[1])
msg = str(sys.argv[2])

message.attach(MIMEText(msg, "plain"))

sslContext = ssl.create_default_context()
server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=sslContext)

server.login(data["user"], data["pass"])

mails = open("mails.txt", "r")
for mail in mails:
    to = mail
    m.append(to)
mails.close

for element in m:
    print(element)
    message["To"] = element
    server.sendmail(message["From"], message["To"], message.as_string())
    print("Mensaje enviado a %s:" % (message["To"]))
server.quit()
