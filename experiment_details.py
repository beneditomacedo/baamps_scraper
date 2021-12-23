from selenium.webdriver.common.by import By
from set_url import set_url
from experiment_detail import get_detail


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
