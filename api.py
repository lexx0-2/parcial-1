from flask import Blueprint, request, jsonify
import re
import sympy as sp

bp = Blueprint("api", __name__, url_prefix="/api")
x = sp.Symbol("x")

LOCAL_DICT = {
    "x": x, "pi": sp.pi, "π": sp.pi, "e": sp.E, "E": sp.E,
    "sen": sp.sin, "sin": sp.sin, "seno": sp.sin,
    "cos": sp.cos, "coseno": sp.cos,
    "tan": sp.tan, "tg": sp.tan, "tangente": sp.tan,
    "cot": sp.cot, "sec": sp.sec, "csc": sp.csc,
    "asin": sp.asin, "arcsin": sp.asin, "acos": sp.acos, "arccos": sp.acos,
    "atan": sp.atan, "arctan": sp.atan,
    "ln": sp.log, "log": sp.log, "log10": lambda z: sp.log(z, 10), "sqrt": sp.sqrt, "raiz": sp.sqrt,
    "abs": sp.Abs, "exp": sp.exp, "sinh": sp.sinh, "cosh": sp.cosh, "tanh": sp.tanh,
}

TRANSFORMATIONS = (
    sp.parsing.sympy_parser.standard_transformations
    + (sp.parsing.sympy_parser.implicit_multiplication_application,)
)

def normalize_expression(expression: str) -> str:
    expression = expression.strip()
    if not expression:
        raise ValueError("La función está vacía.")
    # Símbolos matemáticos frecuentes escritos directamente desde el teclado/copia-pega.
    for old, new in {
        "−":"-", "–":"-", "·":"*", "×":"*", "^":"**", "π":"pi", "÷":"/",
        "²":"**2", "³":"**3", "⁴":"**4", "⁵":"**5", "⁶":"**6",
    }.items():
        expression = expression.replace(old, new)

    # Permite pegar integrales sencillas como ∫(x^2+1)dx. El motor recibe solo el integrando.
    expression = re.sub(r"^\s*∫", "", expression)
    expression = re.sub(r"^\s*\\int", "", expression)
    expression = re.sub(r"d\s*[xX]\s*$", "", expression)

    # Raíz cuadrada Unicode: √x, √(x+1), √x+4. Para expresiones complejas se recomienda sqrt(...).
    expression = re.sub(r"√\s*\(([^()]*)\)", r"sqrt(\1)", expression)
    expression = re.sub(r"√\s*([A-Za-z0-9_.]+)", r"sqrt(\1)", expression)
    for pattern, replacement in [
        (r"\bseno\s*\(", "sin("), (r"\bsen\s*\(", "sin("),
        (r"\bcoseno\s*\(", "cos("), (r"\btangente\s*\(", "tan("),
        (r"\btg\s*\(", "tan("), (r"\braiz\s*\(", "sqrt("),
    ]:
        expression = re.sub(pattern, replacement, expression, flags=re.IGNORECASE)
    return expression

def parse_expression(expression: str):
    return sp.parse_expr(normalize_expression(expression), local_dict=LOCAL_DICT,
                         transformations=TRANSFORMATIONS, evaluate=True)

def finite_float(value):
    n=sp.N(value,16)
    return float(n) if n.is_real else str(n)

@bp.post("/parse")
def parse():
    try:
        expression=request.json.get("expression", "")
        expr=parse_expression(expression)
        anti=sp.integrate(expr,x)
        der=sp.diff(expr,x)
        return jsonify({"ok":True,"normalized":str(expr),"latex":sp.latex(expr),
                        "antiderivative":str(anti),"antiderivative_latex":sp.latex(anti),
                        "derivative":str(der),"derivative_latex":sp.latex(der)})
    except Exception as exc:
        return jsonify({"ok":False,"error":f"No se pudo interpretar la fórmula: {exc}"}),400

@bp.post("/sample")
def sample():
    try:
        expression=request.json.get("expression", "")
        values=request.json.get("x", [])
        expr=parse_expression(expression)
        import numpy as np
        fn=sp.lambdify(x,expr,modules=["numpy"])
        xs=np.asarray(values,dtype=float)
        ys=np.asarray(fn(xs),dtype=float)
        ys=np.where(np.isfinite(ys),ys,np.nan)
        anti=sp.integrate(expr,x)
        return jsonify({"ok":True,"normalized":str(expr),"latex":sp.latex(expr),"y":ys.tolist(),
                        "antiderivative":str(anti),"antiderivative_latex":sp.latex(anti)})
    except Exception as exc:
        return jsonify({"ok":False,"error":f"No se pudo evaluar la función: {exc}"}),400

@bp.post("/integrate")
def integrate():
    try:
        expression=request.json.get("expression", "")
        a=request.json.get("a")
        b=request.json.get("b")
        expr=parse_expression(expression)
        if a is None or b is None:
            result=sp.integrate(expr,x)
            return jsonify({"ok":True,"type":"indefinite","exact":str(result),"latex":sp.latex(result)})
        a_expr=parse_expression(str(a)); b_expr=parse_expression(str(b))
        exact=sp.integrate(expr,(x,a_expr,b_expr))
        numeric=sp.N(exact,16)
        return jsonify({"ok":True,"type":"definite","exact":str(exact),"latex":sp.latex(exact),
                        "numeric":finite_float(numeric)})
    except Exception as exc:
        return jsonify({"ok":False,"error":f"No se pudo integrar: {exc}"}),400
