from flask import Flask, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
# from flask_script import Manager
# from flask_migrate import Migrate
# from flask_login import LoginManager
from flask_cors import CORS
from flask_jwt_extended import JWTManager
import pyodbc
conn = pyodbc.connect("Driver={ODBC Driver 18 for SQL Server};Server=tcp:sql-poncetech.database.windows.net,1433;Database=editora-aprender-homolog-2023-2-16-16-50;Uid=poncetech-admin;Pwd=12@editora@12!;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
# conn = pyodbc.connect("Driver={ODBC Driver 18 for SQL Server};Server=tcp:editora-aprender-teste.database.windows.net,1433;Database=editora-aprender-homolog;Uid=poncetechadm;Pwd=@Ponce1234;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
conn.autocommit = True
import smtplib

myemail='russell.cavalcante@poncetech.com.br'
MY_ADDRESS = 'editoraponce@outlook.com'
emailPonce = 'editora@poncetech.com.br'
password = '@rus312519PONCE'
PASSWORD = 'k3@UqUWWZ96u'
s = smtplib.SMTP(host='smtp.office365.com', port=587)
s.starttls()
s.login(MY_ADDRESS, PASSWORD)

server = Flask(__name__)
# app.config.from_object('config')
banco = SQLAlchemy()
# migrate = Migrate(server, banco)
# banco.init_app(server)
api = Api(server)
cors = CORS(server)
jwt = JWTManager(server)
# manager = Manager(server)
# manager.add_command('db',MigrateCommand)


# lm = LoginManager()
# lm.init_app(server)


# flask_app = Flask('app_name', config.APP_NAME)
# flask_app.secret_key = 'redefinir secret key'


# from .utils.blueprints import declare_api_routes
# declare_api_routes(app=flask_app)


# from app.models import tables, forms
# from app.controllers import services

from app.models import *
from app.services import *
from app.config import *

