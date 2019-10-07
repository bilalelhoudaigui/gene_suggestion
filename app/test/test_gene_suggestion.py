import unittest
from app.test.base import BaseTestCase
from api import app


class ApiTestCase(BaseTestCase):

    def test_gene_suggest_response(self):
        expected_data = {
            "data": [
                {"display_label": "BRCA1", "species": "homo_sapiens"}
            ]
        }
        client = app.test_client()
        test_url = '/api/v1/gene_suggest?query=BRCA1&specie=homo_sapiens&limit=1'
        response = client.get(test_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(expected_data, response.json)


if __name__ == '__main__':
    unittest.main()
