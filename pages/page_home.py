import allure
from .page_base import PageBase
from utils.urls import Urls
from selenium.webdriver.support import expected_conditions as EC

class PageHome(PageBase):

    PAGE_URL= Urls.PAGE_HOME

    @allure.step("Click botón 'View product' by ID")
    def click_boton_view_product_por_id(self, id_producto):
        boton_view = ("xpath", f"//div[@class='choose']//a[@href='/product_details/{id_producto}']")
        self.scroll_into_view(boton_view)
        self.wait.until(EC.element_to_be_clickable(boton_view)).click()
        self.check_and_close_publi()