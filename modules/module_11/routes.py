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
        examples=[r"""\(\int\frac{dx}{\sqrt{9-x^2}}\). **1.** Usa \(x=3\sin\theta\). **2.** Entonces \(dx=3\cos\theta\,d\theta\) y \(\sqrt{9-x^2}=3\cos\theta\). **3.** Se simplifica a \(\int d\theta=\theta+C\). **4.** Regresa: \(\arcsin(x/3)+C\).""",r"""\(\int\frac{dx}{\sqrt{x^2+4}}\). **1.** Usa \(x=2\tan\theta\). **2.** El radical se transforma con \(1+\tan^2\theta=\sec^2\theta\). **3.** Integra la expresión en θ y regresa a x con el triángulo de referencia."""],
        extra=""
    )
