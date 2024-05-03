from selenium import webdriver
# importar mas tipos de selenium para buscar elemendos html
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# estas son las opciones para que el navegador no se cierre instantaneamente
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# browser = webdriver.Chrome(options=options)

browser = webdriver.Chrome()
# hacemos que el explorador espere un determinado tiempo en segundos para realizar una accion
browser.implicitly_wait(10)

browser.get("https://github.com")

link = browser.find_element(By.LINK_TEXT, "Sign in")
link.click()

user_input = browser.find_element(By.ID, "login_field")
pass_input = browser.find_element(By.ID, "password")

user_input.send_keys("holamundo")
pass_input.send_keys("holamundo")

pass_input.send_keys(Keys.RETURN)

profile = browser.find_element(
    By.CLASS_NAME,
    "css-truncate.css-truncate-target.ml-1"
)
# obtenemos el valor del elemento html
label = profile.get_attribute("innerHTML")

# preguntamos si se encuentra un elemento que solo se ve cuando el login es correcto
assert "gatitofeliz" in label

# es importante cerrar el explorador cuando finalice la prueba
browser.quit()
