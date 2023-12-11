from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_stale_element():
    # Configurar el controlador de Selenium
    option = webdriver.ChromeOptions()

    driver = webdriver.Chrome()

    driver.get("https://dev.to")

    try:
        # Encontrar el elemento por su selector (puedes ajustar esto según tu página web)
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, 'article-link-1694306'))
        )

        # Imprimir el texto del elemento antes de que se vuelva obsoleto
        print('Texto del elemento antes de volverse obsoleto:', element.text)

        # Recargar la página (esto hará que el elemento original se vuelva obsoleto)
        driver.refresh()

        # Intentar interactuar con el elemento obsoleto (debería generar una excepción StaleElementReferenceException)
        print('Texto del elemento después de volverse obsoleto:', element.text)

    except StaleElementReferenceException as e:
        print(f"Error al generar: {type(e).__name__}")

    finally:
        # Cerrar el navegador
        driver.quit()

# Ejecutar la prueba
test_stale_element()
