import allure
from .test_base import TestBase
import random


@allure.feature("Gestión de Productos")
class TestSuiteGestionProductos(TestBase):


    categorias_validas = ["Women", "Men", "Kids"]
    subcategorias_validas = {
        "Women": ["Dress", "Tops", "Saree"],
        "Men": ["Tshirts", "Jeans"],
        "Kids": ["Dress", "Tops & Shirts"]
    }
    categoria = random.choice(categorias_validas)
    subcategoria = random.choice(subcategorias_validas[categoria])

    brands_validas = ["Polo", "H&M", "Madame", "Mast & Harbour", "Babyhug", "Allen Solly Junior", "Kookie Kids", "Biba"]
    brand = random.choice(brands_validas)


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

    @allure.story("Gestión del Carrito")
    @allure.tag('Test Case: 12')
    @allure.title("Add Products in Cart")
    def test_add_productos_carrito(self):
        self.page_home.abrir_pagina()
        self.page_home.pagina_abierta()
        self.page_home.click_boton_products()
        self.page_productos.pagina_abierta()
        self.page_productos.add_product_to_cart_by_name('Sleeveless Dress')
        self.page_productos.click_boton_continue_shopping()
        self.page_productos.add_product_to_cart_by_name('Soft Stretch Jeans')
        self.page_productos.click_boton_view_cart()
        self.page_carrito.pagina_abierta()
        self.page_carrito.productos_presentes_carrito('Sleeveless Dress', 'Soft Stretch Jeans')

    @allure.story("Gestión del Carrito")
    @allure.tag('Test Case: 13')
    @allure.title("Verify Product Quantity in Cart")
    def test_cantidad_productos_carrito(self):
        self.page_home.abrir_pagina()
        self.page_home.pagina_abierta()
        self.page_home.click_boton_view_product_por_id(6)
        self.page_detalles_producto.detalles_producto_visible()
        self.page_detalles_producto.establecer_cantidad_producto(4)
        self.page_detalles_producto.click_boton_add_cart()
        self.page_detalles_producto.click_boton_view_cart()
        self.page_carrito.pagina_abierta()
        self.page_carrito.comprobar_cantidad_producto_1(4)

    @allure.story("Gestión del Carrito")
    @allure.tag('Test Case: 17')
    @allure.title("Remove Products From Cart")
    def test_eliminar_productos_carrito(self):
        self.page_home.abrir_pagina()
        self.page_home.pagina_abierta()
        self.page_home.click_boton_products()
        self.page_productos.pagina_abierta()
        self.page_productos.add_product_to_cart_by_name('Men Tshirt')
        self.page_productos.click_boton_continue_shopping()
        self.page_productos.add_product_to_cart_by_name('Fancy Green Top')
        self.page_productos.click_boton_continue_shopping()
        self.page_productos.add_product_to_cart_by_name('Stylish Dress')
        self.page_productos.click_boton_view_cart()
        self.page_carrito.pagina_abierta()
        self.page_carrito.productos_presentes_carrito('Men Tshirt', 'Fancy Green Top', 'Stylish Dress')
        self.page_carrito.borrar_primer_producto()
        self.page_carrito.productos_presentes_carrito('Fancy Green Top', 'Stylish Dress')

    @allure.story("Información y Detalles de Productos")
    @allure.tag('Test Case: 18')
    @allure.title("View Category Products")
    def test_categorias_productos(self):
        self.page_home.abrir_pagina()
        self.page_home.pagina_abierta()
        self.page_home.click_boton_products()
        self.page_productos.header_visible()
        self.page_productos.pagina_abierta()
        self.page_productos.productos_visibles()
        self.page_productos.click_categoria_y_subcategoria(self.categoria, self.subcategoria)
        self.page_productos.header_visible()
        self.page_productos.productos_visibles()
        self.page_productos.verificar_productos_categoria_subcategoria(self.categoria, self.subcategoria)

    @allure.story("Información y Detalles de Productos")
    @allure.tag('Test Case: 19')
    @allure.title("View & Cart Brand Products")
    def test_brand_productos(self):
        self.page_home.abrir_pagina()
        self.page_home.pagina_abierta()
        self.page_home.click_boton_products()
        self.page_productos.header_visible()
        self.page_productos.pagina_abierta()
        self.page_productos.productos_visibles()
        self.page_productos.click_brand_productos(self.brand)
        self.page_productos.header_visible()
        self.page_productos.verificar_productos_brand_page(self.brand)

    @allure.story("Gestión del Carrito")
    @allure.tag('Test Case: 20')
    @allure.title("Search Products and Verify Cart After Login")
    def test_products_presence_at_cart_after_login(self):
        self.registrar_cuenta()
        self.logout_cuenta()

        self.page_home.abrir_pagina()
        self.page_home.pagina_abierta()
        self.page_home.click_boton_products()
        self.page_productos.pagina_abierta()
        self.page_productos.header_visible()
        self.page_productos.productos_visibles()
        self.page_productos.rellenar_busqueda_y_click_boton_buscar("Dress")
        self.page_productos.productos_buscados_visible()
        self.page_productos.add_product_to_cart_by_name('Sleeveless Dress')
        self.page_productos.click_boton_continue_shopping()
        self.page_productos.add_product_to_cart_by_name('Stylish Dress')
        self.page_productos.click_boton_continue_shopping()
        self.page_productos.add_product_to_cart_by_name('Blue Cotton Indie Mickey Dress')
        self.page_productos.click_boton_view_cart()
        self.page_carrito.pagina_abierta()
        self.page_carrito.productos_presentes_carrito('Sleeveless Dress', 'Stylish Dress', 'Blue Cotton Indie Mickey Dress')
        self.page_carrito.click_boton_login_registro()

        self.login_cuenta()

        self.page_home.click_boton_cart()
        self.page_carrito.pagina_abierta()
        self.page_carrito.productos_presentes_carrito('Sleeveless Dress', 'Stylish Dress', 'Blue Cotton Indie Mickey Dress')
        self.page_carrito.click_boton_home()

        self.borrar_cuenta()

    @allure.story("Review de Producto")
    @allure.tag('Test Case: 21')
    @allure.title("Add Review on Product")
    def test_review_producto(self):
        self.page_home.abrir_pagina()
        self.page_home.pagina_abierta()
        self.page_home.click_boton_view_product_por_id(3)
        self.page_detalles_producto.detalles_producto_visible()
        self.page_detalles_producto.review_producto()
        self.page_detalles_producto.thanks_review_visible()

    @allure.story("Gestión del Carrito")
    @allure.tag('Test Case: 22')
    @allure.title("Add to cart from Recommended items")
    def test_add_producto_recomendado(self):
        self.page_home.abrir_pagina()
        self.page_home.pagina_abierta()
        self.page_home.slider_productos_recomendados_visible()
        self.page_home.click_boton_add_cart_primer_recomendado()
        self.page_home.click_boton_view_cart()
        self.page_carrito.pagina_abierta()
        self.page_carrito.carrito_NO_vacio()
