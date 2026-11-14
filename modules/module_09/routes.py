from flask import Blueprint, render_template

bp = Blueprint("module_09", __name__, url_prefix="/modulo/09")

@bp.route("/")
def index():
    return render_template(
        "advanced_module.html",
        number=9,
        title="Integración irracional",
        formula=r"\\sqrt[n]{x^m}=x^{m/n}",
        theory="Los radicales se pueden reescribir como potencias fraccionarias. Cuando conviene, una sustitución convierte la expresión en una integral algebraica más sencilla.",
        explanation="Observa la representación y sigue los pasos del método antes de resolver el ejercicio.",
        default_expr="1/sqrt(x)",
        examples=[r"""\\(\\int\\frac1{\\sqrt{x}}dx\\). **1.** Reescribe: \\(x^{-1/2}\\). **2.** Aplica la regla de potencia: \\(\\frac{x^{1/2}}{1/2}+C\\). **3.** Simplifica: \\(2\\sqrt{x}+C\\).""",r"""\\(\\int\\frac{x}{\\sqrt{x^2+1}}dx\\). **1.** Toma \\(u=x^2+1\\). **2.** Entonces \\(du=2x\\,dx\\). **3.** La integral queda \\(\\frac12\\int u^{-1/2}du\\). **4.** Regresa a x: \\(\\sqrt{x^2+1}+C\\)."""],
        extra=""
    )
