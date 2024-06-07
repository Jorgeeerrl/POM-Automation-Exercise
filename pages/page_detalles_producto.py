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
    FIELD_CANTIDAD_PRODUCTO = ("css selector", "#quantity")
    BOTON_ADD_CART = ("css selector", "button.cart")
    BOTON_SUBMIT_REVIEW = ("css selector", "#button-review")
    REVIEW_NOMBRE = ("css selector", "#name")
    REVIEW_EMAIL = ("css selector", "#email")
    REVIEW_FIELD = ("css selector", "#review")
    MENSAJE_REVIEW_SUCCESS = ("css selector", "#review-section .alert-success")


    @allure.step("Información de Producto visible")
    def detalles_producto_visible(self):
        self.wait.until(EC.visibility_of_element_located(self.NOMBRE_PRODUCTO))
        self.wait.until(EC.visibility_of_element_located(self.PRECIO_PRODUCTO))
        self.wait.until(EC.visibility_of_element_located(self.CATEGORIA_PRODUCTO))
        self.wait.until(EC.visibility_of_element_located(self.DISPONIBILIDAD_PRODUCTO))
        self.wait.until(EC.visibility_of_element_located(self.CONDICION_PRODUCTO))
        self.wait.until(EC.visibility_of_element_located(self.BRAND_PRODUCTO))

    @allure.step("Establecer Cantidad de Producto")
    def establecer_cantidad_producto(self, cantidad):
        self.rellenar(self.FIELD_CANTIDAD_PRODUCTO, f"{cantidad}")

    @allure.step("Click Botón 'Add to cart'")
    def click_boton_add_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.BOTON_ADD_CART)).click()

    @allure.step("Añadir Review de Producto")
    def review_producto(self):
        self.scroll_into_view(self.BOTON_SUBMIT_REVIEW)
        self.wait.until(EC.visibility_of_element_located(self.REVIEW_NOMBRE))
        self.wait.until(EC.visibility_of_element_located(self.REVIEW_EMAIL))
        self.wait.until(EC.visibility_of_element_located(self.REVIEW_FIELD))
        self.wait.until(EC.visibility_of_element_located(self.BOTON_SUBMIT_REVIEW))
        self.rellenar(self.REVIEW_NOMBRE, self.fake.name())
        self.rellenar(self.REVIEW_EMAIL, self.fake.email())
        self.rellenar(self.REVIEW_FIELD, self.fake.paragraph())
        self.screenshot('Review Completa')
        self.wait.until(EC.element_to_be_clickable(self.BOTON_SUBMIT_REVIEW)).click()

    @allure.step("Mensaje Thanks for Review Visible")
    def thanks_review_visible(self):
        texto_thanks_review = self.wait.until(EC.visibility_of_element_located(self.MENSAJE_REVIEW_SUCCESS)).text
        mensaje_esperado = "Thank you for your review."

        with allure.step(f"Verificar que el mensaje es correcto"):
            assert mensaje_esperado == texto_thanks_review, f"Expected: {mensaje_esperado}, Actual: {texto_thanks_review}"
        self.screenshot('Mensaje de Review Completa')