import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Agregado para Edge
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# URL base de la app web (ajustar si es necesario)
BASE_URL = "http://localhost:8000"

@pytest.fixture(scope="module")
def browser():
    edge_options = Options()
    edge_options.add_argument("--headless")
    service = EdgeService(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service, options=edge_options)
    yield driver
    driver.quit()

def test_get_movimientos_form(browser):
    browser.get(f"{BASE_URL}/web/movimientos/nuevo")
    # Acepta cualquiera de los textos principales del formulario
    assert (
        "Registrar Movimiento" in browser.page_source
        or "Nuevo movimiento" in browser.page_source
        or "Registrar" in browser.page_source
    )
    assert browser.find_element(By.NAME, "producto_id")
    assert browser.find_element(By.NAME, "cantidad")
    assert browser.find_element(By.NAME, "tipo")

def test_post_movimiento_form(browser):
    browser.get(f"{BASE_URL}/web/movimientos/nuevo")
    browser.find_element(By.NAME, "producto_id").send_keys("1")
    browser.find_element(By.NAME, "deposito_origen_id").send_keys("1")
    browser.find_element(By.NAME, "deposito_destino_id").send_keys("1")
    browser.find_element(By.NAME, "usuario_id").send_keys("1")
    browser.find_element(By.NAME, "cantidad").send_keys("2")
    browser.find_element(By.NAME, "tipo").send_keys("ingreso")
    browser.find_element(By.TAG_NAME, "form").submit()
    time.sleep(1)
    # Verifica que redirige al listado de productos o muestra mensaje de éxito
    assert (
        "Listado de Productos" in browser.page_source
        or "productos" in browser.title.lower()
        or "exitoso" in browser.page_source.lower()
    )