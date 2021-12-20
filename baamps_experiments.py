# -*- coding: utf-8 -*-
""" baamps_experiment.py

This module scrapes experiments data from BaAMPs website and store this data in
a csv file. The BaAMPS is a database dedicated to antimicrobial peptides (AMPs)
specifically tested against microbial biofilms.

How to run:
        $ python baamps_experiments.py
"""
from selenium.common.exceptions import TimeoutException
from chrome_driver import get_driver
from experiments import get_experiments
from write_csv import write_csv
import sys
import time

URL = 'http://www.baamps.it/experimentlist'
BAAMPS_FILE = 'BaAMPs.csv'
EXPERIMENTS_TITLE = ['id', 'peptide', 'administration', 'microorganism',
                     'activity']


def set_url(d, url):
    try:
        d.get(URL)
        time.sleep(2)
    except TimeoutException as ex:
        print('Timeout getting URL', ex)
        sys.exit(1)
    return


def main(url, baamps_file):

    driver = get_driver()

    set_url(driver, url)

    experiments = get_experiments(driver)

    write_csv(baamps_file, EXPERIMENTS_TITLE, experiments)

    return

#
# main


if __name__ == '__main__':
    main(URL, BAAMPS_FILE)
    sys.exit(0)
