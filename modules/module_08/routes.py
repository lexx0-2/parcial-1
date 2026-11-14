from flask import Blueprint, render_template

bp = Blueprint("module_08", __name__, url_prefix="/modulo/08")

@bp.route("/")
def index():
    return render_template(
        "advanced_module.html",
        number=8,
        title="Integración racional",
        formula=r"\\frac{P(x)}{Q(x)}=S(x)+\\sum_i\\frac{A_i}{(x-r_i)^{m_i}}",
        theory="Se factoriza el denominador y se descompone la fracción en términos más simples. Si el grado del numerador no es menor, primero se realiza división polinómica.",
        explanation="Observa la representación y sigue los pasos del método antes de resolver el ejercicio.",
        default_expr="1/(x^2-1)",
        examples=[r"""\\(\\int\\frac{1}{x^2-1}dx\\). **1.** Factoriza: \\(x^2-1=(x-1)(x+1)\\). **2.** Descompón: \\(\\frac1{x^2-1}=\\frac{1/2}{x-1}-\\frac{1/2}{x+1}\\). **3.** Integra cada término: \\(\\frac12\\ln|x-1|-\\frac12\\ln|x+1|+C\\).""",r"""\\(\\int\\frac{2x+3}{x^2+3x+2}dx\\). **1.** Factoriza el denominador: \\((x+1)(x+2)\\). **2.** Descompón: \\(\\frac1{x+1}+\\frac1{x+2}\\). **3.** Integra: \\(\\ln|x+1|+\\ln|x+2|+C\\)."""],
        extra=""
    )
