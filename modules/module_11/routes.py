from flask import Blueprint, render_template

bp = Blueprint("module_11", __name__, url_prefix="/modulo/11")

@bp.route("/")
def index():
    return render_template("advanced_module.html", number=11, title="Sustitución trigonométrica", formula="\\sqrt{a^2-x^2}:x=a\\sin\\theta;\\quad\\sqrt{a^2+x^2}:x=a\\tan\\theta", theory="Selecciona seno, tangente o secante según el radical y simplifica con identidades.", explanation="Escribe la función y los límites para calcular una integral definida, obtener su primitiva y visualizar su gráfica.", default_expr="1/sqrt(9-x^2)", examples=["\\(\\int\\frac{dx}{\\sqrt{9-x^2}}=\\arcsin(x/3)+C\\).","\\(\\int\\frac{dx}{x^2+4}=\\frac12\\arctan(x/2)+C\\)."], extra="")
