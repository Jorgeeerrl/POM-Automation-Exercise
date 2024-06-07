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
    ETIQUETA_ALL_PRODUCTS = ("css selector", ".features_items h2.text-center")



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

    @allure.step("Añadir producto: {nombre_producto} al carrito")
    def add_product_to_cart_by_name(self, nombre_producto):
        locator_nombre_producto = ("xpath", f"(//p[text()='{nombre_producto}'])[1]")
        locator_precio_producto = ("xpath", f"//p[text()='{nombre_producto}']/preceding-sibling::h2")
        locator_add_cart = ("xpath", f"(//p[text()='{nombre_producto}']/following-sibling::a[@class='btn btn-default add-to-cart'])[2]")
        self.wait.until(EC.visibility_of_element_located(locator_nombre_producto))
        self.wait.until(EC.visibility_of_element_located(locator_precio_producto))
        self.scroll_into_view(locator_nombre_producto)
        self.hover(locator_nombre_producto)
        self.wait.until(EC.presence_of_element_located(locator_add_cart)).click()
        self.check_and_close_publi()

    @allure.step("Click '{categoria} -> {subcategoria}' categoria and subcategoria")
    def click_categoria_y_subcategoria(self, categoria, subcategoria):
        locator_categoria = ('css selector', f'a[href="#{categoria}"]')
        locator_subcategoria = ('xpath', f'//div[@id="{categoria}"]//a[contains(text(), "{subcategoria}")]')
        self.wait.until(EC.element_to_be_clickable(locator_categoria)).click()
        self.check_and_close_publi()
        self.wait.until(EC.element_to_be_clickable(locator_subcategoria)).click()
        self.check_and_close_publi()

    @allure.step("Verificar que '{categoria} -> {subcategoria}' Están abiertas")
    def verificar_productos_categoria_subcategoria(self, categoria, subcategoria):
        texto_esperado = f"{categoria} - {subcategoria} Products"
        texto_productos = self.wait.until(EC.visibility_of_element_located(self.ETIQUETA_ALL_PRODUCTS))
        texto_productos = texto_productos.text
        texto_esperado_uppercase = texto_esperado.upper()
        texto_productos_uppercase = texto_productos.upper()
        assert texto_esperado_uppercase in texto_productos_uppercase, f"Expected '{texto_esperado}' en TEXTO_ETIQUETA, pero se ha encontrado '{texto_productos}'"
        self.screenshot("Productos de la subcategoría")

    @allure.step("Click en la brand '{brand_producto}'")
    def click_brand_productos(self, brand_producto):

        brands_validas = ["Polo", "H&M", "Madame", "Mast & Harbour", "Babyhug", "Allen Solly Junior", "Kookie Kids", "Biba"]

        if brand_producto not in brands_validas:
            raise ValueError(f"Brand Inválida. Las Brands válidas son: {', '.join(brands_validas)}")

        brand = ('css selector', f'.left-sidebar .brands-name a[href="/brand_products/{brand_producto}"]')
        self.scroll_into_view(brand)
        self.wait.until(EC.element_to_be_clickable(brand)).click()
        self.check_and_close_publi()

    @allure.step("Verificar página y productos en '{brand_producto}'")
    def verificar_productos_brand_page(self, brand_producto):
        texto_esperado = f"Brand - {brand_producto} Products"

        texto_productos = self.wait.until(EC.visibility_of_element_located(self.ETIQUETA_ALL_PRODUCTS))
        texto_productos = texto_productos.text
        texto_esperado_uppercase = texto_esperado.upper()
        texto_productos_uppercase = texto_productos.upper()
        assert texto_esperado_uppercase  in texto_productos_uppercase, f"Expected '{texto_esperado}' en TEXTO_ETIQUETA, pero se ha encontrado '{texto_productos}'"
        self.screenshot("Productos de la brand")