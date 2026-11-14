from flask import Blueprint, render_template

bp = Blueprint("module_07", __name__, url_prefix="/modulo/07")

@bp.route("/")
def index():
    return render_template(
        "advanced_module.html",
        number=7,
        title="Integración por partes",
        formula=r"\\int u\\,dv=uv-\\int v\\,du",
        theory="Se utiliza cuando el integrando es un producto y derivar una parte simplifica la expresión. El criterio LIATE orienta la elección de u.",
        explanation="Observa la representación y sigue los pasos del método antes de resolver el ejercicio.",
        default_expr="x*exp(x)",
        examples=[r"""\\(\\int xe^x dx\\). **1.** Elige \\(u=x\\), \\(dv=e^x dx\\). **2.** Entonces \\(du=dx\\), \\(v=e^x\\). **3.** Aplica partes: \\(xe^x-\\int e^x dx\\). **4.** Integra: \\(xe^x-e^x+C\\).""",r"""\\(\\int x\\cos x\\,dx\\). **1.** Elige \\(u=x\\), \\(dv=\\cos x\\,dx\\). **2.** \\(du=dx\\), \\(v=\\sin x\\). **3.** Sustituye: \\(x\\sin x-\\int\\sin x\\,dx\\). **4.** Resultado: \\(x\\sin x+\\cos x+C\\)."""],
        extra=""
    )
