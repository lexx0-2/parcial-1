from flask import Blueprint, render_template

bp = Blueprint("module_07", __name__, url_prefix="/modulo/07")

@bp.route("/")
def index():
    return render_template(
        "advanced_module.html",
        number=7,
        title="Integración por partes",
        formula=r"\int u\,dv=uv-\int v\,du",
        theory="Se utiliza cuando el integrando es un producto y derivar una parte simplifica la expresión. El criterio LIATE orienta la elección de u.",
        explanation="Observa la representación y sigue los pasos del método antes de resolver el ejercicio.",
        default_expr="x*exp(x)",
        examples=[r"""\(\int xe^x dx\). <b>1.</b> Elige \(u=x\), \(dv=e^x dx\). <b>2.</b> Entonces \(du=dx\), \(v=e^x\). <b>3.</b> Aplica partes: \(xe^x-\int e^x dx\). <b>4.</b> Integra: \(xe^x-e^x+C\).""",r"""\(\int x\cos x\,dx\). <b>1.</b> Elige \(u=x\), \(dv=\cos x\,dx\). <b>2.</b> \(du=dx\), \(v=\sin x\). <b>3.</b> Sustituye: \(x\sin x-\int\sin x\,dx\). <b>4.</b> Resultado: \(x\sin x+\cos x+C\)."""],
        extra=""
    )
