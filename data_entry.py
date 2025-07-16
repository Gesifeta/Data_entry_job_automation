from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC

from url import google_form_url,zillow_url
import time

class DataEntry:
    def __init__(self):
        self.service = Service(executable_path="chromedriver.exe")
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(service=self.service, options=self.options)
        self.browser.get(google_form_url)
        self.browser.maximize_window()
        self.wait = WebDriverWait(self.browser, 10)
        time.sleep(10)
    def submit_form(self,address,info,link):
        self.form_elements = self.browser.find_elements(By.CLASS_NAME,"zHQkBf")
        for num in range(len(address)):
            self.form_elements[0].send_keys(address[num])
            self.form_elements[1].send_keys(info[num])
            self.form_elements[2].send_keys(link[num])
            time.sleep(10)
            self.browser.find_element(By.CLASS_NAME,"CeoRYc").click()
            time.sleep(5)
            self.browser.find_element(By.CLASS_NAME,"c2gzEf").click()




