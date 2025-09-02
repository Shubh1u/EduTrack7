from flask import Blueprint

# Create the blueprint object
auth_bp = Blueprint('auth', __name__, template_folder='../templates')

# Import routes so they get registered with the blueprint
from app.auth import routes
