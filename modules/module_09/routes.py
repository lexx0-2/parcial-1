from flask import Blueprint, render_template

bp = Blueprint("module_09", __name__, url_prefix="/modulo/09")

@bp.route("/")
def index():
    return render_template("advanced_module.html", number=9, title="Integración irracional", formula="\\sqrt[n]{x^m}=x^{m/n}", theory="Reescribe radicales como potencias fraccionarias o usa sustituciones como t=√x.", explanation="Escribe la función y los límites para calcular una integral definida, obtener su primitiva y visualizar su gráfica.", default_expr="1/sqrt(x)", examples=["\\(\\int\\frac1{\\sqrt{x}}dx=2\\sqrt{x}+C\\).","\\(\\int\\frac{x}{\\sqrt{x^2+1}}dx=\\sqrt{x^2+1}+C\\)."], extra="")
