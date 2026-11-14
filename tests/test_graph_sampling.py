import json
import unittest

from flask import Flask
from api import bp as api_bp


class GraphSamplingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app = Flask(__name__)
        app.register_blueprint(api_bp)
        cls.client = app.test_client()

    def test_default_graph_functions_return_json_safe_values(self):
        expressions = [
            "x*exp(x)",
            "1/(x^2+1)",
            "1/sqrt(x)",
            "sin(x)^2",
            "1/sqrt(9-x^2)",
            "1/(1+cos(x))",
            "x",
        ]
        xs = [i / 100 for i in range(201)]
        for expression in expressions:
            with self.subTest(expression=expression):
                response = self.client.post(
                    "/api/sample",
                    json={"expression": expression, "x": xs},
                )
                self.assertEqual(response.status_code, 200)
                payload = response.get_json()
                self.assertTrue(payload["ok"])
                self.assertEqual(len(payload["y"]), len(xs))
                for value in payload["y"]:
                    self.assertTrue(value is None or isinstance(value, (int, float)))

    def test_undefined_values_are_null_not_nan(self):
        response = self.client.post(
            "/api/sample",
            json={"expression": "1/sqrt(x)", "x": [-1, 0, 1]},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["y"][:2], [None, None])
        self.assertEqual(response.get_json()["y"][2], 1.0)
        # The response body must be strict JSON: NaN and Infinity are forbidden.
        json.loads(response.get_data(as_text=True), parse_constant=lambda value: self.fail(value))

    def test_scalar_expression_is_expanded_to_all_sample_points(self):
        response = self.client.post(
            "/api/sample",
            json={"expression": "5", "x": [0, 1, 2]},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["y"], [5.0, 5.0, 5.0])


if __name__ == "__main__":
    unittest.main()
