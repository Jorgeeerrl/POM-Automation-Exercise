import allure
from .page_base import PageBase
from utils.urls import Urls
from selenium.webdriver.support import expected_conditions as EC


class PageCuentaBorrada(PageBase):

    PAGE_URL= Urls.PAGE_CUENTA_BORRADA

    MENSAJE_CUENTA_BORRADA = ('css selector', '[data-qa="account-deleted"]')
    BOTON_CONTINUE = ('css selector', '[data-qa="continue-button"]')

    @allure.step("Click Botón Continue")
    def click_boton_continue(self):
        self.wait.until(EC.element_to_be_clickable(self.BOTON_CONTINUE)).click()
        self.check_and_close_publi()

    @allure.step("Mensaje Usuario Borrado Visible")
    def mensaje_cuenta_borrada_visible(self):
        self.wait.until(EC.visibility_of_element_located(self.MENSAJE_CUENTA_BORRADA))
        self.screenshot("Usuario Borrado")