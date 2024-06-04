import allure
from .page_base import PageBase
from selenium.webdriver.support import expected_conditions as EC


class PagePago(PageBase):

    FORMULARIO_TARJETA = ("css selector", ".payment-information")
    NOMBRE_TARJETA = ("css selector", "[data-qa='name-on-card']")
    NUMERO_TARJETA = ("css selector", "[data-qa='card-number']")
    CVC_TARJETA = ("css selector", "[data-qa='cvc']")
    CADUCIDAD_TARJETA_MONTH = ("css selector", "[data-qa='expiry-month']")
    CADUCIDAD_TARJETA_YEAR = ("css selector", "[data-qa='expiry-year']")
    BOTON_PAY_AND_CONFIRM = ("css selector", "#submit[data-qa='pay-button']")


    @allure.step("Formulario Tarjeta Visible")
    def formulario_tarjeta_visible(self):
        self.wait.until(EC.visibility_of_element_located(self.FORMULARIO_TARJETA))
        self.screenshot("Formulario Tarjeta")

    @allure.step("Rellenar Detalles de Pago")
    def rellenar_formulario_tarjeta(self):
        self.rellenar(self.NOMBRE_TARJETA, self.datos.nombre_tarjeta)
        self.rellenar(self.NUMERO_TARJETA, self.datos.numero_tarjeta)
        self.rellenar(self.CVC_TARJETA, self.datos.cvc_tarjeta)
        self.rellenar(self.CADUCIDAD_TARJETA_MONTH, self.datos.mes_caducidad)
        self.rellenar(self.CADUCIDAD_TARJETA_YEAR, self.datos.any_caducidad)
        self.screenshot('Formulario de pago relleno')

    @allure.step("Click Botón Confirm Order")
    def click_boton_confirm_order(self):
        self.wait.until(EC.element_to_be_clickable(self.BOTON_PAY_AND_CONFIRM)).click()
        self.check_and_close_publi()