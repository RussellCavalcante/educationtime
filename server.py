import os
from app import server

if __name__ == '__main__':
    # banco.init_app(server)
    server.run(host = '0.0.0.0', debug=True)
# server.run(debug=False)
