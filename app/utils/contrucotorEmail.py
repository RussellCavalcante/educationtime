# import the smtplib module. It should be included in Python by default
from app import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# import win32com.client as win32

# criar a integração com o outlook
def constructorEmail(emailSend, body):

    
    

    # set up the SMTP server

    # print(s)

    msg = MIMEMultipart()       # create a message

    # add in the actual person name to the message template
    # message = PERSON_NAME=name.title()

    # setup the parameters of the message
    msg['From']=MY_ADDRESS
    msg['To']= emailSend
    msg['Subject']="Editora aprender"

    htmltopo = """\
    <html>
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            *{ font-family: open sans,helvetica neue,Helvetica,sans-serif;}
            .centro{
                margin: 0 auto;
                width: 650px;
            }
            .topo{
                background-color: #E6F5E8;
                padding: 25px 0;
                text-align: center;
            }
            p{
                margin-bottom: 22px;
            }
            .body{
                padding:0 25px;
            }
            .title{
                font-size: 22px;
                color:#333333;
            }
            .subtitle{
                font-family: open sans,helvetica neue,Helvetica,sans-serif;
                font-style: normal;
                font-weight: 700;
                font-size: 25px;
                line-height: 48px;
                color: #008F2D;
            }
            .footer{
                background-color: #008F2D;
                height: 35px;
            }
            .botao{
                padding: 12px 20px;
                color:#FFF;
                background-color:#005F0B;
                text-decoration: none;
                font-size:13px;
            }
        </style>
    </head>
    """
    
    
    htmlcorpo = body

    # add in the message body
    msg.attach(MIMEText(htmltopo + htmlcorpo, 'html'))

    # send the message via the server set up earlier.
    s.send_message(msg)

    del msg
