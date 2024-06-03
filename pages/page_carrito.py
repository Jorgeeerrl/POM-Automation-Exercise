import allure
from .page_base import PageBase
from utils.urls import Urls
from selenium.webdriver.support import expected_conditions as EC


class PageCarrito(PageBase):

    PAGE_URL = Urls.PAGE_CARRITO

    CANTIDAD_PRODUCTOS_CARRITO = ("xpath", "//td[contains(@class, 'cart_quantity')]/button")
    PRECIOS_PRODUCTOS_CARRITO = ("xpath", "//td[contains(@class, 'cart_price')]/p")
    PRECIO_TOTAL_CARRITO = ("xpath", "//p[contains(@class, 'cart_total_price')]")  # ver la posibilidad de eliminarlo
    CARRITO_VACIO = ("css selector", "#empty_cart")
    NOMBRES_PRODUCTOS_CARRITO = ("xpath", "//td[contains(@class, 'cart_description')]//a")


    @allure.step("Productos presentes en carrito")
    def productos_presentes_carrito(self, *nombres_a_comprobar):
        self.carrito_NO_vacio()
        nombres_productos_carrito = self.get_nombres_productos_carrito()

        for nombre_producto in nombres_a_comprobar:
            assert nombre_producto in nombres_productos_carrito, f"Producto '{nombre_producto}' no encontrado en el carrito"

        allure.attach(f"Productos Comprobados: {', '.join(nombres_a_comprobar)}", name="Comprobación de la presencia")

        self.wait.until(EC.presence_of_all_elements_located(self.CANTIDAD_PRODUCTOS_CARRITO))
        self.wait.until(EC.presence_of_all_elements_located(self.PRECIOS_PRODUCTOS_CARRITO))
        self.wait.until(EC.presence_of_all_elements_located(self.PRECIO_TOTAL_CARRITO))
        self.screenshot("Productos del Carrito")

    @allure.step("Comprobar carrito NO vacío")
    def carrito_NO_vacio(self):
        vacio = self.wait.until(EC.invisibility_of_element_located(self.CARRITO_VACIO))
        allure.attach(f"Carrito NO Vacío: {not vacio}", name="Comprobar Carrito NO Vacío")
        self.screenshot("Productos en el carrito")
        return not vacio

    @allure.step("Capturar nombres de los productos del carrito")
    def get_nombres_productos_carrito(self):
        nombres_productos = self.capturar_texto_elementos(self.NOMBRES_PRODUCTOS_CARRITO)
        allure.attach(f"Productos: {', '.join(nombres_productos)}", name="Productos del Carrito")
        return nombres_productos

    @allure.step("Capturar cantidades de los productos del carrito")
    def get_cantidades_productos_carrito(self):
        cantidades_productos = self.capturar_texto_elementos(self.CANTIDAD_PRODUCTOS_CARRITO)
        allure.attach(f"Cantidades: {', '.join(cantidades_productos)}", name="Cantidades de los Productos")
        return cantidades_productos

    def comprobar_cantidad_producto_1(self, cantidad):
        cantidades = self.get_cantidades_productos_carrito()
        cantidades = int(cantidades[0])
        with allure.step(f"Verificar que la cantidad es correcta"):
            assert cantidades == cantidad, f"Esperado: {cantidad}, Actual: {cantidades}"
        self.screenshot("Cantidad del Producto")