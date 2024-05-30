import allure
from .page_base import PageBase
from utils.urls import Urls
from selenium.webdriver.support import expected_conditions as EC


class PageCuentaCreada(PageBase):

    PAGE_URL= Urls.PAGE_CUENTA_CREADA

    MENSAJE_CUENTA_CREADA = ('css selector', '[data-qa="account-created"]')
    BOTON_CONTINUE = ('css selector', '[data-qa="continue-button"]')

    @allure.step("Click Botón Continue")
    def click_boton_continue(self):
        self.wait.until(EC.element_to_be_clickable(self.BOTON_CONTINUE)).click()
        self.check_and_close_publi()

    @allure.step("Mensaje de Cuenta Creada Visible")
    def mensaje_cuenta_creada_visible(self):
        self.wait.until(EC.visibility_of_element_located(self.MENSAJE_CUENTA_CREADA))
        self.screenshot("Cuenta Creada")