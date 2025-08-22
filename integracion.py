from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def initialize_driver():  
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
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
    print("login ok")


def ir_a_PIM(driver):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//span[text()="PIM"]'))
    ).click()
    print("entrando a PIM")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//h5[text()="Employee Information"]'))
    )

             



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

