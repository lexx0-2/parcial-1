from flask import Blueprint, render_template

bp = Blueprint("module_10", __name__, url_prefix="/modulo/10")

@bp.route("/")
def index():
    return render_template("advanced_module.html", number=10, title="Integración trigonométrica", formula="\\sin^2x+\\cos^2x=1,\\quad1+\\tan^2x=\\sec^2x", theory="Usa identidades pitagóricas, reducción de potencias y relaciones trigonométricas.", explanation="Escribe la función y los límites para calcular una integral definida, obtener su primitiva y visualizar su gráfica.", default_expr="sin(x)^2", examples=["\\(\\int\\sin^2x dx=\\frac{x}{2}-\\frac{\\sin2x}{4}+C\\).","\\(\\int\\sin x\\cos x dx=\\frac{\\sin^2x}{2}+C\\)."], extra="")
