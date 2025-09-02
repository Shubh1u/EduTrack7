import os
from datetime import datetime
from werkzeug.utils import secure_filename
from flask import Blueprint, render_template, request, redirect, url_for, session, flash, current_app
from app.utils import login_required
from app.models import db, Certificate

certificates_bp = Blueprint('certificates', __name__, template_folder='../templates')

@certificates_bp.route('/certificates', methods=['GET', 'POST'])
@login_required
def certificates():
    user_id = session['user_id']
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        issued_date = request.form.get('issued_date')
        file = request.files.get('file')
        file_path = None

        if file and allowed_image(file.filename):
            filename = secure_filename(file.filename)
            os.makedirs(current_app.config['UPLOAD_FOLDER'], exist_ok=True)
            save_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            file.save(save_path)
            file_path = save_path

        cert = Certificate(
            name=name or "Certificate",
            file_path=file_path,
            issued_date=datetime.strptime(issued_date, "%Y-%m-%d").date() if issued_date else None,
            user_id=user_id
        )
        db.session.add(cert)
        db.session.commit()
        flash("Certificate added.", "success")
        return redirect(url_for('certificates.certificates'))

    items = Certificate.query.filter_by(user_id=user_id).order_by(Certificate.id.desc()).all()
    return render_template('certificates.html', items=items)

def allowed_image(filename):
    if '.' not in filename:
        return False
    ext = filename.rsplit('.', 1)[1].lower()
    from flask import current_app
    return ext in current_app.config.get('ALLOWED_IMAGE_EXTENSIONS', {})
