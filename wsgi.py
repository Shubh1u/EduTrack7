from app import create_app, socketio, db

app = create_app()

# ✅ Create tables at runtime
with app.app_context():
    db.create_all()
    print("✅ Tables created at runtime")

if __name__ == "__main__":
    socketio.run(app)
