import json
import math
import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

from app import app


class ModulePageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.config.update(TESTING=True)
        cls.client = app.test_client()

    def test_all_module_pages_render(self):
        for number in range(1, 15):
            with self.subTest(module=number):
                response = self.client.get(f"/modulo/{number:02d}/")
                self.assertEqual(response.status_code, 200)
                body = response.get_data(as_text=True)
                self.assertIn("Métodos Numéricos e Integración", body)
                self.assertIn("plot", body)

    def test_modules_7_to_14_have_renderable_plot_code(self):
        node = shutil.which("node")
        for number in range(7, 15):
            with self.subTest(module=number):
                response = self.client.get(f"/modulo/{number:02d}/")
                self.assertEqual(response.status_code, 200)
                body = response.get_data(as_text=True)
                self.assertIn('id="plot"', body)
                self.assertIn("drawMainGraph", body)
                self.assertIn("drawMethodDiagram", body)
                scripts = re.findall(r"<script>(.*?)</script>", body, flags=re.S)
                self.assertTrue(scripts, "No se encontró el JavaScript de la página")
                if node:
                    with tempfile.NamedTemporaryFile("w", suffix=".js", encoding="utf-8", delete=False) as handle:
                        handle.write(scripts[-1])
                        script_path = handle.name
                    try:
                        result = subprocess.run(
                            [node, "--check", script_path],
                            capture_output=True,
                            text=True,
                            timeout=15,
                        )
                        self.assertEqual(result.returncode, 0, result.stderr)
                    finally:
                        Path(script_path).unlink(missing_ok=True)


class CalculationRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.config.update(TESTING=True)
        cls.client = app.test_client()

    def integrate(self, expression, a, b, expected, places=7):
        response = self.client.post(
            "/api/integrate",
            json={"expression": expression, "a": a, "b": b},
        )
        self.assertEqual(response.status_code, 200, response.get_data(as_text=True))
        payload = response.get_json()
        self.assertTrue(payload["ok"])
        self.assertAlmostEqual(float(payload["numeric"]), expected, places=places)

    def test_representative_integrals_from_modules_7_to_12(self):
        self.integrate("x*exp(x)", 0, 2, math.e**2 + 1)                         # parts
        self.integrate("1/(x^2+1)", 0, 2, math.atan(2))                         # rational
        self.integrate("1/sqrt(x)", 0, 2, 2*math.sqrt(2))                       # irrational
        self.integrate("sin(x)^2", 0, 2, 1 - math.sin(4)/4)                     # trig identities
        self.integrate("1/sqrt(9-x^2)", 0, 2, math.asin(2/3))                   # trig substitution
        self.integrate("1/(1+cos(x))", 0, 2, math.tan(1))                       # universal substitution

    def test_module_5_area_between_curves(self):
        self.integrate("abs(x-x^2)", 0, 1, 1/6)

    def test_parse_verifies_the_derivative_of_the_antiderivative(self):
        response = self.client.post("/api/parse", json={"expression": "(x-1)(x+1)"})
        self.assertEqual(response.status_code, 200, response.get_data(as_text=True))
        payload = response.get_json()
        self.assertTrue(payload["verification"])
        self.assertEqual(payload["antiderivative_derivative_latex"], "x^{2} - 1")

    def test_cross_section_volume_formulas(self):
        self.integrate("x^2", 0, 2, 8/3)                                       # square, side x
        self.integrate("pi*2^2/8", 0, 3, 3*math.pi/2)                           # semicircle, diameter 2
        self.integrate("sqrt(3)*x^2/4", 0, 2, 2*math.sqrt(3)/3)                 # equilateral triangle, side x

    def test_revolution_volume_formulas(self):
        self.integrate("pi*x^2", 0, 2, 8*math.pi/3)                            # disks
        self.integrate("pi*((x+2)^2-2^2)", 0, 2, 32*math.pi/3)                 # washers
        self.integrate("2*pi*x*x^2", 0, 2, 8*math.pi)                          # shells about y-axis

    def test_graph_samples_are_strict_json_and_domain_gaps_are_null(self):
        response = self.client.post(
            "/api/sample",
            json={"expression": "1/sqrt(x)", "x": [-1, 0, 1, 4]},
        )
        self.assertEqual(response.status_code, 200, response.get_data(as_text=True))
        raw = response.get_data(as_text=True)
        json.loads(raw, parse_constant=lambda value: self.fail(f"Invalid JSON constant: {value}"))
        values = response.get_json()["y"]
        self.assertEqual(values[0], None)
        self.assertEqual(values[1], None)
        self.assertAlmostEqual(values[2], 1.0)
        self.assertAlmostEqual(values[3], 0.5)

    def test_constant_function_is_sampled_at_every_x(self):
        response = self.client.post(
            "/api/sample",
            json={"expression": "5", "x": [0, 1, 2]},
        )
        self.assertEqual(response.status_code, 200, response.get_data(as_text=True))
        self.assertEqual(response.get_json()["y"], [5.0, 5.0, 5.0])


if __name__ == "__main__":
    unittest.main()
