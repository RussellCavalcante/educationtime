# import the smtplib module. It should be included in Python by default
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import win32com.client as win32

# criar a integração com o outlook
def sendEmail(hash, emailSend):

    
    

    # set up the SMTP server

    myemail='russell.cavalcante@poncetech.com.br'
    MY_ADDRESS = 'editoraponce@outlook.com'
    password = '@rus312519PONCE'
    PASSWORD = 'k3@UqUWWZ96u'
    s = smtplib.SMTP(host='smtp.office365.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # print(s)

    msg = MIMEMultipart()       # create a message

    # add in the actual person name to the message template
    # message = PERSON_NAME=name.title()

    # setup the parameters of the message
    msg['From']=MY_ADDRESS
    msg['To']= emailSend
    msg['Subject']="This is TEST"

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
    
    htmlcorpo =  f"""\
    <body>
        
        <div class="centro">
            <div class="topo">
                <img src="images/v2_90.png" width="150px" alt="">
                <h3 class="title">Convite de Acesso ao Sistema</h5>
            </div>
            <div class="body">
                <h4 class="subtitle">Olá, Marcos Peixoto.</h4>
                <p>Boas Vindas à Aprender Editora!<br/><br/>
                Estamos entusiasmados por ter você conosco.</p>
                <p><b>Foi criada uma área exclusiva que lhe dará acesso a nossa plataforma</b>, por meio do botão abaixo você poderá completar seu cadastro e fazer o primeiro login. Depois de fazer login,<b> você terá acesso à nossa vasta coleção de recursos todos projetados para lhe ajudar a impulsionar os indicadores educacionais.</b></p>
                <p><br/><a class="botao" href="http://projetoaprender.poncetech.com.br/primeiroacesso/{hash}">Aceitar convite</a><br/><br/></p>
                <p>Se você tiver alguma dúvida ou precisar de ajuda com seu login, não hesite em entrar em contato com nossa equipe de suporte ao cliente, que está disponível para ajudá-lo com qualquer problema ou preocupação.</p>
                <p><b>Entre em contato com (85) 3194-1300<br/><br/>
                www.aprendereditora.com.br</b></p>
                <p><br/></p>
                <p>Caso não seja você, por favor, desconsidere este e-mail.</p>
                <p><br/></p>
                <p>Equipe Aprender Editora</p>
                <p><br/></p>
            </div>
            <div class="footer">

            </div>
        </div>
    </body>
    </html>
    """

    # add in the message body
    msg.attach(MIMEText(htmltopo + htmlcorpo, 'html'))

    # send the message via the server set up earlier.
    s.send_message(msg)

    del msg
        