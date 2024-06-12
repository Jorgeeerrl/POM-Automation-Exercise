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
    MODAL_CHECKOUT = ("css selector", "#checkoutModal .modal-content")
    BOTON_MODAL_LOG_REG = ("css selector", "#checkoutModal [href='/login']")
    BOTON_MODAL_CONTINUAR = ("css selector", "#checkoutModal .btn-success")
    BOTON_CHECKOUT = ("css selector", "a[class='btn btn-default check_out']")


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

    @allure.step("Modal checkout pop up visible")
    def modal_checkout_visible(self):
        self.wait.until(EC.visibility_of_element_located(self.MODAL_CHECKOUT))
        self.wait.until(EC.visibility_of_element_located(self.BOTON_MODAL_LOG_REG))
        self.wait.until(EC.visibility_of_element_located(self.BOTON_MODAL_CONTINUAR))
        self.wait.until(EC.element_to_be_clickable(self.BOTON_MODAL_LOG_REG))
        self.wait.until(EC.element_to_be_clickable(self.BOTON_MODAL_CONTINUAR))

    @allure.step("Click botón 'Login/Registro'")
    def click_boton_log_reg(self):
        self.modal_checkout_visible()
        self.wait.until(EC.element_to_be_clickable(self.BOTON_MODAL_LOG_REG)).click()

    @allure.step("Click botón 'Proceed To Checkout'")
    def click_boton_proceed(self):
        self.wait.until(EC.element_to_be_clickable(self.BOTON_CHECKOUT)).click()
        self.check_and_close_publi()

    @allure.step("Borrar primer producto del carrito")
    def borrar_primer_producto(self):
        self.carrito_NO_vacio()
        boton_delete_locator = ("xpath", "//a[@class='cart_quantity_delete'][1]")
        boton_delete = self.wait.until(EC.element_to_be_clickable(boton_delete_locator))
        boton_delete.click()

        nombre_producto = self.get_nombres_productos_carrito()[0]
        boton_delete.click()
        allure.attach(f"Producto borrado: {nombre_producto}", name="Producto Borrado")

    @allure.step("Comprobar carrito vacío")
    def carrito_vacio(self):
        vacio_visible = self.wait.until(EC.visibility_of_element_located(self.CARRITO_VACIO))
        allure.attach(f"Carrito Vacío: {vacio_visible}", name="Comprobar Carrito Vacío")
        self.screenshot("Carrito Vacío")
