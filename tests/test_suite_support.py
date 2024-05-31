import allure
from .test_base import TestBase


@allure.feature("Soporte al Cliente")
class TestSuiteContactUs(TestBase):

    @allure.story("Formulario de Contacto")
    @allure.tag('Test Case: 6')
    @allure.title("Contact Us Form")
    def test_contact_us_form(self):
        self.page_home.abrir_pagina()
        self.page_home.pagina_abierta()
        self.page_home.header_visible()
        self.page_home.click_boton_contacto()
        self.page_contacto.pagina_abierta()
        self.page_contacto.formulario_contacto_visible()
        self.page_contacto.rellenar_formulario_contacto()
        self.page_contacto.subir_archivo_contacto()
        self.page_contacto.click_boton_submit()
        self.page_contacto.aceptar_alerta()
        self.page_contacto.screenshot("Mensaje 'Success'")
        self.page_contacto.click_boton_home_success()
        self.page_home.header_visible()
        self.page_home.pagina_abierta()