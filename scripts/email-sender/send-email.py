import smtplib, ssl
import time

port = 587  # For starttls
smtp_server = "smtp.office365.com"
sender_email = "maddalenabin@hotmail.com"
# receiver_email = ["maddalenabin@gmail.com","maddalena.bin@fysik.su.se"]
# receiver_email = "maddalenabin@gmail.com,maddalena.bin@fysik.su.se"
receiver_email = "maddalenabin.tests@gmail.com" # "maddalenabin@hotmail.com"
# password = input("Type your password and press enter:")
password = "MaxIVNanoMax2019"

# from email.message import EmailMessage

context = ssl.create_default_context()
timestamp = time.strftime("%Y-%m-%d %H-%M-%S")

# -- this works
# "Test email" 
message = f"""Subject: this is a test for myself
From: Maddalena <{sender_email}>
To: {receiver_email}

Last attempt to make it work.
The timestamp is {timestamp}"""

with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email.split(','), message)

"""
# Import the email modules we'll need
# import smtplib
from email.parser import BytesParser, Parser
from email.policy import default


# If the e-mail headers are in a file, uncomment these two lines:
# with open(messagefile, 'rb') as fp:
#     headers = BytesParser(policy=default).parse(fp)

#  Or for parsing headers in a string (this is an uncommon operation), use:
headers = Parser(policy=default).parsestr(
        'From: Foo Bar <maddalenabin.tests@gmail.com>\n'
        'To: <maddalenabin.tests@gmail.com>\n'
        'Subject: Test message\n'
        '\n'
        'Body would go here\n')

#  Now the header items can be accessed as a dictionary:
print('To: {}'.format(headers['to']))
print('From: {}'.format(headers['from']))
print('Subject: {}'.format(headers['subject']))

# You can also access the parts of the addresses:
print('Recipient username: {}'.format(headers['to'].addresses[0].username))
print('Sender name: {}'.format(headers['from'].addresses[0].display_name))
"""