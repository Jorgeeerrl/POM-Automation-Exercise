import allure
from .page_base import PageBase
from utils.urls import Urls
from selenium.webdriver.support import expected_conditions as EC


class PageProductos(PageBase):

    PAGE_URL = Urls.PAGE_PRODUCTOS

    PANEL_IZQUIERDO = ("css selector", ".left-sidebar")
    CONTENEDOR_PRODUCTOS = ("css selector", ".features_items")
    BUSCAR_PRODUCTO = ("css selector", "#search_product")
    BOTON_SUBMIT_BUSCAR = ("css selector", "#submit_search")



    @allure.step("Página Productos Visible")
    def productos_visibles(self):
        self.wait.until(EC.visibility_of_element_located(self.PANEL_IZQUIERDO))
        self.wait.until(EC.visibility_of_element_located(self.CONTENEDOR_PRODUCTOS))
        self.screenshot("Página de Productos")

    @allure.step("Click botón 'View product' by ID: {id_producto}")
    def click_boton_view_product_por_id(self, id_producto):
        boton_view = ("xpath", f"//a[@href='/product_details/{id_producto}'][contains(.,'View Product')]")
        self.scroll_into_view(boton_view)
        self.wait.until(EC.element_to_be_clickable(boton_view)).click()
        self.check_and_close_publi()

    @allure.step("Introducir {datos_busqueda} en búsqueda y hacer click en buscar")
    def rellenar_busqueda_y_click_boton_buscar(self, datos_busqueda):
        self.rellenar(self.BUSCAR_PRODUCTO, datos_busqueda)
        self.wait.until(EC.visibility_of_element_located(self.BOTON_SUBMIT_BUSCAR))
        self.wait.until(EC.element_to_be_clickable(self.BOTON_SUBMIT_BUSCAR)).click()
        self.check_and_close_publi()
        self.screenshot("Resultado de la Búsqueda")

    @allure.step("Página de Productos Buscados Visible")
    def productos_buscados_visible(self):
        self.wait.until(EC.visibility_of_element_located(self.PANEL_IZQUIERDO))
        self.wait.until(EC.visibility_of_element_located(self.CONTENEDOR_PRODUCTOS))
        self.screenshot("Productos Buscados")