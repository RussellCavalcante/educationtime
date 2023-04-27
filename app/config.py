# import os.path
# basedir = os.path.abspath(os.path.dirname(__file__))

from datetime import timedelta
from flask import Flask, jsonify
from flask_restful import Resource, Api 
from flask_jwt_extended import JWTManager
# from blacklist import BLACKLIST
from flask_cors import CORS
from app.services.user import *
from werkzeug.utils import secure_filename
# from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
from app import server, jwt, banco
from app.blueprints import avaliable_route



server.register_blueprint(avaliable_route)

server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
server.config['JWT_SECRET_KEY'] = 'DontTellAnyone'
server.config['JWT_BLACKLIST_ENABLED'] = True
server.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=999)
server.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg', 'csv'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
# @server.before_first_request

@jwt.token_in_blocklist_loader
def verifica_blocklist(self, token):
    return token['jti'] in BLACKLIST

@jwt.revoked_token_loader
def token_de_acesso_invalidado(jwt_header, jwt_payload):
    return jsonify({'message': 'você foi deslogado'}), 401
