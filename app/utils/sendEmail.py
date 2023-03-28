import win32com.client as win32

# criar a integração com o outlook
def sendEmail(hash, emailSend):
    outlook = win32.Dispatch('outlook.application')

    # criar um email
    email = outlook.CreateItem(0)

    # configurar as informações do seu e-mail
    email.To = f"{emailSend};"
    email.Subject = "E-mail automático do Python"
    email.HTMLBody = f"""
                <p>Olá Lira, aqui é o código Python</p>

                <p>O faturamento da loja foi de R$</p>
                <p>Vendemos produtos</p>
                <p>O ticket Médio foi de R${hash}</p>

                <p>Abs,</p>
                <p>Código Python</p>
                """

    # anexo = "C://Users/joaop/Downloads/arquivo.xlsx"
    # email.Attachments.Add(anexo)

    email.Send()