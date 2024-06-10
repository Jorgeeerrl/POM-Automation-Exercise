from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import os


@pytest.fixture(scope="function", autouse=True)
def driver(request):

# Este Fixture se ejecuta automáticamente (autouse=true) antes de cada función de prueba (scope=function).

    options = Options()
    options.add_argument('--headless=new')
    options.add_argument("--start-maximized")
    options.add_argument('--window-size=1920,1080')

    download_folder = os.path.join(os.getcwd(), 'recursos')
    preferences = {"download.default_directory": download_folder}  # Define una preferencia.
    options.add_experimental_option("prefs", preferences)  # Aplica las preferencias definidas.

    driver = webdriver.Chrome(options=options)  # Inicializa una instancia de WebDriver con las opciones definidas.
    request.cls.driver = driver # Asigna el WebDriver a la clase de prueba, permitiendo su uso en los métodos de prueba.
    yield driver
    driver.close()
    driver.quit()