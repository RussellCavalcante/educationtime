
# import the smtplib module. It should be included in Python by default
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# set up the SMTP server

myemail='russell.cavalcante@poncetech.com.br'
MY_ADDRESS = 'editoraponce@outlook.com'
password = '@rus312519PONCE'
PASSWORD = 'k3@UqUWWZ96u'
s = smtplib.SMTP(host='smtp.office365.com', port=587)
s.starttls()
s.login(MY_ADDRESS, PASSWORD)

print(s)

msg = MIMEMultipart()       # create a message

# add in the actual person name to the message template
# message = PERSON_NAME=name.title()

# setup the parameters of the message
msg['From']=MY_ADDRESS
msg['To']= email
msg['Subject']="This is TEST"

# add in the message body
msg.attach(MIMEText('russell', 'plain'))

# send the message via the server set up earlier.
s.send_message(msg)

del msg