from flask import Blueprint, render_template

bp = Blueprint("module_13", __name__, url_prefix="/modulo/13")

@bp.route("/")
def index():
    return render_template("advanced_module.html", number=13, title="Volúmenes con sección conocida", formula="V=\\int_a^b A(x)\\,dx", theory="Integra el área transversal. Se incluyen secciones cuadradas, semicirculares y triangulares equiláteras, tomando f(x) como lado o diámetro.", explanation="Escribe la función y los límites para calcular una integral definida, obtener su primitiva y visualizar su gráfica.", default_expr="x", examples=["Sección cuadrada de lado x, de 0 a 2: \\(V=\\int_0^2x^2dx=8/3\\).","Semicírculos de diámetro 2, de 0 a 3: \\(V=\\int_0^3\\pi(2)^2/8\\,dx=3\\pi/2\\)."], extra="<div class=\"controls\"><label>Sección transversal<select id=\"shape\"><option value=\"square\">Cuadrado (lado f(x))</option><option value=\"semicircle\">Semicírculo (diámetro f(x))</option><option value=\"triangle\">Triángulo equilátero (lado f(x))</option></select></label><button onclick=\"calculateVolume()\">Calcular volumen</button></div>")
