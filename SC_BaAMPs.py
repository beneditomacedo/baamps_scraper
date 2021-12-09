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


def get_experiment(elements):
    experiment = []

    for e in elements:
        experiment.append(e.text)

    experiment[4] = experiment[4].replace("\n", " ")

    return experiment


rows = driver.find_elements_by_class_name('row0')

experiments = []
for r in rows:
    elements = r.find_elements(By.TAG_NAME, 'td')
    experiments.append(get_experiment(elements))

print(experiments)
