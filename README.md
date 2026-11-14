# Métodos Numéricos e Integración — Plataforma modular

Proyecto web educativo desarrollado con Python y Flask para el estudio de métodos numéricos e integración.

## Arquitectura

El repositorio está organizado con **una carpeta independiente por módulo**:

```text
parcial-1/
├── app.py
├── api.py
├── requirements.txt
├── README.md
├── static/
│   ├── css/style.css
│   └── js/app.js
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── module_01.html ... module_06.html
│   └── placeholder.html
└── modules/
    ├── module_01/
    ├── module_02/
    ├── module_03/
    ├── module_04/
    ├── module_05/
    ├── module_06/
    ├── module_07/
    ├── ...
    └── module_14/
```

Cada módulo usa un **Flask Blueprint**, de modo que la lógica de cada tema queda separada.

## Módulos

### Módulos 1–4 — Métodos Numéricos
1. **Sumas de Riemann**: izquierda, derecha y punto medio; ajuste de (n), convergencia y visualización.
2. **Regla del Trapecio**: fórmula, interpretación geométrica y trapecios sobre la curva.
3. **Regla del Punto Medio**: fórmula y rectángulos de punto medio.
4. **Regla de Simpson**: condición de (n) par y parábolas ajustadas.

### Módulo 5 — Integral Definida y Área
Incluye el Teorema Fundamental del Cálculo, ajuste de límites y visualización del área bajo la curva.

### Módulo 6 — Integración Directa
Incluye solucionador interactivo con potencias, polinomios, productos, fracciones, raíces, seno, coseno, tangente, exponenciales, logaritmos, funciones hiperbólicas, trigonometría inversa y constantes (e) y (pi).

Ejemplos aceptados:

```text
sin(x)
sen(x)
cos(x)
coseno(x)
tan(x)
e^x
exp(x)
ln(x)
log(x)
sqrt(x)
raiz(x)
3/x^2 - 9/sqrt(x)
x + 4*sqrt(x) - 4/x
x - 1 - 1/x
(x-1)(x+1)
∫(x^2+1)dx
```

El resultado se muestra con **KaTeX** y se comprueba mediante derivación.

### Módulos 7–14 — Técnicas de integración y volúmenes
7. **Integración por partes**: identidad de integración por partes y ejemplos.
8. **Integración racional**: factorización y fracciones parciales.
9. **Integración irracional**: radicales, potencias fraccionarias y sustituciones.
10. **Integración trigonométrica**: identidades trigonométricas y reducción de potencias.
11. **Sustitución trigonométrica**: sustituciones con seno, tangente y secante.
12. **Sustitución universal**: t=tan(x/2) para racionalizar seno y coseno.
13. **Volúmenes con sección conocida**: secciones cuadradas, semicirculares y triangulares.
14. **Volúmenes de sólidos de revolución**: discos, arandelas y capas cilíndricas.

Cada módulo tiene página propia, teoría, fórmulas, ejemplos resueltos, calculadora de integrales definidas y gráfica interactiva. Los módulos 13 y 14 incluyen controles específicos para calcular volúmenes.

## Tecnologías

- **Python 3.10+**
- **Flask**: servidor web.
- **SymPy**: parseo, derivación e integración simbólica.
- **NumPy**: evaluación numérica para las gráficas.
- **Plotly.js**: visualizaciones interactivas.
- **KaTeX**: renderizado de fórmulas matemáticas.
- **HTML5/CSS3/JavaScript**.

## Instalación

En Windows:

```bat
py -m venv .venv
.venv\Scripts\activate
py -m pip install -r requirements.txt
py app.py
```

Abrir:

```text
http://127.0.0.1:5000/
```

## Modo oscuro

La interfaz incluye un botón **Modo oscuro** y guarda la preferencia en el navegador mediante `localStorage`.

## Contribuir

1. Crear una rama para el cambio.
2. Mantener cada módulo dentro de `modules/module_XX/`.
3. Probar el proyecto localmente.
4. Usar commits descriptivos.
5. Abrir un Pull Request explicando los cambios y las pruebas realizadas.


## Mejoras didácticas y gráficas

La versión actual incorpora:
- Guías breves de resolución paso a paso en los 14 módulos.
- Gráficas numéricas con ejes identificados, títulos específicos y leyendas para las aproximaciones.
- Representaciones diferenciadas: rectángulos de Riemann, trapecios, puntos medios, parábolas de Simpson, área definida, funciones y antiderivadas.
- En los módulos 7 a 14, procedimientos específicos para partes, fracciones parciales, radicales, identidades trigonométricas, sustituciones y aplicaciones de volumen.
- En el módulo 14, una representación tridimensional del sólido generado por revolución con discos o arandelas.
