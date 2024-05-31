import allure
import os
from .page_base import PageBase
from utils.urls import Urls
from selenium.webdriver.support import expected_conditions as EC


class PageContacto(PageBase):

    PAGE_URL= Urls.PAGE_CONTACTO

    FIELD_NOMBRE_CONTACTO = ('css selector', "[name='name']")
    FIELD_EMAIL_CONTACTO = ('css selector', "[name='email']")
    FIELD_SUBJECT_CONTACTO = ('css selector', "[name='subject']")
    FIELD_MENSAJE_CONTACTO = ('css selector', "#message")
    BOTON_SUBMIT = ('css selector', "[name='submit']")
    SELECCIONAR_ARCHIVO = ('css selector', "[name='upload_file']")
    FORMULARIO_CONTACTO = ('css selector', "#contact-us-form.contact-form")
    MENSAJE_SUCCESS = ('css selector', ".status.alert-success")
    BOTON_HOME_SUCCESS = ('css selector', ".btn-success")

    @allure.step("Formulario de Contacto Visible")
    def formulario_contacto_visible(self):
        self.wait.until(EC.visibility_of_element_located(self.FIELD_NOMBRE_CONTACTO))
        self.wait.until(EC.visibility_of_element_located(self.FIELD_EMAIL_CONTACTO))
        self.wait.until(EC.visibility_of_element_located(self.FIELD_SUBJECT_CONTACTO))
        self.wait.until(EC.visibility_of_element_located(self.FIELD_MENSAJE_CONTACTO))
        self.wait.until(EC.visibility_of_element_located(self.SELECCIONAR_ARCHIVO))
        self.wait.until(EC.visibility_of_element_located(self.BOTON_SUBMIT))
        self.screenshot("Formulario de Contacto")

    @allure.step("Click Botón Home")
    def click_boton_home_success(self):
        self.wait.until(EC.visibility_of_element_located(self.BOTON_HOME_SUCCESS))
        self.wait.until(EC.visibility_of_element_located(self.MENSAJE_SUCCESS))
        self.wait.until(EC.element_to_be_clickable(self.BOTON_HOME_SUCCESS)).click()

    @allure.step("Subir Archivo")
    def subir_archivo_contacto(self):
        archivo = self.wait.until(EC.visibility_of_element_located(self.SELECCIONAR_ARCHIVO))
        path_archivo = os.path.join(os.getcwd(), 'recursos', 'foto_contacto.png')
        archivo.send_keys(path_archivo)
        self.screenshot('Archivo Subido')

    @allure.step("Rellenar Formulario Random")
    def rellenar_formulario_contacto(self):
        self.rellenar(self.FIELD_NOMBRE_CONTACTO, self.fake.name())
        self.rellenar(self.FIELD_EMAIL_CONTACTO, self.fake.email())
        self.rellenar(self.FIELD_SUBJECT_CONTACTO, self.fake.sentence())
        self.rellenar(self.FIELD_MENSAJE_CONTACTO, self.fake.paragraph())
        self.screenshot('Formulario Relleno')

    @allure.step("Click Botón Submit")
    def click_boton_submit(self):
        self.wait.until(EC.visibility_of_element_located(self.BOTON_SUBMIT))
        self.wait.until(EC.element_to_be_clickable(self.BOTON_SUBMIT)).click()

    @allure.step("Aceptar Alerta")
    def aceptar_alerta(self):
        alert = self.wait.until(EC.alert_is_present())
        self.driver.switch_to.alert
        alert.accept()