import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import keyboard


driver = webdriver.Chrome()

# Configura abas a serem abertas e automatizadas
# Para adicionar novas abas basta replicar a linha "driver.execute_script("window.open('https://www.urlteste.com');")"

driver.get("https://www.urlteste.com")
driver.execute_script("window.open('https://www.urlteste.com');")
driver.execute_script("window.open('https://www.urlteste.com');")
driver.execute_script("window.open('https://www.urlteste.com');")

handles = driver.window_handles

pause = False

def check_pause():
    return keyboard.is_pressed('ctrl') and keyboard.is_pressed('space')

while True:
    for handle in handles:
        driver.switch_to.window(handle)
        driver.refresh()
        while True:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
            start_time = time.time()
            while time.time() - start_time < 10:
                if check_pause():
                    pause = not pause
                    time.sleep(0.2)
                    break
                if pause:
                    time.sleep(0.1)
                    continue
                time.sleep(0.1)
            if pause:
                continue
            break
    if pause:
        break

driver.quit()
