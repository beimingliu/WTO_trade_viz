from flask import Flask, request, render_template
import os

#################################################################
#
#         APP
#
#################################################################

"""
Purpose: this is a JSON Catcher app
1. will receive POST requests with JSON strings as the payload
2. will log all requests
3. and if valid json strings, will extract name and age information
to be stored.

MAIN paths:

POST http://json_server/
GET http://json_server/test  - will return a note if its running
GET http://json_server/shutdown - will shut down server remotely,
    even if running
    on either Flask or Gunicorn
"""

app = Flask(__name__)

#################################################################
#
#         WEB HANDLERS
#
#################################################################


@app.route('/')
def HomeHandler():
    """
    """
    return render_template('index.html')


@app.route('/test')
def test_connection():
    """
    Used for testing if the server is up, returns simple message
    """
    return "Server running! Prefix: %s \n" % app.config.get('prefix')


@app.route('/shutdown')
def shutdown():
    """
    Used for shutting down the server remotely. This calls the underlying
    platform and forces a shutdown.
    # subprocess.call("pkill gunicorn", shell = True)
    """

    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        # if running on gunicorn
        os._exit(4)
    else:
        # if running python server.py (using werkzeug)
        func()
    return "Process shutting down..."
