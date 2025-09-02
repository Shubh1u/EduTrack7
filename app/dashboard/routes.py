from flask import Blueprint, render_template, session
from app.utils import login_required
from app.models import User, Attendance, Project, Certificate

dashboard_bp = Blueprint('dashboard', __name__, template_folder='../templates')

@dashboard_bp.route('/dashboard')
@login_required
def dashboard():
    username = session.get('username', 'User')
    user = User.query.get(session['user_id'])
    cgpa = user.cgpa or 0
    attendance_pct = calc_attendance_percent(user.id)
    projects_count = Project.query.filter_by(user_id=user.id).count()
    certs_count = Certificate.query.filter_by(user_id=user.id).count()
    return render_template(
        'dashboard.html',
        username=username,
        cgpa=cgpa,
        attendance_pct=attendance_pct,
        projects_count=projects_count,
        certs_count=certs_count
    )

def calc_attendance_percent(user_id):
    total = Attendance.query.filter_by(user_id=user_id).count()
    if total == 0:
        return 0
    present = Attendance.query.filter_by(user_id=user_id, status='Present').count()
    return round((present / total) * 100)
