import allure
from allure_commons.types import AttachmentType
from faker import Faker
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from utils.generador_datos import Datos
from .page_header_footer import PageHeaderFooter


class PageBase(PageHeaderFooter):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15, poll_frequency=1)
        self.fake = Faker()
        self.datos = Datos()

    def abrir_pagina(self):
        with allure.step(f"Abrir página {self.PAGE_URL} "):
            self.driver.get(self.PAGE_URL)
        self.check_and_close_publi()

    def pagina_abierta(self):
        try:
            with allure.step(f"Página {self.PAGE_URL} abierta"):
                if "#google_vignette" in self.driver.current_url:
                    self.check_and_close_publi()
                else:
                    self.wait.until_not(EC.visibility_of_element_located(self.iFRAME_PUBLI))
                    self.wait.until(EC.url_to_be(self.PAGE_URL))             
        except Exception as e:
            current_url = self.driver.current_url
            self.screenshot("Página abierta")
            allure.attach(f"Test fallado. Exception: {str(e)}. Current URL: {current_url}", name="Detalles Fallos", attachment_type=allure.attachment_type.TEXT)
            raise  

    @allure.step("Verificar texto del status del usuario")
    def user_status_ok(self):
        nombre_usuario = self.datos.nombre_login
        user_status = self.wait.until(EC.visibility_of_element_located(self.USER_STATUS))
        texto_user_status = user_status.text
        user_status_esperado = f'Logged in as {nombre_usuario}'

        with allure.step(f"Verificar que el texto del status es correcto para el usuario {nombre_usuario}"):
            assert texto_user_status == user_status_esperado, f"Expected: {user_status_esperado}, Actual: {texto_user_status}"

    def screenshot(self, nombre_screenshot):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=nombre_screenshot,
            attachment_type=AttachmentType.PNG
        )

    @allure.step("Rellenar con value: {value}")
    def rellenar(self, locator, value):
        field = self.wait.until(EC.visibility_of_element_located(locator))
        field.clear()
        field.send_keys(value)

    @allure.step("Seleccionar opción con value: {texto_opcion}")
    def seleccionar_opcion(self, locator_select, texto_opcion):
        seleccionar_opcion = self.wait.until(EC.visibility_of_element_located(locator_select))
        opcion = Select(seleccionar_opcion)
        try:
            opcion.select_by_visible_text(texto_opcion)
        except NoSuchElementException:
            # If not found by visible text, try selecting by value
            opcion.select_by_value(texto_opcion)

    def seleccionar_sexo(self, locator_sexo):
        boton_sexo = self.wait.until(EC.presence_of_element_located(locator_sexo))
        boton_sexo.click()

    def seleccionar_checkbox(self, locator_checkbox):
        checkbox = self.wait.until(EC.element_to_be_clickable(locator_checkbox))
        if not checkbox.is_selected():
            checkbox.click()

    def eliminar_checkbox(self, locator_checkbox):
        checkbox = self.wait.until(EC.element_to_be_clickable(locator_checkbox))
        if checkbox.is_selected():
            checkbox.click()

    @allure.step("Scroll hasta ver elemento")
    def scroll_into_view(self, locator_elemento):
        elemento = self.wait.until(EC.presence_of_element_located(locator_elemento))
        self.driver.execute_script("arguments[0].scrollIntoView();", elemento)

    @allure.step("Scroll abajo hasta el final")
    def scroll_abajo(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.END).perform()

    @allure.step("Mover puntero sobre el elemento")
    def hover(self, locator_elemento):
        elemento = self.wait.until(EC.presence_of_element_located(locator_elemento))
        actions = ActionChains(self.driver)
        actions.move_to_element(elemento).perform()

    def capturar_texto_elementos(self, locator):
        elementos = self.wait.until(EC.presence_of_all_elements_located(locator))
        return [element.text for element in elementos]