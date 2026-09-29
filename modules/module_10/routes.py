from flask import Blueprint, render_template

bp = Blueprint("module_10", __name__, url_prefix="/modulo/10")

@bp.route("/")
def index():
    return render_template("placeholder.html", module_number=10)
