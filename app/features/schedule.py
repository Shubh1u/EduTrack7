from flask import Blueprint, render_template
from app.utils import login_required

schedule_bp = Blueprint('schedule', __name__, template_folder='../templates')

@schedule_bp.route('/schedule')
@login_required
def schedule():
    return render_template('schedule.html')
