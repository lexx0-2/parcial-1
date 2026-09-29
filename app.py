from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

from api import bp as api_bp
app.register_blueprint(api_bp)

# Each module is isolated in its own package/Blueprint.
from modules.module_01.routes import bp as module_01_bp
from modules.module_02.routes import bp as module_02_bp
from modules.module_03.routes import bp as module_03_bp
from modules.module_04.routes import bp as module_04_bp
from modules.module_05.routes import bp as module_05_bp
from modules.module_06.routes import bp as module_06_bp
from modules.module_07.routes import bp as module_07_bp
from modules.module_08.routes import bp as module_08_bp
from modules.module_09.routes import bp as module_09_bp
from modules.module_10.routes import bp as module_10_bp
from modules.module_11.routes import bp as module_11_bp
from modules.module_12.routes import bp as module_12_bp
from modules.module_13.routes import bp as module_13_bp
from modules.module_14.routes import bp as module_14_bp

for bp in [
    module_01_bp, module_02_bp, module_03_bp, module_04_bp,
    module_05_bp, module_06_bp, module_07_bp, module_08_bp,
    module_09_bp, module_10_bp, module_11_bp, module_12_bp,
    module_13_bp, module_14_bp
]:
    app.register_blueprint(bp)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(debug=True)
