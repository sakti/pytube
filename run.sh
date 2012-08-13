#!/bin/sh
gunicorn_django -b 0.0.0.0:9090 --workers=9
