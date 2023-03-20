import os, smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path

def SMTP(sender, receiver, subject, cc, body, attachementImage):
    message=MIMEMultipart()
    message['from']=str(sender)
    message['to']=str(receiver)
    message['subject']=str(subject)
    message['cc']=list(str(cc).split(","))
    message.attach(MIMEText(str(body)))
    message.attach(MIMEImage(Path(str(attachementImage)).read_bytes()))

    filename = "BIODIVERSITY.pdf"
    attachment = open("F:\workingprojects\EmailServer\BIODIVERSITY.pdf", "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read ())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    message.attach(part)

    with smtplib.SMTP(host="smtp.gmail.com",port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(os.environ.get("FROMEMAIL"),os.environ.get("PASSWORD"))
        smtp.send_message(message)
        print("sent!")
        
    return ("finished perfectly!")