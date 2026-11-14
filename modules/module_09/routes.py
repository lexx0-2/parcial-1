from flask import Blueprint, render_template

bp = Blueprint("module_09", __name__, url_prefix="/modulo/09")

@bp.route("/")
def index():
    return render_template(
        "advanced_module.html",
        number=9,
        title="Integración irracional",
        formula=r"\sqrt[n]{x^m}=x^{m/n}",
        theory="Los radicales se pueden reescribir como potencias fraccionarias. Cuando conviene, una sustitución convierte la expresión en una integral algebraica más sencilla.",
        explanation="Observa la representación y sigue los pasos del método antes de resolver el ejercicio.",
        default_expr="1/sqrt(x)",
        examples=[r"""\(\int\frac1{\sqrt{x}}dx\). <b>1.</b> Reescribe: \(x^{-1/2}\). <b>2.</b> Aplica la regla de potencia: \(\frac{x^{1/2}}{1/2}+C\). <b>3.</b> Simplifica: \(2\sqrt{x}+C\).""",r"""\(\int\frac{x}{\sqrt{x^2+1}}dx\). <b>1.</b> Toma \(u=x^2+1\). <b>2.</b> Entonces \(du=2x\,dx\). <b>3.</b> La integral queda \(\frac12\int u^{-1/2}du\). <b>4.</b> Regresa a x: \(\sqrt{x^2+1}+C\)."""],
        extra=""
    )
