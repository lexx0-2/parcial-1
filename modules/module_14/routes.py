from flask import Blueprint, render_template

bp = Blueprint("module_14", __name__, url_prefix="/modulo/14")

@bp.route("/")
def index():
    return render_template(
        "advanced_module.html",
        number=14,
        title="Volúmenes de sólidos de revolución",
        formula=r"V=\pi\int_a^b(R^2-r^2)dx;\quad V=2\pi\int_a^bxf(x)dx",
        theory="Al girar una región alrededor de un eje se forma un sólido. Se puede calcular con discos, arandelas o capas cilíndricas, según la orientación de los cortes.",
        explanation="Observa la representación y sigue los pasos del método antes de resolver el ejercicio.",
        default_expr="x",
        examples=[r"""Girar \(y=x\) de 0 a 2 alrededor del eje x. <b>1.</b> Método de discos, radio \(R=x\). <b>2.</b> Área: \(A(x)=\pi x^2\). <b>3.</b> Volumen: \(V=\pi\int_0^2x^2dx=8\pi/3\).""",r"""Girar \(y=x\) de 0 a 2 alrededor del eje y. <b>1.</b> Método de capas, radio x y altura x. <b>2.</b> Elemento: \(dV=2\pi x(x)dx\). <b>3.</b> Volumen: \(V=2\pi\int_0^2x^2dx=16\pi/3\)."""],
        extra="""<div class="controls"><label>Método<select id="method"><option value="disk">Discos</option><option value="washer">Arandelas</option><option value="shell">Capas cilíndricas (eje y)</option></select></label><label>Radio interior g(x)<input id="inner" value="0"></label><button onclick="calculateVolume()">Calcular volumen</button></div>"""
    )
