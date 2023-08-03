import smtplib,ssl
import os

def send_email(message,topic,sender):
    host = "smtp.gmail.com"
    port = 465
    username = "terese.akombo@gmail.com"
    password = os.getenv("PWD")
    receiver = "terese.akombo@gmail.com"
    my_context = ssl.create_default_context()
    message2 = f"""\
Subject: Enquiry on {topic}

From: {sender}

Topic: {topic} 

{message}
"""
    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message2)


# send_email()
