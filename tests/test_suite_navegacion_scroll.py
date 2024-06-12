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

    @allure.story("Funcionalidad Scroll")
    @allure.tag('Test Case: 25')
    @allure.title("Verify Scroll Up using 'Arrow' button and Scroll Down functionality")
    def test_boton_scroll_up(self):
        self.page_home.abrir_pagina()
        self.page_home.pagina_abierta()
        self.page_home.scroll_abajo()
        self.page_home.subscription_visible()
        self.page_home.screenshot("Final Página Visible")
        self.page_home.click_boton_arriba()
        self.page_home.header_visible()
        self.page_home.texto_slider_principal_visible()
        self.page_home.screenshot("Inicio Página Visible")

    @allure.story("Funcionalidad Scroll")
    @allure.tag('Test Case: 26')
    @allure.title("Verify Scroll Up without 'Arrow' button and Scroll Down functionality")
    def test_scroll_arriba_scroll_abajo(self):
        self.page_home.abrir_pagina()
        self.page_home.pagina_abierta()
        self.page_home.scroll_abajo()
        self.page_home.subscription_visible()
        self.page_home.screenshot("Final Página Visible")
        self.page_home.scroll_arriba()
        self.page_home.header_visible()
        self.page_home.texto_slider_principal_visible()
        self.page_home.screenshot("Inicio Página Visible")