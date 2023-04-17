#!/bin/bash
#
# Runs Flask app directly, instead of using WYSGI implementation like gunicorn
#
# Used during development lifecycle
#

python3 -m maintmodule.app run --port 8000
