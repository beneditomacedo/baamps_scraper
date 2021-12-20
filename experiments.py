from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from experiment import get_experiment


def get_experiments(d):

    #
    # select all experiments
    #
    select_element = d.find_element(By.ID, 'limit')
    select_object = Select(select_element)
    select_object.select_by_value('0')

    #
    # get all rows which contains one experiment for row
    #
    rows = d.find_elements_by_class_name('row0')

    experiments = []
    for r in rows:
        elements = r.find_elements(By.TAG_NAME, 'td')
        experiments.append(get_experiment(elements))

    return experiments
