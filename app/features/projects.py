from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.utils import login_required
from app.models import db, Project

projects_bp = Blueprint('projects', __name__, template_folder='../templates')

@projects_bp.route('/projects', methods=['GET', 'POST'])
@login_required
def projects():
    user_id = session['user_id']
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()
        repo_link = request.form.get('repo_link', '').strip()
        if not title:
            flash("Title is required.", "warning")
        else:
            db.session.add(Project(title=title, description=description, repo_link=repo_link, user_id=user_id))
            db.session.commit()
            flash("Project added.", "success")
        return redirect(url_for('projects.projects'))
    items = Project.query.filter_by(user_id=user_id).order_by(Project.id.desc()).all()
    return render_template('projects.html', items=items)
