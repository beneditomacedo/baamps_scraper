from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

DRIVER_PATH = '/usr/local/bin/chromedriver'

options = Options()
options.headless = True
options.add_argument("--windows-size=1920,1200")
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

URL = 'http://www.baamps.it/experimentlist'

driver.get(URL)

rows = driver.find_elements_by_class_name('row0')

firstLine = rows[0]

elements = firstLine.find_elements(By.TAG_NAME, 'td')


def get_experiment(elements):
    experiment = []
    for e in elements:
        experiment.append(e.text)
    return experiment


print(get_experiment(elements))
