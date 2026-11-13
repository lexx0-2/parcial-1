from flask import Blueprint, render_template

bp = Blueprint("module_14", __name__, url_prefix="/modulo/14")

@bp.route("/")
def index():
    return render_template("advanced_module.html", number=14, title="Volúmenes de sólidos de revolución", formula="V=\\pi\\int_a^b(R^2-r^2)dx;\\quad V=2\\pi\\int_a^bxf(x)dx", theory="Métodos: discos, arandelas o capas cilíndricas alrededor del eje y.", explanation="Escribe la función y los límites para calcular una integral definida, obtener su primitiva y visualizar su gráfica.", default_expr="x", examples=["Girar y=x, de 0 a 2, alrededor del eje x: \\(V=\\pi\\int_0^2x^2dx=8\\pi/3\\).","Girar y=√x, de 0 a 4, alrededor del eje x: \\(V=\\pi\\int_0^4x dx=8\\pi\\)."], extra="<div class=\"controls\"><label>Método<select id=\"method\"><option value=\"disk\">Discos</option><option value=\"washer\">Arandelas</option><option value=\"shell\">Capas cilíndricas (eje y)</option></select></label><label>Radio interior g(x)<input id=\"inner\" value=\"0\"></label><button onclick=\"calculateVolume()\">Calcular volumen</button></div>")
