from __future__ import division, unicode_literals
import flask
import socket
import json
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


@app.route('/get_mturk_data')
def handle_get_mturk_data():
	info_sent_from_button = request.json # conver the string to object
	button_id = info_sent_from_button.get('workerId')
	content = {
		'btn_1': 'You click button 1',
		'btn_2': 'You click button 2',
	}
	return_data = {
		'content': content[button_id]
	}
	return json.dumps(return_data) # Convert the data to string and send it back to UI. 


if __name__ == '__main__':
	if server:
		flask_helpers.main(app, port=PORT, host='127.0.0.1', debug=DEBUG, use_evalex=False)
	else:
		app.run(port=PORT, host='127.0.0.1', debug=DEBUG)
