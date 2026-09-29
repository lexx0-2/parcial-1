# Métodos Numéricos e Integración — Plataforma modular

Aplicación web educativa en Python/Flask para los módulos 1–14. Los módulos 1–6 corresponden a la primera fase funcional y los módulos 7–14 son placeholders para las siguientes fases.

## Arquitectura

```text
metodos_numericos_web/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
├── static/
│   └── css/
│       └── style.css
└── modules/
    ├── module_01/
    │   ├── __init__.py
    │   └── routes.py
    ├── module_02/
    ...
    └── module_14/
```

Cada carpeta `module_XX` es un módulo independiente y utiliza un Flask Blueprint. Esto permite desarrollar, probar y ampliar cada tema sin mezclar su lógica con los demás.

### Tecnologías

- Python 3.10+
- Flask
- HTML5/CSS3/JavaScript
- Plotly.js para visualizaciones interactivas
- Math.js para evaluar expresiones matemáticas en el navegador
- KaTeX para renderizar fórmulas

Plotly, Math.js y KaTeX se cargan mediante CDN desde las páginas HTML, por lo que no necesitan instalarse con `pip`.

## Requisitos

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar:

```bash
python app.py
```

Abrir:

```text
http://127.0.0.1:5000/
```

## Módulos funcionales

1. Sumas de Riemann: izquierda, derecha y punto medio; convergencia; 2 ejemplos.
2. Regla del Trapecio: teoría, geometría, visualizador y 2 ejemplos.
3. Regla del Punto Medio: teoría, visualizador y 2 ejemplos.
4. Regla de Simpson: teoría, condición de n par, parábolas y 2 ejemplos.
5. Integral Definida y Área bajo la Curva: TFC, límites ajustables y 2 ejemplos, incluido área entre curvas.
6. Integración Directa: fórmulas, 3 ejemplos paso a paso y gráficas de f(x) y F(x).
7–14. Placeholders con el mensaje exacto solicitado.

## Contribuir

1. Crear una rama:
   ```bash
   git checkout -b feature/nuevo-modulo
   ```
2. Mantener cada módulo dentro de su carpeta `modules/module_XX/`.
3. No mezclar JavaScript específico de un módulo con otro.
4. Probar la aplicación antes de hacer commit.
5. Hacer commit descriptivo:
   ```bash
   git add .
   git commit -m "Agrega visualizador del modulo X"
   ```
6. Crear un Pull Request explicando cambios, pruebas realizadas y posibles pendientes.

## Publicar en GitHub

```bash
git init
git add .
git commit -m "Proyecto inicial de métodos numéricos"
git branch -M main
git remote add origin URL_DE_TU_REPOSITORIO
git push -u origin main
```


## Motor matemático avanzado

La aplicación utiliza **SymPy** en el servidor para interpretar, evaluar, derivar e integrar las expresiones. Esto permite manejar, entre otras:

```text
sin(x)      sen(x)       cos(x)       coseno(x)
tan(x)      tg(x)        e^x          exp(x)
ln(x)       log(x)       log10(x)     sqrt(x)      raiz(x)
abs(x)      sinh(x)      cosh(x)      tanh(x)
2sin(x)+3x^2-e^x
(x^2+1)/(x-1)
```

También acepta `pi`, `π`, `e`, potencias (`^`), fracciones y multiplicación implícita. La API `/api/parse` devuelve LaTeX, derivada y antiderivada; `/api/integrate` calcula integrales definidas o indefinidas; `/api/sample` prepara los valores para las gráficas.

## Modo oscuro

El botón **Modo oscuro** está disponible en todas las páginas y guarda la preferencia en `localStorage`.

El Módulo 6 permite introducir una función personalizada y obtiene automáticamente su antiderivada, derivada y gráfica de `f(x)` y `F(x)`.


## Solucionador de integrales directas

El Módulo 6 incluye un solucionador interactivo basado en SymPy. Permite introducir el integrando o pegar una integral sencilla como `∫(x^2+1)dx`. Se procesan potencias, raíces cuadradas, funciones trigonométricas, exponenciales, logaritmos, fracciones, productos con multiplicación implícita y expresiones con constantes/símbolos.

Ejemplos: `3/x^2 - 9/sqrt(x)`, `x + 4*sqrt(x) - 4/x`, `x - 1 - 1/x` y `(x-1)(x+1)`. En expresiones simbólicas como `(a*x+b*y)^2`, el sistema puede obtener una antiderivada en función de `a`, `b` e `y`; para graficar se recomienda asignar valores numéricos a los parámetros.
