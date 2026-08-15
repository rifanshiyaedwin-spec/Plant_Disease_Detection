import sys
import os

# Add root directory to path for serverless imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app
import serverless_wsgi

def handler(event, context):
    return serverless_wsgi.handle_request(app, event, context)
