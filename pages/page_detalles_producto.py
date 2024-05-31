import allure
from .page_base import PageBase
from utils.urls import Urls
from selenium.webdriver.support import expected_conditions as EC


class PageDetallesProducto(PageBase):

    NOMBRE_PRODUCTO = ("xpath", "//div[@class='product-information']/h2")
    PRECIO_PRODUCTO = ("xpath", "//div[@class='product-information']/span/span")
    CATEGORIA_PRODUCTO = ("xpath", "//div[@class='product-information']/p")
    DISPONIBILIDAD_PRODUCTO = ("xpath", "(//div[@class='product-information']/p)[2]")
    CONDICION_PRODUCTO = ("xpath", "(//div[@class='product-information']/p)[3]")
    BRAND_PRODUCTO = ("xpath", "(//div[@class='product-information']/p)[4]")


    @allure.step("Información de Producto visible")
    def detalles_producto_visible(self):
        self.wait.until(EC.visibility_of_element_located(self.NOMBRE_PRODUCTO))
        self.wait.until(EC.visibility_of_element_located(self.PRECIO_PRODUCTO))
        self.wait.until(EC.visibility_of_element_located(self.CATEGORIA_PRODUCTO))
        self.wait.until(EC.visibility_of_element_located(self.DISPONIBILIDAD_PRODUCTO))
        self.wait.until(EC.visibility_of_element_located(self.CONDICION_PRODUCTO))
        self.wait.until(EC.visibility_of_element_located(self.BRAND_PRODUCTO))