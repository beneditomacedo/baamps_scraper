from selenium import webdriver
from selenium.webdriver.chrome.options import Options

DRIVER_PATH='/usr/local/bin/chromedriver'

options = Options()
options.headless = True
options.add_argument("--windows-size=1920,1200")
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

target = 'http://www.baamps.it/experimentlist'

driver.get(target)
print(driver.title)
print(driver.current_url)