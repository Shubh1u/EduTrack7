import os
from werkzeug.utils import secure_filename
from flask import Blueprint, render_template, request, redirect, url_for, session, flash, current_app
from app.utils import login_required
from app.models import db, User

profile_bp = Blueprint('profile', __name__, template_folder='../templates')

@profile_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    user = User.query.get(session['user_id'])
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip().lower()
        file = request.files.get('profile_pic')

        if username:
            user.username = username
            session['username'] = username
        if email:
            user.email = email
        if file and allowed_image(file.filename):
            filename = secure_filename(file.filename)
            os.makedirs(current_app.config['UPLOAD_FOLDER'], exist_ok=True)
            save_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            file.save(save_path)
            user.profile_pic = save_path

        db.session.commit()
        flash("Profile updated.", "success")
        return redirect(url_for('profile.profile'))

    return render_template('profile.html', user=user)

def allowed_image(filename):
    if '.' not in filename:
        return False
    ext = filename.rsplit('.', 1)[1].lower()
    from flask import current_app
    return ext in current_app.config.get('ALLOWED_IMAGE_EXTENSIONS', {})
