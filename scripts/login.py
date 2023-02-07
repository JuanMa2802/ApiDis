import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

opc = webdriver.ChromeOptions()

opc.add_argument("--no-sandbox")
opc.add_argument("--disable-dev-shm-usage")
opc.add_argument("--disable-gpu")
opc.add_argument("--disable-blink-features=AutomationControlled")
opc.add_argument("--start-maximized")
# opc.add_argument("--window-size=1920x1080")
opc.add_argument("--enable-features=NetworkService,NetworkServiceInProcess")
opc.add_argument("--ignore-certificate-errors")
opc.add_argument("--allow-running-insecure-content")
opc.add_argument("--disable-notifications")
opc.add_argument("--disable-blink-features")
# opc.add_argument("--incognito")
opc.add_argument('--no-proxy-server')
opc.add_argument("--proxy-server='direct://'")
opc.add_argument("--proxy-bypass-list=*")
opc.add_argument('--disable-dev-shm-usage')
opc.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36")


driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=opc)
action = ActionChains(driver)


driver.get('https://www1.sincoerp.com/SincoArconsa/V3/Marco/Login.aspx')
time.sleep(5)

idPersona = int(sys.argv[1])


print("Hola", idPersona)