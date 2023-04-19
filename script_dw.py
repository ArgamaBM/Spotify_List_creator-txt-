from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

try:

    # Ruta donde se encuentra el controlador de Edge
    edge_driver_path = "C:/path/to/edge/driver"

    # Crear una instancia del controlador de Edge
    driver = webdriver.Edge(executable_path=edge_driver_path)
    
    # Acceder a la página web
    driver.get("xxxxxxxxxxxxxxx")  #Pagina web de descarga
    time.sleep(7)

    try:
        # Localizar el botón de descarga y hacer clic en él
        download_button = driver.find_element(By.ID,'fullwrapper')
        if download_button != None:
            download_button.click()
            driver.find_element
            time.sleep(10)
    except Exception as e:
        print(f'Error en loc descarga:_ {e}')
                

    # Localizar la textbox y escribir un string
    textbox = driver.find_element(By.ID("buttonSearch"))
    if textbox != None:
        driver.find_element(By.CLASS_NAME,"buttonQuery")
        textbox.send_keys("netsky - Thunder")
        time.sleep(10)

    # Localizar el botón de descarga y hacer clic en él
    download_button = driver.find_element(By.ID,"searchButton")
    if download_button != None:
        download_button.click()
        time.sleep(10)


    # Localizar el botón de descarga y hacer clic en él
    download_button = driver.find_element(By.CLASS_NAME, "trackDownload")
    if download_button != None:
        download_button.click()
        time.sleep(10)

    # Cerrar el controlador de Edge
    #driver.quit()

except Exception as e:
    print(e)