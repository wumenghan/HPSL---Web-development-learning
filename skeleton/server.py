from __future__ import division, unicode_literals
import sqlite3
import flask
import socket
from flask import Flask, render_template, request

app = Flask(__name__, static_folder='client/build/static', template_folder='client/build')

PORT = YOUR_PORT_ON_HCI # put your port here
server = True if socket.gethostname() == 'hci.ecn.purdue.edu' else False
DEBUG = False

if server:
	import flask_hci_server, flask_helpers
	flask_hci_server.adapt_for_crowd_server(app)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')


if __name__ == '__main__':
	if server:
		flask_helpers.main(app, port=PORT, host='127.0.0.1', debug=DEBUG, use_evalex=False)
	else:
		app.run(port=PORT, host='127.0.0.1', debug=DEBUG)
