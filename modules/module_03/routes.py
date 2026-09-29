from flask import Blueprint, render_template

bp = Blueprint("module_03", __name__, url_prefix="/modulo/03")

@bp.route("/")
def index():
    return render_template("module_03.html")
