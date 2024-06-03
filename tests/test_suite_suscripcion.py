import allure
from .test_base import TestBase


@allure.feature("Suscripción")
class TestSuiteSuscripcion(TestBase):

    @allure.story("Suscripción de Usuario")
    @allure.tag('Test Case: 10')
    @allure.title("Verify Subscription in home page")
    def test_verificar_suscripcion_page_home(self):
        self.page_home.abrir_pagina()
        self.page_home.pagina_abierta()
        self.page_home.scroll_abajo()
        self.page_home.subscription_visible()
        self.page_home.rellenar_email_subscription()
        self.page_home.click_boton_subscribe()
        self.page_home.mensaje_subscription_ok_visible()

    @allure.story("Suscripción de Usuario")
    @allure.tag('Test Case: 11')
    @allure.title("Verify Subscription in cart page")
    def test_verificar_suscripcion_page_carrito(self):
        self.page_home.abrir_pagina()
        self.page_home.pagina_abierta()
        self.page_home.click_boton_cart()
        self.page_carrito.pagina_abierta()
        self.page_carrito.header_visible()
        self.page_carrito.scroll_abajo()
        self.page_carrito.subscription_visible()
        self.page_carrito.rellenar_email_subscription()
        self.page_carrito.click_boton_subscribe()
        self.page_carrito.mensaje_subscription_ok_visible()
