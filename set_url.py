from selenium.common.exceptions import TimeoutException
import sys
import time


def set_url(d, url):
    try:
        d.get(url)
        time.sleep(2)
    except TimeoutException as ex:
        print('Timeout getting URL', ex)
        sys.exit(1)
    return
