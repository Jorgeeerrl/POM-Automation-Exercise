import allure
from .test_base import TestBase


@allure.feature("Pruebas")
class TestPrueba(TestBase):

    def test_prueba(self):

        print("Hola esto es una prueba")


