import allure
from .page_base import PageBase
from utils.urls import Urls
from selenium.webdriver.support import expected_conditions as EC


class PageRegistro(PageBase):

    PAGE_URL= Urls.PAGE_REGISTRO

    BOTON_CREAR_CUENTA = ('css selector', '[data-qa="create-account"]')
    BOTON_MR = ('css selector', '[value="Mr"]')
    BOTON_MRS = ('css selector', '[value="Mrs"]')
    FIELD_NOMBRE_USUARIO = ('css selector', '#name')
    FIELD_EMAIL = ('css selector', '#email')
    FIELD_PASSWORD = ('css selector', '#password')
    SELECT_DIA_NACIMIENTO = ('css selector', '#days')
    SELECT_MES_NACIMIENTO = ('css selector', '#months')
    SELECT_AÑO_NACIMIENTO = ('css selector', '#years')
    CHECKBOX_NEWSLETTER = ('css selector', '#newsletter')
    CHECKBOX_SPECIAL_OFFERS = ('css selector', '#optin')
    FIELD_NOMBRE = ('css selector', '#first_name')
    FIELD_APELLIDO = ('css selector', '#last_name')
    FIELD_EMPRESA = ('css selector', '#company')
    FIELD_DIRECCION = ('css selector', '#address1')
    FIELD_DIRECCION_2 = ('css selector', '#address2')
    SELECT_PAIS = ('css selector', '#country')
    FIELD_ESTADO = ('css selector', '#state')
    FIELD_CIUDAD = ('css selector', '#city')
    FIELD_CP = ('css selector', '#zipcode')
    FIELD_TELEFONO = ('css selector', '#mobile_number')

    @allure.step("Click Botón Crear Cuenta")
    def click_boton_crear_cuenta(self):
        self.scroll_into_view(self.BOTON_CREAR_CUENTA)
        self.wait.until(EC.element_to_be_clickable(self.BOTON_CREAR_CUENTA)).click()
        self.check_and_close_publi()

    @allure.step("Rellenar Account Information")
    def rellenar_account_info(self):

        self.seleccionar_sexo(self.BOTON_MRS)
        self.rellenar(self.FIELD_PASSWORD, self.datos.password)
        self.seleccionar_opcion(self.SELECT_DIA_NACIMIENTO, self.datos.dia_nacimiento)
        self.seleccionar_opcion(self.SELECT_MES_NACIMIENTO, self.datos.mes_nacimiento)
        self.seleccionar_opcion(self.SELECT_AÑO_NACIMIENTO, self.datos.any_nacimiento)
        self.seleccionar_checkbox(self.CHECKBOX_NEWSLETTER)
        self.seleccionar_checkbox(self.CHECKBOX_SPECIAL_OFFERS)
        self.screenshot('Formulario Info Cuenta Relleno')

    @allure.step("Rellenar Adress Information")
    def rellenar_adress_info(self):
        self.rellenar(self.FIELD_NOMBRE, self.datos.nombre_registro)
        self.rellenar(self.FIELD_APELLIDO, self.datos.apellido_registro)
        self.rellenar(self.FIELD_EMPRESA, self.datos.empresa)
        self.rellenar(self.FIELD_DIRECCION, self.datos.direccion)
        self.rellenar(self.FIELD_DIRECCION_2, self.datos.direccion_secundaria)
        self.seleccionar_opcion(self.SELECT_PAIS, self.datos.country)
        self.rellenar(self.FIELD_ESTADO, self.datos.provincia)
        self.rellenar(self.FIELD_CIUDAD, self.datos.poblacion)
        self.rellenar(self.FIELD_CP, self.datos.codigo_postal)
        self.rellenar(self.FIELD_TELEFONO, self.datos.telefono)
        self.screenshot('Formulario Info Dirección Relleno')
  