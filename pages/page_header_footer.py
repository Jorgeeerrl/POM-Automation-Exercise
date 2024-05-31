import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait


class PageHeaderFooter():

    BOTON_LOGO = ('xpath', "//img[@src='/static/images/home/logo.png']")
    BOTON_HOME_HEADER = ('xpath', "//a[@href='/'][contains(.,'Home')]")
    BOTON_PRODUCTS_HEADER = ('xpath', "//a[@href='/products']")
    BOTON_CART_HEADER = ('xpath', "(//a[contains(@href,'cart')])[1]")
    BOTON_REGISTRO_LOGIN_HEADER = ('xpath', "//a[@href='/login']")
    BOTON_CONTACTO_HEADER = ('xpath', "//a[@href='/contact_us']")
    BOTON_LOGOUT_HEADER = ('xpath', '//a[contains(text(), " Logout")]')
    BOTON_DELETE_ACCOUNT_HEADER = ('xpath', '//a[contains(text(), " Delete Account")]')
    BOTON_TEST_CASES_HEADER = ('xpath', "(//a[contains(.,'Test Cases')])[1]")
    HEADER = ("css selector", ".nav.navbar-nav")
    USERNAME_FIELD = ("xpath", "//input[@name='username']")
    USER_STATUS = ('xpath', '//a[contains(text(), "Logged in as")]')

    iFRAME_PUBLI = ('xpath', '//*[@id="ad_iframe"]')
    FULL_FRAME_PUBLI = ('xpath', '//div[@id="ad_position_box"]')
    BOTON_CERRAR_PUBLI = ('css selector', 'div#dismiss-button')
    PUBLI_ACTIVA = ('css selector', 'ins.adsbygoogle[data-ad-status="filled"][data-vignette-loaded="true"]')
    iFRAME_PUBLI_ACTIVO = ('css selector', 'ins.adsbygoogle[data-ad-status="filled"][data-vignette-loaded="true"] iframe')
    iFRAME_PUBLI_ANIDADO_ACTIVO = ('css selector', 'iframe#ad_iframe[title="Advertisement"]')


    def check_and_close_publi(self):
        try:
            iframe_publi = self.driver.find_element(*self.iFRAME_PUBLI_ACTIVO)
            if iframe_publi.is_displayed():
                with allure.step("Cerrar Publicidad"):
                    self.driver.switch_to.frame(iframe_publi)
    
                    try:
                        boton_cerrar_publi = self.driver.find_element(*self.BOTON_CERRAR_PUBLI)
                        boton_cerrar_publi.click()
                    except NoSuchElementException:
                        # Si el botóm cerrar anuncio no está en el iframe, cambia al iframe anidado porsia
                        iframe_publi_anidado = self.driver.find_element(*self.iFRAME_PUBLI_ANIDADO_ACTIVO)
                        self.driver.switch_to.frame(iframe_publi_anidado)
                        boton_cerrar_publi_anidado = self.driver.find_element(*self.BOTON_CERRAR_PUBLI)
                        boton_cerrar_publi_anidado.click()
                        self.driver.switch_to.parent_frame()
    
                    self.driver.switch_to.default_content()
                    allure.attach("Publicidad Cerrada", name="Estado de la Publicidad", attachment_type=allure.attachment_type.TEXT)
        except NoSuchElementException:
            pass


        try:
            wait = WebDriverWait(self.driver, 0.3)
            cookie_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div[1]/div[2]/div[2]/button[1]/p")))
            cookie_button.click()
            print("Pop-up de cookies cerrado.")
        except TimeoutException:
            return("No se encontró el pop-up de cookies.")

    @allure.step("Click Botón Signup/Login")
    def click_boton_login_registro(self):
        self.wait.until(EC.element_to_be_clickable(self.BOTON_REGISTRO_LOGIN_HEADER)).click()
        self.check_and_close_publi()

    @allure.step("Username Visible")
    def user_name_visible(self):
        self.wait.until(EC.visibility_of_element_located(self.BOTON_LOGOUT_HEADER))      
        self.wait.until(EC.visibility_of_element_located(self.BOTON_DELETE_ACCOUNT_HEADER)) 

    @allure.step("Click Botón Delete Account")
    def click_boton_delete_account(self):
        self.wait.until(EC.visibility_of_element_located(self.BOTON_DELETE_ACCOUNT_HEADER))
        self.wait.until(EC.element_to_be_clickable(self.BOTON_DELETE_ACCOUNT_HEADER)).click()
        self.check_and_close_publi()

    @allure.step("Click Botón Logout")
    def click_boton_logout(self):
        self.wait.until(EC.element_to_be_clickable(self.BOTON_LOGOUT_HEADER)).click()
        self.check_and_close_publi()

    @allure.step("Header Visible")
    def header_visible(self):
        if "#google_vignette" in self.driver.current_url:
            self.check_and_close_publi()
        self.wait.until(EC.visibility_of_element_located(self.HEADER))

    @allure.step("Click Botón Contact Us")
    def click_boton_contacto(self):
        self.wait.until(EC.element_to_be_clickable(self.BOTON_CONTACTO_HEADER)).click()
        self.check_and_close_publi()

    @allure.step("Click Botón Test Cases")
    def click_boton_test_cases(self):
        self.wait.until(EC.element_to_be_clickable(self.BOTON_TEST_CASES_HEADER)).click()
        self.check_and_close_publi()

    @allure.step("Click Botón Products")
    def click_boton_products(self):
        self.wait.until(EC.element_to_be_clickable(self.BOTON_PRODUCTS_HEADER)).click()
        self.check_and_close_publi()