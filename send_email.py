import smtplib, ssl
host = "smtp.gmail.com"
port = 465

username = "a09103511843@gmail.com"
password = "radada"

receiver = "ar09103511843@gmail.com"
context = ssl.create_default_context()

message = """
Hi!
How are you?
Bye!
"""
with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)