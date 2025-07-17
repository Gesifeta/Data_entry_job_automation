
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import requests

proxy = 'http://brd-customer-hl_c312bb53-zone-web_unlocker1:@brd.superproxy.io:33335'
proxies = {
    'http': proxy,
    'https': proxy,
}

class Zillow:
    def __init__(self,category,headers, city):
        # self.options = webdriver.ChromeOptions()
        # self.options.add_experimental_option("detach", True)
        # self.service = Service(executable_path= "chromedriver.exe")
        # self.driver = webdriver.Chrome(service=self.service,options=self.options)
        self.response = requests.get(url = f"https://www.zillow.com/{city}/{category}/",
                                     verify = False,
                                     proxies=proxies,)
        self.soup = BeautifulSoup(self.response.text,"html.parser")
        self.rooms = []
        # self.driver.get(f"https://www.zillow.com/{city}/{category}/")
        # self.driver.maximize_window()
        # self.wait = WebDriverWait(self.driver, 10)
        # self.soup = BeautifulSoup(self.driver.page_source, "html.parser")
    def get_data(self):
        self.links = self.soup.find_all(attrs={'class':'property-card-link'})
        self.room_info = self.soup.find_all(attrs={'class':'bcrfLm'})
        self.href =self.soup.find_all(attrs={'class':'property-card-data'})
        self.address= []
        self.info = []
        self.hrefs= []
        for room in self.room_info:
            self.info.append(room.text)

        for link in self.links:
            self.hrefs.append(link.get('href'))
            self.address.append(link.text)











