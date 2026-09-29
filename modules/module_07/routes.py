from flask import Blueprint, render_template

bp = Blueprint("module_07", __name__, url_prefix="/modulo/07")

@bp.route("/")
def index():
    return render_template("placeholder.html", module_number=7)
