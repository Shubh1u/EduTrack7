
from flask import Flask
from flask_migrate import Migrate
from flask_socketio import SocketIO
from app.config import DevelopmentConfig
from app.models import db

socketio = SocketIO(cors_allowed_origins="*",async_mode="threading")  # eventlet/gevent compatible

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    # Initialize extensions
    db.init_app(app)
    Migrate(app, db)
    socketio.init_app(app)
     with app.app_context():
        db.create_all()
        print("✅ Tables created at runtime")

    return app

    

    # Blueprints
    from app.auth.routes import auth_bp
    from app.dashboard.routes import dashboard_bp
    from app.features.chat import chat_bp
    from app.features.attendance import attendance_bp
    from app.features.practice import practice_bp
    from app.features.projects import projects_bp
    from app.features.certificates import certificates_bp
    from app.features.profile import profile_bp
    from app.features.cgpa import cgpa_bp
    from app.features.schedule import schedule_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(chat_bp)
    app.register_blueprint(attendance_bp)
    app.register_blueprint(practice_bp)
    app.register_blueprint(projects_bp)
    app.register_blueprint(certificates_bp)
    app.register_blueprint(profile_bp)
    app.register_blueprint(cgpa_bp)
    app.register_blueprint(schedule_bp)

    return app
