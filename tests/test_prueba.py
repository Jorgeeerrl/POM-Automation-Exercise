import allure
from .test_base import TestBase


@allure.feature("Checkout")
class TestSuiteCheckout(TestBase):

    @allure.story("Proceso de Checkout")
    @allure.tag('Test Case: 24')
    @allure.title("Download Invoice after purchase order")
    def test_comprobar_descarga_archivo_invoice(self):
        self.registrar_cuenta()

        self.page_home.click_boton_products()
        self.page_productos.pagina_abierta()
        self.page_productos.add_product_to_cart_by_name('Green Side Placket Detail T-Shirt')
        self.page_productos.click_boton_view_cart()
        self.page_carrito.pagina_abierta()
        self.page_carrito.productos_presentes_carrito('Green Side Placket Detail T-Shirt')
        self.page_carrito.click_boton_proceed()
        self.page_checkout.pagina_abierta()
        self.page_checkout.direccion_envio_visible()
        self.page_checkout.direccion_facturacion_visible()
        self.page_checkout.verificar_info_envio()
        self.page_checkout.verificar_info_facturacion()
        self.page_checkout.rellenar_comentarios_envio()
        self.page_checkout.click_boton_place_order()
        self.page_pago.formulario_tarjeta_visible()
        self.page_pago.rellenar_formulario_tarjeta()
        self.page_pago.click_boton_confirm_order()
        self.page_envio.mensaje_pedido_realizado_visible()
        self.page_envio.click_boton_download_invoice()
        self.page_envio.click_boton_continue()
        self.page_home.pagina_abierta()

        self.borrar_cuenta()
