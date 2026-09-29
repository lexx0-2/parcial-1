from flask import Blueprint, render_template
bp=Blueprint("module_05",__name__,url_prefix="/modulo/05")
@bp.route("/")
def index(): return render_template("module_05.html")
