from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def initialize_driver():  
    options = Options()
    options.add_argument("--headless=new")   # modo headless moderno
    options.add_argument("--no-sandbox")     # necesario en contenedores
    options.add_argument("--disable-dev-shm-usage") # evita problemas de memoria compartida
    options.add_argument("--disable-gpu")    # seguridad extra
    options.add_argument("--window-size=1920,1080") # simula pantalla grande

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver     


def login(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
        )
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
    WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))
    print("✅ Login OK")


def ir_a_PIM(driver):
    # Esperar hasta que la URL contenga "dashboard"
    WebDriverWait(driver, 20).until(EC.url_contains("dashboard"))

    # Esperar a que el módulo PIM esté presente
    pim_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//span[text()="PIM"]'))
    )
    
    # Asegurar que el elemento sea visible y hacer scroll si es necesario
    driver.execute_script("arguments[0].scrollIntoView(true);", pim_element)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="PIM"]')))
    pim_element.click()
    print("✅ Entrando al módulo PIM")

    # Esperar hasta que el encabezado de Employee Information aparezca
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//h5[text()="Employee Information"]'))
    )
    print("✅ Employee Information cargado")



def main():  
    driver = initialize_driver()
    try:
        login(driver)
        ir_a_PIM(driver)
        time.sleep(3)
    finally:
        driver.quit()

if __name__ == '__main__':  
    main()