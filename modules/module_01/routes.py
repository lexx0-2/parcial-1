from flask import Blueprint, render_template

bp = Blueprint("module_01", __name__, url_prefix="/modulo/01")

@bp.route("/")
def index():
    return render_template("module_01.html")
