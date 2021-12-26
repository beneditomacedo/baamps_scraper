from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from commons.set_url import set_url


def get_basics(driver):

    #
    # select all peptides
    #
    select_element = driver.find_element(By.ID, 'limit')
    select_object = Select(select_element)
    select_object.select_by_value('0')

    #
    # get all rows which contains one peptide for row
    #
    rows = driver.find_elements_by_class_name('row0')

    peptides = []
    for r in rows:
        elements = r.find_elements(By.TAG_NAME, 'td')
        temp_peptide = get_peptide(elements)

        tag = r.find_elements(By.TAG_NAME, 'th')[0]
        tag = tag.get_attribute('textContent').strip()

        temp_peptide.append(tag)

        peptides.append(temp_peptide)

    full_peptides = []

    for e in peptides:
        details = get_details(driver, e[0])

        full_peptides.append(e + details)

    return full_peptides


def get_peptide(elements):
    peptide = []

    for e in elements:
        peptide.append(e.get_attribute('textContent').strip())

    return peptide


def get_details(d, id):

    URL = 'http://www.baamps.it/peptidelist?task=peptide.display&ID='

    url = URL + id

    set_url(d, url)

    details = []

    rows = d.find_elements_by_class_name('row0')

    for r in rows:
        value = r.find_element_by_class_name('attrib-value').text
        details.append(value)

    full_sequence = d.find_elements(By.TAG_NAME, 'table')[0]\
                     .find_elements(By.TAG_NAME, 'tr')[2].text.split(' ')[1]

    details.append(full_sequence)

    return details
