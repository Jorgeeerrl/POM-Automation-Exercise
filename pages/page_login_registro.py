import allure
from .page_base import PageBase
from utils.urls import Urls
from selenium.webdriver.support import expected_conditions as EC


class PageLoginRegistro(PageBase):

    PAGE_URL= Urls.PAGE_LOGIN_REGISTRO

    EMAIL_LOGIN = ('css selector', '[data-qa="login-email"]')
    PASSWORD_LOGIN = ('css selector', '[data-qa="login-password"]')
    BOTON_LOGIN = ('css selector', '[data-qa="login-button"]')
    ETIQUETA_LOGIN = ('css selector', '.login-form h2')
    NOMBRE_REGISTRO = ('css selector', '[data-qa="signup-name"]')
    EMAIL_REGISTRO = ('css selector', '[data-qa="signup-email"]')
    BOTON_REGISTRO = ('css selector', '[data-qa="signup-button"]')
    ETIQUETA_REGISTRO = ('css selector', '.signup-form h2')
    MENSAJE_DATOS_INVALIDOS = ('xpath', '//*[text()="Your email or password is incorrect!"]')
    MENSAJE_EMAIL_EXISTE = ('xpath', '//*[text()="Email Address already exist!"]')

    @allure.step("Introducir nombre de registro")
    def introducir_nombre_registro(self):
        self.rellenar(self.NOMBRE_REGISTRO, self.datos.nombre_login)

    @allure.step("Introducir email de registro")
    def introducir_email_registro(self):
        self.rellenar(self.EMAIL_REGISTRO, self.datos.email)

    @allure.step("Introducir email existente en el registro")
    def introducir_email_existente(self):
        self.rellenar(self.EMAIL_REGISTRO, "example.test@mail.com")

    @allure.step("Introducir email y password incorrectos")
    def introducir_email_password_incorrectos(self):
        self.rellenar(self.EMAIL_LOGIN, "example.test@mail.com")
        self.rellenar(self.PASSWORD_LOGIN, "realyincorrectpassword")

    @allure.step("Click Botón Registro")
    def click_boton_registro(self):
        self.wait.until(EC.element_to_be_clickable(self.BOTON_REGISTRO)).click()
        self.check_and_close_publi()
        
    @allure.step("Introducir email en login")
    def introducir_login(self):
        self.rellenar(self.EMAIL_LOGIN, self.datos.email)
        
    @allure.step("Introducir Password")
    def introducir_password(self):
        self.rellenar(self.PASSWORD_LOGIN, self.datos.password)

    @allure.step("Click Botón Login")
    def click_boton_login(self):
        self.wait.until(EC.element_to_be_clickable(self.BOTON_LOGIN)).click()
        self.check_and_close_publi()

    @allure.step("Mensaje 'Email Address already exist!' visible")
    def error_email_existe_visible(self):
        texto_mensaje_error = self.wait.until(EC.visibility_of_element_located(self.MENSAJE_EMAIL_EXISTE)).text
        mensaje_error_esperado = "Email Address already exist!"

        with allure.step(f"Verificar texto del mensaje de error"):
            assert mensaje_error_esperado == texto_mensaje_error, f"Expected: {mensaje_error_esperado}, Actual: {texto_mensaje_error}"
        self.screenshot("Error 'Email Address already exist!'")

    @allure.step("Mensaje 'Your email or password is incorrect!' visible")
    def error_email_password_invalidos_visible(self):       
        texto_mensaje_error = self.wait.until(EC.visibility_of_element_located(self.MENSAJE_DATOS_INVALIDOS)).text
        mensaje_error_esperado = "Your email or password is incorrect!"

        with allure.step(f"Verificar texto del mensaje de error"):
            assert mensaje_error_esperado == texto_mensaje_error, f"Expected: {mensaje_error_esperado}, Actual: {texto_mensaje_error}"
        self.screenshot("Error 'Your email or password is incorrect!'")