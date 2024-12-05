from django.test import TestCase
from django.urls import reverse
from .models import Laboratorio


class Tests_Laboratorio(TestCase):
    @classmethod
    def test_data(self):
        self.laboratorio = Laboratorio.objects.create(
            nombre='Lab A', ciudad='Ciudad A', pais='País A')

    def test_model(self):
        self.assertEqual(self.laboratorio.nombre, 'Lab A')
        self.assertEqual(self.laboratorio.ciudad, 'Ciudad A')
        self.assertEqual(self.laboratorio.pais, 'País A')

    def test_http_200(self):
        response = self.client.get(reverse('listar_laboratorios'))
        self.assertEqual(response.status_code, 200)

    def test_template(self):
        response = self.client.get(reverse('listar_laboratorios'))
        self.assertTemplateUsed(response, 'listar.html')

# Create your tests here.
