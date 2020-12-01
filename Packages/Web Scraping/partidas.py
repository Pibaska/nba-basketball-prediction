from .DriverFirefox import Driver_Firefox
from bs4 import BeautifulSoup
import time


def Partidas():
    gecko_driver, firefox_options = Driver_Firefox()

    url = "https://www.basketball-reference.com/boxscores/?month=5&day=3&year=2019"

    gecko_driver.get(url)

    time.sleep(3)

    element = gecko_driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]")
    html_content = element.get_attribute('outerHTML')

    html_content.decompose()

    soup = BeautifulSoup(html_content, 'html.parser')
    gecko_driver.quit()  # fechar o navegador

    return soup, html_content[0]
