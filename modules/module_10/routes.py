from flask import Blueprint, render_template

bp = Blueprint("module_10", __name__, url_prefix="/modulo/10")

@bp.route("/")
def index():
    return render_template(
        "advanced_module.html",
        number=10,
        title="Integración trigonométrica",
        formula=r"\\sin^2x+\\cos^2x=1,\\quad1+\\tan^2x=\\sec^2x",
        theory="Se usan identidades trigonométricas para transformar potencias y productos de seno, coseno, tangente y secante antes de integrar.",
        explanation="Observa la representación y sigue los pasos del método antes de resolver el ejercicio.",
        default_expr="sin(x)^2",
        examples=[r"""\\(\\int\\sin^2x\\,dx\\). **1.** Usa reducción de potencia: \\(\\sin^2x=\\frac{1-\\cos(2x)}2\\). **2.** Separa: \\(\\frac12\\int1\\,dx-\\frac12\\int\\cos(2x)\\,dx\\). **3.** Integra: \\(\\frac{x}{2}-\\frac{\\sin(2x)}4+C\\).""",r"""\\(\\int\\sin x\\cos x\\,dx\\). **1.** Toma \\(u=\\sin x\\). **2.** Entonces \\(du=\\cos x\\,dx\\). **3.** Integra \\(\\int u\\,du=\\frac{u^2}{2}+C\\). **4.** Resultado: \\(\\frac{\\sin^2x}{2}+C\\)."""],
        extra=""
    )
