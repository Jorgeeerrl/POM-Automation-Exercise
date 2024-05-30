import pytest

from utils.generador_datos import Datos

from pages.page_home import PageHome
from pages.page_login_registro import PageLoginRegistro
from pages.page_registro import PageRegistro
from pages.page_cuenta_creada import PageCuentaCreada
from pages.page_cuenta_borrada import PageCuentaBorrada

class TestBase:

    # Se definen las múltiples páginas como atributos de la clase para organizar y reutilizar el código mejor.

    datos: Datos

    page_home: PageHome
    page_login_registro: PageLoginRegistro
    page_registro: PageRegistro
    page_cuenta_creada: PageCuentaCreada
    page_cuenta_borrada: PageCuentaBorrada


    ''' Esta función está incluída en self.check_and_close_publi(). Uncomment para usarla adicionalmente si es preciso.

    def cerrar_cookie_popup(self):
        try:
            wait = WebDriverWait(self.driver, 0.5)
            cookie_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div[1]/div[2]/div[2]/button[1]/p")))
            cookie_button.click()
            print("Pop-up de cookies cerrado.")
        except TimeoutException:
            return("No se encontró el pop-up de cookies.")
    '''


    @pytest.fixture(autouse=True)
    def setup(self, request, driver):  # Se ejecuta automáticamente antes de cada prueba, iniciando las páginas y el driver.
        request.cls.driver = driver  # Permite que el driver sea accesible en las pruebas sin necesidad de pasarlo explícitamente.
        request.cls.datos = Datos()

        request.cls.page_home = PageHome(driver)
        request.cls.page_login_registro = PageLoginRegistro(driver)
        request.cls.page_registro = PageRegistro(driver)
        request.cls.page_cuenta_creada = PageCuentaCreada(driver)
        request.cls.page_cuenta_borrada = PageCuentaBorrada(driver)

    def registrar_cuenta(self):
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

    def login_cuenta(self):
        self.page_login_registro.pagina_abierta()
        self.page_login_registro.introducir_login()
        self.page_login_registro.introducir_password()
        self.page_login_registro.click_boton_login()
        self.page_home.pagina_abierta()
        self.page_home.user_name_visible()
        self.page_home.user_status_ok()

    def logout_cuenta(self):
        self.page_home.click_boton_logout()
        self.page_login_registro.pagina_abierta()

    def borrar_cuenta(self):
        self.page_home.click_boton_delete_account()
        self.page_cuenta_borrada.pagina_abierta()
        self.page_cuenta_borrada.mensaje_cuenta_borrada_visible()
        self.page_cuenta_borrada.click_boton_continue()
        self.page_home.pagina_abierta()