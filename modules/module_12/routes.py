from flask import Blueprint, render_template

bp = Blueprint("module_12", __name__, url_prefix="/modulo/12")

@bp.route("/")
def index():
    return render_template(
        "advanced_module.html",
        number=12,
        title="Sustitución universal",
        formula=r"t=\tan(x/2),\quad\sin x=\frac{2t}{1+t^2},\quad\cos x=\frac{1-t^2}{1+t^2}",
        theory="La sustitución de ángulo mitad transforma expresiones racionales de seno y coseno en fracciones racionales de t.",
        explanation="Observa la representación y sigue los pasos del método antes de resolver el ejercicio.",
        default_expr="1/(1+cos(x))",
        examples=[r"""\(\int\frac{dx}{1+\cos x}\). <b>1.</b> Define \(t=\tan(x/2)\). <b>2.</b> Usa \(1+\cos x=\frac{2}{1+t^2}\) y \(dx=\frac{2dt}{1+t^2}\). <b>3.</b> La integral se reduce a \(\int dt\). <b>4.</b> Resultado: \(\tan(x/2)+C\).""",r"""Para \(\int\frac{dx}{1+\sin x}\), <b>1.</b> sustituye seno y diferencial por expresiones en t. <b>2.</b> Simplifica la fracción racional resultante. <b>3.</b> Integra en t y finalmente reemplaza \(t=\tan(x/2)\)."""],
        extra=""
    )
