import allure
from .test_base import TestBase


class TestSuiteLoginRegistro(TestBase):

    @allure.tag('Test Case: 1')
    @allure.title("Register User")
    def test_registro_correcto(self):
        self.page_home.abrir_pagina()
        self.page_home.pagina_abierta()
        self.page_home.click_boton_login_registro()
        self.page_login_registro.pagina_abierta()
        self.page_login_registro.introducir_nombre_registro()
        self.page_login_registro.introducir_email_registro()
        self.page_login_registro.click_boton_registro()
        self.page_registro.pagina_abierta()
        self.page_registro.rellenar_account_info()
        self.page_registro.rellenar_adress_info()
        self.page_registro.click_boton_crear_cuenta()
        self.page_cuenta_creada.pagina_abierta()
        self.page_cuenta_creada.mensaje_cuenta_creada_visible()
        self.page_cuenta_creada.click_boton_continue()
        self.page_home.pagina_abierta()
        self.page_home.user_name_visible()
        self.page_home.user_status_ok()
        self.page_home.click_boton_delete_account()
        self.page_cuenta_borrada.pagina_abierta()
        self.page_cuenta_borrada.mensaje_cuenta_borrada_visible()
        self.page_cuenta_borrada.click_boton_continue()
        self.page_home.pagina_abierta()

    @allure.tag('Test Case: 2')
    @allure.title("Login User with correct email and password")
    def test_login_correcto(self):
        self.registrar_cuenta()
        self.logout_cuenta()

        self.page_login_registro.pagina_abierta()
        self.page_login_registro.introducir_login()
        self.page_login_registro.introducir_password()
        self.page_login_registro.click_boton_login()
        self.page_home.pagina_abierta()
        self.page_home.user_name_visible()
        self.page_home.user_status_ok()

        self.borrar_cuenta()

    @allure.tag('Test Case: 3')
    @allure.title("Login User with incorrect email and password")
    def test_login_incorrecto(self):
        self.page_home.abrir_pagina()
        self.page_home.pagina_abierta()
        self.page_home.click_boton_login_registro()
        self.page_login_registro.pagina_abierta()
        self.page_login_registro.introducir_email_password_incorrectos()
        self.page_login_registro.click_boton_login()
        self.page_login_registro.error_email_password_invalidos_visible()

    @allure.tag('Test Case: 4')
    @allure.title("Logout User")
    def test_logout(self):
        self.registrar_cuenta()

        self.page_home.click_boton_logout()
        self.page_login_registro.pagina_abierta()

        self.login_cuenta()
        self.borrar_cuenta()

    @allure.tag('Test Case: 5')
    @allure.title("Register User with existing email")
    def test_registro_email_existente(self):
        self.page_home.abrir_pagina()
        self.page_home.pagina_abierta()
        self.page_home.click_boton_login_registro()
        self.page_login_registro.pagina_abierta()
        self.page_login_registro.introducir_nombre_registro()
        self.page_login_registro.introducir_email_existente()
        self.page_login_registro.click_boton_registro()
        self.page_login_registro.error_email_existe_visible()