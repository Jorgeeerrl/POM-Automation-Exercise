import allure
from .page_base import PageBase
from utils.urls import Urls
from selenium.webdriver.support import expected_conditions as EC


class PageTestCases(PageBase):
    PAGE_URL = Urls.PAGE_TEST_CASES

    TEST_CASES = ("css selector", ".panel-group h4")

    @allure.step("Test cases visibles")
    def testcases_visible(self):
        self.wait.until(EC.visibility_of_all_elements_located(self.TEST_CASES))
