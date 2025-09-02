from flask import Blueprint, render_template
from app.utils import login_required

practice_bp = Blueprint('practice', __name__, template_folder='../templates')

@practice_bp.route('/practice')
@login_required
def practice():
    return render_template('practice.html')
