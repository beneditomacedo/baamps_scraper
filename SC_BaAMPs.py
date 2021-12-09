from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import csv
import sys

DRIVER_PATH = '/usr/local/bin/chromedriver'
URL = 'http://www.baamps.it/experimentlist'
BAAMPS_FILE = 'BaAMPs.csv'

options = Options()
options.headless = True
options.add_argument("--windows-size=1920,1200")
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)



try:
    driver.get(URL)
except TimeoutException as ex:
    print('Timeout getting URL', ex)
    sys.exit(1)


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

with open(BAAMPS_FILE, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(experiments)

sys.exit(0)
