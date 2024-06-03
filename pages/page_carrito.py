import allure
from .page_base import PageBase
from utils.urls import Urls
from selenium.webdriver.support import expected_conditions as EC


class PageCarrito(PageBase):

    PAGE_URL = Urls.PAGE_CARRITO