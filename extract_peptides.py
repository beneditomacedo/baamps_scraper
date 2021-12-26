# -*- coding: utf-8 -*-
""" extract_peptides.py

This module extracts peptides data from BaAMPs website and store this data
in a csv file. The BaAMPS is a database dedicated to antimicrobial peptides
 (AMPs) specifically tested against microbial biofilms.

How to run:
        $ python extract_peptides.py
"""

# Standard Library imports
import sys

# Local imports
from commons.set_url import set_url
from commons.chrome_driver import get_driver
from commons.write_csv import write_csv
from baamps.peptides import get_basics

# Constants
URL = 'http://www.baamps.it/peptidelist'
PEPTIDES_FILE = 'peptides.csv'
PEPTIDES_TITLE = ['id', 'peptide', 'partial sequence', 'source', 'size',
                  'tags', 'netcharge5', 'netcharge7', 'isoelectric point',
                  'molecular weight', 'extinction coefficient',
                  'hydrophobicity (CCS)', 'hydrophobic Mom (CCS)',
                  'full sequence']


# main
def main(url, title, file):

    driver = get_driver()

    set_url(driver, url)

    peptides = get_basics(driver)

    write_csv(file, title, peptides)

    return


if __name__ == '__main__':
    main(URL, PEPTIDES_TITLE, PEPTIDES_FILE)
    sys.exit(0)
