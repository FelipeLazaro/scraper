import time
import os

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from recaptcha import *

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--enable-logging')
options.add_argument('--log-level=0')
options.add_argument('--v=99')
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument("--disable-impl-side-painting")
options.add_argument("--disable-setuid-sandbox")
options.add_argument("--disable-seccomp-filter-sandbox")
options.add_argument("--disable-breakpad")
options.add_argument("--disable-client-side-phishing-detection")
options.add_argument("--disable-cast")
options.add_argument("--disable-cast-streaming-hw-encoding")
options.add_argument("--disable-cloud-import")
options.add_argument("--disable-popup-blocking")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--disable-session-crashed-bubble")
options.add_argument("--disable-ipv6")
options.add_argument("--allow-http-screen-capture")
options.add_argument("--start-maximized")
#options.add_argument('--single-process')
options.add_argument('--data-path=/tmp/data-path')
options.add_argument('--ignore-certificate-errors')
#options.add_argument('--homedir=/tmp')
options.add_argument('--disk-cache-dir=/tmp/cache-dir')
options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
#options.binary_location = os.getcwd() + "/bin/headless-chromium"
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options, executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('http://api.scraperapi.com/?api_key=85212010e6392d4540db44bb197adb2f&url=https://www.gob.mx/curp&render=true');
#driver.get('https://www.gob.mx/curp')
time.sleep(5) 

inputCurp = driver.find_element_by_id("curpinput")
inputCurp.send_keys('LASF871119HDFZNL04')
time.sleep(10) 
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()
driver.switch_to.default_content()
time.sleep(8)
consultarCurp = driver.find_element_by_id("searchButton")
consultarCurp.click()
time.sleep(5)
driver.quit()
