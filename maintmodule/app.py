import os
import io 
import logging
from flask import Flask, request, render_template, render_template_string, jsonify

# log level mutes every request going to stdout
#log = logging.getLogger('werkzeug')
#log.setLevel(logging.ERROR)
app = Flask(__name__)
log = app.logger

# have this path specifically show json response
@app.route('/json')
def show_json():
    return jsonify(type='Exception',status=503,response=os.getenv("MAINTENANCE_MESSAGE")), 503, {'StatusHeader': 'Status: maintenance window'}

# catch-all
@app.route('/', defaults={'path':''})
@app.route('/<path:path>')
def show_default(path):
    return render_template_string(maint_file_as_string, maintenance_message=MAINTENANCE_MESSAGE), 503

print(f"__name__ is {__name__}")

# read in maintenance template
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
maint_file=os.path.join(ROOT_DIR,"maintenance.html")
maint_file_exists=os.path.exists(maint_file)
print("ROOT_DIR = {}, maintenance.html={}, exists? {}".format(ROOT_DIR,maint_file,maint_file_exists))
with open(maint_file,'r') as file:
  maint_file_as_string = file.read()
print(maint_file_as_string)

# get maintenance message from env var
MAINTENANCE_MESSAGE = os.getenv("MAINTENANCE_MESSAGE","This is the fallback maintenance message")
print("MAINTENANCE_MESSAGE = {}".format(MAINTENANCE_MESSAGE))

# called as Flask app
if __name__ == '__main__' or __name__ == "main":
  print("called as Flask app")
  port = int(os.getenv("PORT", 8080))
  print("Starting web server on port {}".format(port))
  app.run(host='0.0.0.0', port=port, debug=True)
# called as WSGI gunicorn app
else:
  print(f"called as WSGI gunicorn app {__name__}")

