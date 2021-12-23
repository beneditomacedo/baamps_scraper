from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from experiment import get_experiment
from experiment_details import get_details


def get_experiments(driver):

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
