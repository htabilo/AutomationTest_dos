from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def clic_en_boton():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # Abre una página con al menos un botón para hacer clic
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    boton = driver.find_element(By.CSS_SELECTOR, "button")
    boton.click()
    
    time.sleep(3)
    driver.quit()



if __name__ == "__main__":
    clic_en_boton()

