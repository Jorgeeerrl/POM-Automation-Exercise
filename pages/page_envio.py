from selenium.webdriver.support import expected_conditions as EC
from .page_base import PageBase
import allure
import os
import time


''' PROBAR A REFACTORIZAR PARA INCLUIR PAGE_ENVIO EN PAGE_PAGO '''

class PageEnvio(PageBase):

    MENSAJE_PEDIDO_REALIZADO = ('css selector', '.title > b')
    BOTON_CONTINUE = ('css selector', '[data-qa="continue-button"]')
    BOTON_DOWNLOAD_INVOICE = ('css selector', '.btn.check_out')


    @allure.step("Mensaje Pedido Realizado Visible")
    def mensaje_pedido_realizado_visible(self):
        self.wait.until(EC.visibility_of_element_located(self.MENSAJE_PEDIDO_REALIZADO))
        self.screenshot("Pedido Realizado")

    @allure.step("Click continue button")
    def click_boton_continue(self):
        self.wait.until(EC.element_to_be_clickable(self.BOTON_CONTINUE)).click()
        self.check_and_close_publi()

    @allure.step("Click Botón 'Download Invoice'")
    def click_boton_download_invoice(self):
        self.wait.until(EC.element_to_be_clickable(self.BOTON_DOWNLOAD_INVOICE)).click()
        time.sleep(3)
        path_archivo = os.path.join(os.getcwd(), 'recursos', 'invoice.txt')
        self.archivo_presente(path_archivo)

    @allure.step("Invoice Descargado")
    def archivo_presente(self, path_invoice):
        with allure.step(f"Verificar presencia del archivo en {path_invoice}"):
                if not os.path.exists(path_invoice) or not os.path.isfile(path_invoice):
                    raise FileNotFoundError(f"Archivo {path_invoice} no encontrado")

        return True
