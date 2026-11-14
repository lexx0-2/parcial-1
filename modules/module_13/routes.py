from flask import Blueprint, render_template

bp = Blueprint("module_13", __name__, url_prefix="/modulo/13")

@bp.route("/")
def index():
    return render_template(
        "advanced_module.html",
        number=13,
        title="Volúmenes con sección conocida",
        formula=r"V=\int_a^b A(x)\,dx",
        theory="El sólido se construye mediante secciones transversales. En cada posición x se calcula el área A(x) y luego se integra a lo largo del intervalo.",
        explanation="Observa la representación y sigue los pasos del método antes de resolver el ejercicio.",
        default_expr="x",
        examples=[r"""Sección cuadrada de lado \(s(x)=x\), entre 0 y 2. **1.** Área: \(A(x)=x^2\). **2.** Volumen: \(V=\int_0^2x^2dx\). **3.** Evalúa: \([x^3/3]_0^2=8/3\) unidades cúbicas.""",r"""Semicírculos de diámetro constante 2 entre 0 y 3. **1.** Área: \(A=\pi d^2/8=\pi/2\). **2.** Volumen: \(V=\int_0^3\pi/2\,dx\). **3.** Resultado: \(3\pi/2\) unidades cúbicas."""],
        extra="""<div class="controls"><label>Sección transversal<select id="shape"><option value="square">Cuadrado (lado f(x))</option><option value="semicircle">Semicírculo (diámetro f(x))</option><option value="triangle">Triángulo equilátero (lado f(x))</option></select></label><button onclick="calculateVolume()">Calcular volumen</button></div>"""
    )
