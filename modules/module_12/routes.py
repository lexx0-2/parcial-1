from flask import Blueprint, render_template

bp = Blueprint("module_12", __name__, url_prefix="/modulo/12")

@bp.route("/")
def index():
    return render_template("placeholder.html", module_number=12)
