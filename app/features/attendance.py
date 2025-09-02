from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.utils import login_required
from app.models import db, Attendance
from datetime import date

attendance_bp = Blueprint('attendance', __name__, template_folder='../templates')

@attendance_bp.route('/attendance', methods=['GET', 'POST'])
@login_required
def attendance():
    user_id = session['user_id']
    if request.method == 'POST':
        status = request.form.get('status')
        if status not in ('Present', 'Absent'):
            flash("Invalid status.", "warning")
        else:
            db.session.add(Attendance(user_id=user_id, status=status, date=date.today()))
            db.session.commit()
            flash("Attendance marked.", "success")
        return redirect(url_for('attendance.attendance'))
    records = Attendance.query.filter_by(user_id=user_id).order_by(Attendance.date.desc()).all()
    return render_template('attendance.html', records=records)
