# -*- coding: utf-8 -*-
""" extract_baamps.py

This module extracts experiments data from BaAMPs website and store this data
in a csv file. The BaAMPS is a database dedicated to antimicrobial peptides
 (AMPs) specifically tested against microbial biofilms.

How to run:
        $ python extract_baamps.py
"""

# Standard Library imports
import sys

# Local imports
from commons.set_url import set_url
from commons.chrome_driver import get_driver
from commons.write_csv import write_csv
from baamps.experiments import get_basics

# Constants
URL = 'http://www.baamps.it/experimentlist'
EXPERIMENTS_FILE = 'experiments.csv'
EXPERIMENTS_TITLE = ['id', 'peptide', 'administration', 'microorganism',
                     'activity', 'method', 'amp effect', 'concentration',
                     'notes']


# main
def main(url, title, file):

    driver = get_driver()

    set_url(driver, url)

    experiments = get_basics(driver)

    write_csv(file, title, experiments)

    return


if __name__ == '__main__':
    main(URL, EXPERIMENTS_TITLE, EXPERIMENTS_FILE)
    sys.exit(0)
