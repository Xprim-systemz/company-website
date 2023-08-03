import smtplib,ssl
host="smtp.gmail.com"
port=465
username="terese.akombo@gmail.com"
password="jnzqxbarhubwlezf"

receiver="terese.akombo@gmail.com"
my_context=ssl.create_default_context()
message="""\
Subject: Greetings!
Good to see and read from you
bye!
"""

with smtplib.SMTP_SSL(host,port,context=my_context) as server:
    server.login(username,password)
    server.sendmail(username,receiver,message)
