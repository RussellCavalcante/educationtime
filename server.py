import os
from app import server

if __name__ == '__main__':
    # banco.init_app(server)
    # server.run(host = '0.0.0.0', debug=True)

    # port = int(os.environ.get("PORT", 5000))
    # server.run(host='0.0.0.0', port=port)
    server.run(debug=False)