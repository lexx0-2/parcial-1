from flask import Blueprint, render_template

bp = Blueprint("module_09", __name__, url_prefix="/modulo/09")

@bp.route("/")
def index():
    return render_template("placeholder.html", module_number=9)
