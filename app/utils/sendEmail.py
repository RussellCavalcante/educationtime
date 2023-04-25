class sendEmailModel():

    def conviteAcesso(hash,nome):

        htmlcorpo =  f"""\
        <body>
            
            <div class="centro">
                <div class="topo">
                    <img src="images/v2_90.png" width="150px" alt="">
                    <h3 class="title">Convite de Acesso ao Sistema</h5>
                </div>
                <div class="body">
                    <h4 class="subtitle">Olá, {nome}.</h4>
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
        return htmlcorpo