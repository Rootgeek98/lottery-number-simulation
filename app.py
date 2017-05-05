import os
from OpenSSL import SSL

from app import create_app
from flask.ext.script import Manager, Shell

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
# TODO: solve HTTPS connection with Manager
manager = Manager(app)

def make_shell_context():
     return dict(app=app)

manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
    # enable safer HTTPS connection
    #app.run(ssl_context='adhoc')
    #app.run(host='0.0.0.0', port=8080, debug=True)
    manager.run()
