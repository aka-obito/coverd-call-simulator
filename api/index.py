from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

# Import your app from app.py
from app import app

app.wsgi_app = ProxyFix(app.wsgi_app)

# Lambda handler (Vercel serverless function)
def handler(event, context):
    return app(event, context)
