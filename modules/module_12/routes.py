from flask import Blueprint, render_template

bp = Blueprint("module_12", __name__, url_prefix="/modulo/12")

@bp.route("/")
def index():
    return render_template("advanced_module.html", number=12, title="Sustitución universal", formula="t=\\tan(x/2),\\quad\\sin x=\\frac{2t}{1+t^2},\\quad\\cos x=\\frac{1-t^2}{1+t^2}", theory="Transforma integrales racionales de seno y coseno en integrales racionales de t.", explanation="Escribe la función y los límites para calcular una integral definida, obtener su primitiva y visualizar su gráfica.", default_expr="1/(1+cos(x))", examples=["Para \\(\\int dx/(1+\\sin x)\\), usa t=tan(x/2), sen x=2t/(1+t²), dx=2dt/(1+t²).","\\(\\int dx/(1+\\cos x)=\\tan(x/2)+C\\)."], extra="")
