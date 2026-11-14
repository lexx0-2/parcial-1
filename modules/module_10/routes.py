from flask import Blueprint, render_template

bp = Blueprint("module_10", __name__, url_prefix="/modulo/10")

@bp.route("/")
def index():
    return render_template(
        "advanced_module.html",
        number=10,
        title="Integración trigonométrica",
        formula=r"\sin^2x+\cos^2x=1,\quad1+\tan^2x=\sec^2x",
        theory="Se usan identidades trigonométricas para transformar potencias y productos de seno, coseno, tangente y secante antes de integrar.",
        explanation="Observa la representación y sigue los pasos del método antes de resolver el ejercicio.",
        default_expr="sin(x)^2",
        examples=[r"""\(\int\sin^2x\,dx\). <b>1.</b> Usa reducción de potencia: \(\sin^2x=\frac{1-\cos(2x)}2\). <b>2.</b> Separa: \(\frac12\int1\,dx-\frac12\int\cos(2x)\,dx\). <b>3.</b> Integra: \(\frac{x}{2}-\frac{\sin(2x)}4+C\).""",r"""\(\int\sin x\cos x\,dx\). <b>1.</b> Toma \(u=\sin x\). <b>2.</b> Entonces \(du=\cos x\,dx\). <b>3.</b> Integra \(\int u\,du=\frac{u^2}{2}+C\). <b>4.</b> Resultado: \(\frac{\sin^2x}{2}+C\)."""],
        extra=""
    )
