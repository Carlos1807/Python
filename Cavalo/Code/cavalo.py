import time
import winsound


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import os


class ChromeAuto:
    def __init__(self, path):
        self.driver_path = Service("driver/chromedriver.exe")
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('user-data-dir=' + path)
        self.chrome = webdriver.Chrome(
            service=self.driver_path,
            options=self.options
        )

    def acessa(self, site):
        self.chrome.get(site)

    def sair(self):
        self.chrome.quit()

    def clica_all(self):
        botao = self.chrome.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[2]'
                                                   '/div/div/div[1]/div/div/ul/li[1]')
        botao.click()

    def clica_share_profit(self):
        botao1 = self.chrome.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div'
                                                   '/div/div[1]/div/div/ul/li[3]')
        botao1.click()
        time.sleep(1)
        if len(self.chrome.find_elements(By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div/div/div[2]'
                                                   '/div/div/div[2]/div')) > 0:

            print("achou")
            winsound.Beep(440, 200)
            botao = self.chrome.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div/div'
                                                       '/div[2]/div/div/div[2]/div')
            botao.click()

            time.sleep(1)
            botao_rent = self.chrome.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[3]/div[2]/div/div[2]')
            botao_rent.click()

            return 0
        return 1


if __name__ == '__main__':

    caminho = os.getenv('LOCALAPPDATA')
    caminho = caminho.replace('\\', '/')
    caminho += '/Google/Chrome/User Data'
    chrome = ChromeAuto(caminho)

    chrome.acessa('https://play.pegaxy.io/renting?tab=all')
    time.sleep(1)
    while(True):
        if(chrome.clica_share_profit() == 0):
            break
        chrome.clica_all()

