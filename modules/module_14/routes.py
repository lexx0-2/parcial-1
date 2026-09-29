from flask import Blueprint, render_template

bp = Blueprint("module_14", __name__, url_prefix="/modulo/14")

@bp.route("/")
def index():
    return render_template("placeholder.html", module_number=14)
