import allure
from selenium.webdriver.support import expected_conditions as EC

from .page_base import PageBase

''' PROBAR A REFACTORIZAR PARA INCLUIR PAGE_ENVIO EN PAGE_PAGO '''

class PageEnvio(PageBase):

    MENSAJE_PEDIDO_REALIZADO = ('css selector', '.title > b')
    BOTON_CONTINUE = ('css selector', '[data-qa="continue-button"]')


    @allure.step("Mensaje Pedido Realizado Visible")
    def mensaje_pedido_realizado_visible(self):
        self.wait.until(EC.visibility_of_element_located(self.MENSAJE_PEDIDO_REALIZADO))
        self.screenshot("Pedido Realizado")

    @allure.step("Click continue button")
    def click_boton_continue(self):
        self.wait.until(EC.element_to_be_clickable(self.BOTON_CONTINUE)).click()
        self.check_and_close_publi()