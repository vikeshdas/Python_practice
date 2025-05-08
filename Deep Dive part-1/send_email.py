from email.message import EmailMessage
import smtplib

email=EmailMessage()
email['from']='Python <masterpythonprograming@gmail.com>'
email['to']='vk0015262@gmail.com'
email['subject']='Good job python'
email.set_charset('this body of email')


# make connection to the smtp server,we have used with so that it will close conneciton automatically.

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp :
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login('masterpythonprograming@gmail.com','password')
    smtp.send_message(email)
    print("mail was send")
