from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def Ingresar():
    driver=webdriver.Chrome()
    driver.get("https://www.netflix.com/login")
    time.sleep(5)

    correo=driver.find_element(By.ID,":r0:")
    correo.send_keys("asjkaksjaks@dksfkdskkfds")
    
    contraseña=driver.find_element(By.NAME,"password")
    contraseña.send_keys("2345678")

    btn_ingresar=driver.find_element(By.CLASS_NAME,"e1ax5wel2")
    btn_ingresar.click()
    time.sleep(5)
    driver.quit()
Ingresar()


def Recuperación_cuenta():
    driver=webdriver.Chrome()
    driver.get("https://www.netflix.com/login")
    time.sleep(5)

    perdida_contraseña=driver.find_element(By.PARTIAL_LINK_TEXT,"¿Olvidaste")
    perdida_contraseña.click()

    correo_respaldo=driver.find_element(By.ID,"forgot_password_input")
    correo_respaldo.send_keys("asjkaksjaks@dksfkdskkfds")

    Btn_restablecer=driver.find_element(By.CLASS_NAME,"forgot-password-action-button")
    Btn_restablecer.click()
    time.sleep(5)
    driver.quit()
Recuperación_cuenta()

def Chropath():
    driver=webdriver.Chrome()
    driver.get("https://www.netflix.com/login")
    time.sleep(5)

    correo=driver.find_element(By.XPATH,"//input[@id=':r0:']")
    correo.send_keys("asjkaksjaks@dksfkdskkfds")
    
    contraseña=driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/div[1]/input[1]")
    contraseña.send_keys("2345678")

    btn_ingresar=driver.find_element(By.CSS_SELECTOR,"div.default-ltr-cache-k55181.eoi9e9o1 div.default-ltr-cache-8hdzfz.eoi9e9o0:nth-child(3) div.default-ltr-cache-1osrymp.e1puclvk0 form.e13lzdkk1.default-ltr-cache-9beyap > button.e1ax5wel2.ew97par0.default-ltr-cache-1aba556-PressableButton-StyledPressable-StyledPressable.e1ff4m3w2:nth-child(3)")
    btn_ingresar.click()
    time.sleep(5)
    driver.quit()    

Chropath()



    





