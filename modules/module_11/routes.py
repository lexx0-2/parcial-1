from flask import Blueprint, render_template

bp = Blueprint("module_11", __name__, url_prefix="/modulo/11")

@bp.route("/")
def index():
    return render_template(
        "advanced_module.html",
        number=11,
        title="Sustitución trigonométrica",
        formula=r"\sqrt{a^2-x^2}:x=a\sin\theta;\quad\sqrt{a^2+x^2}:x=a\tan\theta",
        theory="Se cambia x por una función trigonométrica para eliminar radicales que contienen sumas o diferencias de cuadrados. La elección depende de la forma del radical.",
        explanation="Observa la representación y sigue los pasos del método antes de resolver el ejercicio.",
        default_expr="1/sqrt(9-x^2)",
        examples=[r"""\(\int\frac{dx}{\sqrt{9-x^2}}\). <b>1.</b> Usa \(x=3\sin\theta\). <b>2.</b> Entonces \(dx=3\cos\theta\,d\theta\) y \(\sqrt{9-x^2}=3\cos\theta\). <b>3.</b> Se simplifica a \(\int d\theta=\theta+C\). <b>4.</b> Regresa: \(\arcsin(x/3)+C\).""",r"""\(\int\frac{dx}{\sqrt{x^2+4}}\). <b>1.</b> Usa \(x=2\tan\theta\). <b>2.</b> El radical se transforma con \(1+\tan^2\theta=\sec^2\theta\). <b>3.</b> Integra en θ: \\(\\ln|\\sec\\theta+\\tan\\theta|+C\\). Regresa a x usando \\(\\tan\\theta=x/2\\)."""],
        extra=""
    )
