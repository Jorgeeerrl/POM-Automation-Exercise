import allure
from .page_base import PageBase
from utils.urls import Urls
from selenium.webdriver.support import expected_conditions as EC
from utils.generador_datos import Datos


class PageCheckout(PageBase):

    PAGE_URL = Urls.PAGE_CHECKOUT

    ETIQUETA_DIRECCION_ENVIO = ("css selector", "#address_delivery")
    ETIQUETA_DIRECCION_FACTURACION = ("css selector", "#address_invoice")
    DE_NOMBRE = ('css selector', '#address_delivery > .address_firstname')
    DF_NOMBRE = ('css selector', '#address_invoice > .address_firstname')
    DE_DIRECCION_1 = ("xpath", "(//li[@class='address_address1 address_address2'])[2]")
    DF_DIRECCION_1 = ("xpath", "(//li[@class='address_address1 address_address2'])[5]")
    DE_DIRECCION_2 = ("xpath", "(//li[@class='address_address1 address_address2'])[3]")
    DF_DIRECCION_2 = ("xpath", "(//li[@class='address_address1 address_address2'])[6]")
    DE_POBLACION = ('css selector', '#address_delivery > .address_city') # Formato State + City + Zip
    DF_POBLACION= ('css selector', '#address_invoice > .address_city')
    DE_PAIS = ('xpath', '(//li[@class="address_country_name"])[1]')
    DF_PAIS = ('xpath', '(//li[@class="address_country_name"])[2]')
    DE_TELEFONO = ('css selector', '#address_delivery > .address_phone')
    DF_TELEFONO = ('css selector', '#address_invoice > .address_phone')
    MENSAJE_ENVIO = ("css selector", "#ordermsg [name='message']")
    BOTON_ENVIO = ("css selector", "[href='/payment']")
    # info = ("", ".address_firstname.address_lastname")


    @allure.step("Información de dirección de envío visible")
    def direccion_envio_visible(self):
        self.wait.until(EC.visibility_of_element_located(self.ETIQUETA_DIRECCION_ENVIO))
        self.screenshot("Dirección de envío")

    @allure.step("Información de dirección de facturación visible")
    def direccion_facturacion_visible(self):
        self.wait.until(EC.visibility_of_element_located(self.ETIQUETA_DIRECCION_FACTURACION))
        self.screenshot("Dirección de facturación")

    @allure.step("Verificar Información de Envío")
    def verificar_info_envio(self):
        texto_nombre = self.capturar_texto_elemento(self.DE_NOMBRE)
        texto_direccion1 = self.capturar_texto_elemento(self.DE_DIRECCION_1)
        texto_direccion2 = self.capturar_texto_elemento(self.DE_DIRECCION_2)
        texto_poblacion = self.capturar_texto_elemento(self.DE_POBLACION)
        texto_pais = self.capturar_texto_elemento(self.DE_PAIS)
        texto_telefono = self.capturar_texto_elemento(self.DE_TELEFONO)

        with allure.step("Verificar Nombre"):
            assert self.datos.nombre_registro in texto_nombre, f"Expected: {self.datos.nombre_registro} in {texto_nombre}"
            assert self.datos.apellido_registro in texto_nombre, f"Expected: {self.datos.apellido_registro} in {texto_nombre}"

        with allure.step("Verificar Dirección de Envío"):
            assert self.datos.direccion in texto_direccion1, f"Expected: {self.datos.direccion} in {texto_direccion1}"
            assert self.datos.direccion_secundaria in texto_direccion2, f"Expected: {self.datos.direccion_secundaria} in {texto_direccion2}"
            assert self.datos.poblacion in texto_poblacion, f"Expected: {self.datos.poblacion} in {texto_poblacion}"
            assert self.datos.provincia in texto_poblacion, f"Expected: {self.datos.provincia} in {texto_poblacion}"
            assert self.datos.codigo_postal in texto_poblacion, f"Expected: {self.datos.codigo_postal} in {texto_poblacion}"

        with allure.step("Verificar País y Teléfono"):
            assert self.datos.country in texto_pais, f"Expected: {self.datos.country} in {texto_pais}"
            assert self.datos.telefono in texto_telefono, f"Expected: {self.datos.telefono} in {texto_telefono}"

    @allure.step("Verificar Dirección de Facturación")
    def verificar_info_facturacion(self):
        texto_nombre = self.capturar_texto_elemento(self.DF_NOMBRE)
        texto_direccion1 = self.capturar_texto_elemento(self.DF_DIRECCION_1)
        texto_direccion2 = self.capturar_texto_elemento(self.DF_DIRECCION_2)
        texto_poblacion = self.capturar_texto_elemento(self.DF_POBLACION)
        texto_pais = self.capturar_texto_elemento(self.DF_PAIS)
        texto_telefono = self.capturar_texto_elemento(self.DF_TELEFONO)

        with allure.step("Verificar Nombre"):
            assert self.datos.nombre_registro in texto_nombre, f"Expected: {self.datos.nombre_registro} in {texto_nombre}"
            assert self.datos.apellido_registro in texto_nombre, f"Expected: {self.datos.apellido_registro} in {texto_nombre}"

        with allure.step("Verificar Dirección de Facturación"):
            assert self.datos.direccion in texto_direccion1, f"Expected: {self.datos.direccion} in {texto_direccion1}"
            assert self.datos.direccion_secundaria in texto_direccion2, f"Expected: {self.datos.direccion_secundaria} in {texto_direccion2}"
            assert self.datos.poblacion in texto_poblacion, f"Expected: {self.datos.poblacion} in {texto_poblacion}"
            assert self.datos.provincia in texto_poblacion, f"Expected: {self.datos.provincia} in {texto_poblacion}"
            assert self.datos.codigo_postal in texto_poblacion, f"Expected: {self.datos.codigo_postal} in {texto_poblacion}"

        with allure.step("Verificar País y Teléfono"):
            assert self.datos.country in texto_pais, f"Expected: {self.datos.country} in {texto_pais}"
            assert self.datos.telefono in texto_telefono, f"Expected: {self.datos.telefono} in {texto_telefono}"

    @allure.step("Rellenar comentario de envío")
    def rellenar_comentarios_envio(self):
        self.scroll_into_view(self.MENSAJE_ENVIO)
        self.rellenar(self.MENSAJE_ENVIO, self.fake.paragraph())
        self.screenshot('Comentarios de Envío')

    @allure.step("Click Botón 'Place Order'")
    def click_boton_place_order(self):
        self.scroll_into_view(self.BOTON_ENVIO)
        self.wait.until(EC.element_to_be_clickable(self.BOTON_ENVIO)).click()
        self.check_and_close_publi()
