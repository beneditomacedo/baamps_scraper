from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from commons.set_url import set_url


def get_basics(driver):

    #
    # select all experiments
    #
    select_element = driver.find_element(By.ID, 'limit')
    select_object = Select(select_element)
    select_object.select_by_value('0')

    #
    # get all rows which contains one experiment for row
    #
    rows = driver.find_elements_by_class_name('row0')

    experiments = []
    for r in rows:
        elements = r.find_elements(By.TAG_NAME, 'td')
        experiments.append(get_experiment(elements))

    full_experiments = []

    for e in experiments:
        details = get_details(driver, e[0])

        for d in details:
            full_experiments.append(e+d)

    return full_experiments


def get_experiment(elements):
    experiment = []

    for e in elements:
        experiment.append(e.text)

    experiment[1] = experiment[1].replace("\n", "")
    experiment[4] = experiment[4].replace("\n", " ")

    return experiment


def get_details(d, id):

    URL = 'http://www.baamps.it/experimentlist?task=experiment.display&ID='

    url = URL + id

    set_url(d, url)

    details = []

    rows = d.find_elements_by_class_name('row00')

    for r in rows:
        elements = r.find_elements(By.TAG_NAME, 'td')
        details.append(get_detail(elements))

    rows = d.find_elements_by_class_name('row01')

    for r in rows:
        elements = r.find_elements(By.TAG_NAME, 'td')
        details.append(get_detail(elements))

    return details


def get_detail(elements):
    detail = []

    for e in elements:
        detail.append(e.text)

    return detail
