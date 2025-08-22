from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

def clic_en_boton():
    # Ya no necesitas WebDriverManager en el CI,
    # el controlador se gestiona en el archivo .yml
    # service = Service(ChromeDriverManager().install())
    
    # El controlador de Chrome ya está en el PATH del sistema
    # gracias a la configuración de GitHub Actions.
    driver = webdriver.Chrome()

    # Abre una página con al menos un botón para hacer clic
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    boton = driver.find_element(By.CSS_SELECTOR, "button")
    boton.click()
    
    time.sleep(3)
    driver.quit()


if __name__ == "__main__":
    clic_en_boton()

