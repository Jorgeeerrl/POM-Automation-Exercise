import allure
from .test_base import TestBase

@allure.feature("Gestión de Productos")
class TestSuiteGestionProductos(TestBase):


    @allure.story("Información y Detalles de Productos")
    @allure.tag('Test Case: 8')
    @allure.title("Verify All Products and Product Detail Page")
    def test_detalles_productos(self):
        self.page_home.abrir_pagina()
        self.page_home.pagina_abierta()
        self.page_home.click_boton_products()
        self.page_productos.header_visible()
        self.page_productos.pagina_abierta()
        self.page_productos.productos_visibles()
        self.page_productos.click_boton_view_product_por_id(2)
        self.page_detalles_producto.header_visible()
        self.page_detalles_producto.detalles_producto_visible()

    @allure.story("Información y Detalles de Productos")
    @allure.tag('Test Case: 9')
    @allure.title("Search Product")
    def test_busqueda_productos(self):
        self.page_home.abrir_pagina()
        self.page_home.pagina_abierta()
        self.page_home.click_boton_products()
        self.page_productos.pagina_abierta()
        self.page_productos.header_visible()
        self.page_productos.productos_visibles()
        self.page_productos.rellenar_busqueda_y_click_boton_buscar("Jeans")
        self.page_productos.productos_buscados_visible()
