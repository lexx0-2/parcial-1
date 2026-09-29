from flask import Blueprint, render_template

bp = Blueprint("module_06", __name__, url_prefix="/modulo/06")

@bp.route("/")
def index():
    return render_template("module_06.html")
