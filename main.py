from flask import Flask, render_template, render_template_string, jsonify
import os


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

def show_html(request):
    return render_template_string(maint_file_as_string, maintenance_message=MAINTENANCE_MESSAGE), 503

def show_json(request):
    return jsonify(type='Exception',status=503,response=os.getenv("MAINTENANCE_MESSAGE")), 200, {'StatusHeader': 'Status: maintenance window'}

