from flask import Blueprint, render_template

bp = Blueprint("module_07", __name__, url_prefix="/modulo/07")

@bp.route("/")
def index():
    return render_template("advanced_module.html", number=7, title="Integración por partes", formula="\\int u\\,dv=uv-\\int v\\,du", theory="Escoge u (criterio LIATE), deriva para obtener du e integra dv para obtener v.", explanation="Escribe la función y los límites para calcular una integral definida, obtener su primitiva y visualizar su gráfica.", default_expr="x*exp(x)", examples=["\\(\\int xe^x dx\\): u=x, dv=e^x dx; du=dx, v=e^x. Resultado: xe^x−e^x+C.","\\(\\int x\\cos x dx\\): u=x, dv=cos x dx. Resultado: x sen x+cos x+C."], extra="")
