# This file makes `features` a package and can also be used to import all feature blueprints

from app.features.attendance import attendance_bp
from app.features.certificates import certificates_bp
from app.features.cgpa import cgpa_bp
from app.features.chat import chat_bp
from app.features.practice import practice_bp
from app.features.profile import profile_bp
from app.features.projects import projects_bp
from app.features.schedule import schedule_bp

# A list of all feature blueprints for easy registration in app/__init__.py
feature_blueprints = [
    attendance_bp,
    certificates_bp,
    cgpa_bp,
    chat_bp,
    practice_bp,
    profile_bp,
    projects_bp,
    schedule_bp
]
