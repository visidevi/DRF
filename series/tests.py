import string
from django.test import TestCase
from series.models import Serie, Episode
from django.contrib.auth.models import User
import uuid
# Create your tests here.
class TestSerie(TestCase):

    def _generate_user(self) -> User:
        return User.objects.create(
            username=f'fake Username {uuid.uuid4()}',
            password='superuser',
            email='user@gmail.com')

    def _generate_serie(self):
        serie = Serie.objects.create(
            title=f'mock Serie {uuid.uuid4()}',
            description='Una serie mock'
        )
        for i in range(1, 6):
            Episode.objects.create(
                serie_id=serie.pk,
                name=f'Episodio {i}',
                number=i
            )
        return serie

    def test_retrive_serie(self):
        serie = self._generate_serie()
        response = self.client.get(f'/api/series/{serie.pk}/')
        self.assertEqual(response.status_code, 200)

        response_json = response.json()
        self.assertIsInstance(response_json, dict)
        self.assertIsInstance(response_json.get('id'), int)
        self.assertIsInstance(response_json.get('title'), str)
        self.assertIsInstance(response_json.get('description'), str)
        self.assertIsInstance(response_json.get('episodes'), list)
        #self.assertIsInstance(response_json.get('score'), None)
        self.assertEqual(len(response_json.get('episodes')), 5)

    def test_create_serie(self):
        user = self._generate_user()
        #serie = self._generate_serie()
        self.client.force_login(user=user)
        serie_dict = {
            'title':f'mock Serie {uuid.uuid4()}',
            'description':'Una serie mock'
        }
        response = self.client.post(f'/api/series/', serie_dict)
        self.assertEqual(response.status_code, 200)

    def test_user_not_authorized(self):

        serie_dict = {
            'title':f'mock Serie {uuid.uuid4()}',
            'description':'Una serie mock'
        }
        response = self.client.post(f'/api/series/', serie_dict)
        self.assertEqual(response.status_code, 401)


