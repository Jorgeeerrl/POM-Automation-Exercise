import allure
from .test_base import TestBase


@allure.feature("Navegación y Scroll")
class TestSuiteNavScroll(TestBase):

    @allure.story("Verificar Test Cases")
    @allure.tag('Test Case: 7')
    @allure.title("Verify All Cases Page")
    def test_verificar_test_cases(self):
        self.page_home.abrir_pagina()
        self.page_home.header_visible()
        self.page_home.click_boton_test_cases()
        self.page_test_cases.pagina_abierta()
        self.page_test_cases.testcases_visible()
        self.page_home.screenshot("Test Cases Presentes")