import allure
from .page_base import PageBase
from utils.urls import Urls
from selenium.webdriver.support import expected_conditions as EC

class PageHome(PageBase):

    PAGE_URL= Urls.PAGE_HOME

    SLIDER_PRODUCTOS_RECOMENDADOS = ("css selector", ".recommended_items")
    BOTON_ADD_CART_PRIMER_RECOMENDADO_ACTIVO = ("xpath", "(//*[@id='recommended-item-carousel']//*[contains(@class, 'active')]//*[contains(@class, 'add-to-cart')])[1]")
    BOTON_SCROLL_UP = ('css selector', '#scrollUp')
    TEXTO_SLIDER_PRINCIPAL = ("xpath", "//div[@class = 'item active']//h2[contains(text(), 'Full-Fledged practice website for Automation Engineers')]")


    @allure.step("Click botón 'View product' by ID")
    def click_boton_view_product_por_id(self, id_producto):
        boton_view = ("xpath", f"//div[@class='choose']//a[@href='/product_details/{id_producto}']")
        self.scroll_into_view(boton_view)
        self.wait.until(EC.element_to_be_clickable(boton_view)).click()
        self.check_and_close_publi()

    @allure.step("Scroll abajo para comprobar visibilidad de los productos recomendados")
    def slider_productos_recomendados_visible(self):
        self.scroll_into_view(self.SLIDER_PRODUCTOS_RECOMENDADOS)
        self.wait.until(EC.visibility_of_element_located(self.SLIDER_PRODUCTOS_RECOMENDADOS))
        self.screenshot("Productos Recomendados")

    @allure.step("Click botón añadir del primer producto recomendado")
    def click_boton_add_cart_primer_recomendado(self):
        self.wait.until(EC.visibility_of_element_located(self.BOTON_ADD_CART_PRIMER_RECOMENDADO_ACTIVO))
        self.wait.until(EC.element_to_be_clickable(self.BOTON_ADD_CART_PRIMER_RECOMENDADO_ACTIVO)).click()
        self.check_and_close_publi()

    @allure.step("Click Botón Arriba")
    def click_boton_arriba(self):
        self.wait.until(EC.visibility_of_element_located(self.BOTON_SCROLL_UP))
        self.wait.until(EC.element_to_be_clickable(self.BOTON_SCROLL_UP)).click()

    @allure.step("Texto 'Full-Fledged practice website...' visible en el slider")
    def texto_slider_principal_visible(self):
        self.wait.until(EC.visibility_of_element_located(self.TEXTO_SLIDER_PRINCIPAL))
        self.wait.until(EC.element_to_be_clickable(self.TEXTO_SLIDER_PRINCIPAL))