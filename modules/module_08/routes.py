from flask import Blueprint, render_template

bp = Blueprint("module_08", __name__, url_prefix="/modulo/08")

@bp.route("/")
def index():
    return render_template("advanced_module.html", number=8, title="Integración racional", formula="\\frac{P(x)}{Q(x)}=S(x)+\\sum_i\\frac{A_i}{(x-r_i)^{m_i}}", theory="Factoriza Q(x); si el grado de P es mayor o igual, realiza primero división polinómica.", explanation="Escribe la función y los límites para calcular una integral definida, obtener su primitiva y visualizar su gráfica.", default_expr="1/(x^2-1)", examples=["\\(\\int\\frac{1}{x^2-1}dx=\\frac12\\ln|\\frac{x-1}{x+1}|+C\\).","\\(\\int\\frac{2x+3}{x^2+3x+2}dx=\\ln|x^2+3x+2|+C\\)."], extra="")
