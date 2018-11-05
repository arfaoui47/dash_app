#!/usr/bin/env bash

cd ~/dash_app
venv/bin/gunicorn --workers 4 --bind 0.0.0.0:4041 web_app:server
lt --port 4041
