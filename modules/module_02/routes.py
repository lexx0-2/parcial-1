from flask import Blueprint, render_template

bp = Blueprint("module_02", __name__, url_prefix="/modulo/02")

@bp.route("/")
def index():
    return render_template("module_02.html")
