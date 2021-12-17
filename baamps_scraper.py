from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import csv
import sys

DRIVER_PATH = '/usr/local/bin/chromedriver'
URL = 'http://www.baamps.it/experimentlist'
BAAMPS_FILE = 'BaAMPs.csv'


def get_driver(driver_path):
    options = Options()
    options.headless = True
    options.add_argument("--windows-size=1920,1200")
    driver = webdriver.Chrome(options=options, executable_path=driver_path)
    return driver


def set_url(d, url):
    try:
        d.get(URL)
    except TimeoutException as ex:
        print('Timeout getting URL', ex)
        sys.exit(1)
    return


def sanitizer_strings(s):
    s = s.replace('\n', '')
    s = s.replace('"', '') 
    return s


def get_experiments(d):
    rows = d.find_elements_by_class_name('row0')

    experiments = []
    for r in rows:
        elements = r.find_elements(By.TAG_NAME, 'td')
        experiments.append(get_experiment(elements))

    return experiments


def get_experiment(elements):
    experiment = []

    for e in elements:
        experiment.append(e.text)

    experiment[1] = experiment[1].replace("\n", "")
    experiment[4] = experiment[4].replace("\n", " ")

    return experiment


def write_csv(file, data):

    with open(file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

    return


def main(driver_path, url, baamps_file):

    driver = get_driver(driver_path)

    set_url(driver, url)

    experiments = get_experiments(driver)

    write_csv(baamps_file, experiments)

    return

#
# main


if __name__ == '__main__':
    main(DRIVER_PATH, URL, BAAMPS_FILE)


sys.exit(0)
