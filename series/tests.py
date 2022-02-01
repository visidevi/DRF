import string
from django.test import TestCase
from series.models import Serie, Episode
import uuid
# Create your tests here.
class TestSerie(TestCase):

    def _generate_serie(self):
        serie = Serie.objects.create(
            title=f"mock Serie {uuid.uuid4()}",
            description="Una serie mock"
        )
        for i in range(1, 6):
            Episode.objects.create(
                serie_id=serie.pk,
                name=f"Episodio {i}",
                number=i
            )
        return serie

    def test_retrive_serie(self):
        serie = self._generate_serie()
        response = self.client.get(f'/api/series/{serie.pk}/')
        self.assertEqual(response.status_code, 200)

        repsonse_json = response.json()
        self.assertIsInstance(repsonse_json, dict)
        self.assertIsInstance(repsonse_json.get('id'), int)
        self.assertIsInstance(repsonse_json.get('title'), str)
        self.assertIsInstance(repsonse_json.get('description'), str)
        self.assertIsInstance(repsonse_json.get('episodes'), list)
        self.assertIsInstance(repsonse_json.get('score'), None)
        self.assertEqual(len(repsonse_json.get('episodes')), 5)

