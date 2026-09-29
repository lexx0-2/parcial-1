from flask import Blueprint, render_template

bp = Blueprint("module_04", __name__, url_prefix="/modulo/04")

@bp.route("/")
def index():
    return render_template("module_04.html")
