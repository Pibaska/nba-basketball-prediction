from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
import os


def Driver_Firefox():
    firefox_options = Options().headless
    gecko_driver = webdriver.Firefox(
        firefox_binary=FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe') if os.name == 'nt'
        else '/bin/firefox',
        executable_path=os.path.join(os.getcwd(), "geckodriver"))
    return gecko_driver, firefox_options
