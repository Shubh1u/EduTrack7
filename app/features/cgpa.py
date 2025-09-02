from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.utils import login_required
from app.models import db, User

cgpa_bp = Blueprint('cgpa', __name__, template_folder='../templates')

@cgpa_bp.route('/cgpa', methods=['GET', 'POST'])
@login_required
def cgpa():
    user = User.query.get(session['user_id'])
    if request.method == 'POST':
        try:
            value = float(request.form.get('cgpa', user.cgpa or 0))
            if value < 0 or value > 10:
                raise ValueError()
            user.cgpa = value
            db.session.commit()
            flash("CGPA updated.", "success")
        except Exception:
            flash("Enter a valid CGPA between 0 and 10.", "warning")
        return redirect(url_for('cgpa.cgpa'))
    return render_template('cgpa.html', cgpa=user.cgpa or 0.0)
