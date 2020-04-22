import os
import time
import urllib
import requests
from selenium import webdriver
from os.path import dirname, abspath, join
from .util.write_csv import write_csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


ROOT_PATH = dirname(abspath(__file__))


class FlourishWebGenerator:

    def __init__(self, source_path=join(ROOT_PATH, 'file_upload')):
        self.driver = None
        self.source_path = source_path

    def create_driver(self, account, password, full_screen=False):

        options = webdriver.ChromeOptions()
        # 全螢幕設定
        if full_screen:
            options.add_argument('--kiosk')
        # remove 自動測試的 bar
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        # remove 記帳號密碼的框框
        prefs = {"": ""}
        prefs["credentials_enable_service"] = False
        prefs["profile.password_manager_enabled"] = False
        options.add_experimental_option("prefs", prefs)

        # 開啟 Chrome
        driver = webdriver.Chrome(join(ROOT_PATH, 'chrome_driver\chromedriver.exe'),
                                  chrome_options=options)  # Optional argument, if not specified will search path.

        # Log in flourish
        login_url = 'https://app.flourish.studio/projects'
        driver.get(login_url)
        driver.find_element_by_xpath("//*[@name='email']").send_keys(str(account))
        driver.find_element_by_xpath("//*[@name='password']").send_keys(str(password))
        driver.find_element_by_xpath("//*[@value='Log in']").click()

        self.driver = driver

    def upload_to_flourish(self, flourish_id, upload_file_name, data_beg_alphabet, data_end_alphabet):

        # 進到放 data 的頁面
        driver = self.driver
        page_url = f"https://app.flourish.studio/visualisation/{flourish_id}/edit"
        driver.get(page_url)
        driver.find_element_by_xpath("//*[@name='show-pane' and @value='data']").click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((
            By.XPATH, "//*[@class='btn action' and @ data-action='add-data']")))
        # 放入 data 先點上傳 然後用 autoit 選上傳資料
        driver.find_element_by_xpath("//*[@class='btn action' and @ data-action='add-data']").click()

        upload_file_path = join(self.source_path, upload_file_name)
        write_csv(ROOT_PATH, 'file_path.csv', {0: [upload_file_path]})

        os.system(join(ROOT_PATH, 'load_csv_then_upload_file.exe'))

        # 點 import publicly
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((
            By.XPATH, "//*[@class='btn primary']")))
        driver.find_element_by_xpath("//*[@class='btn primary']").click()
        # 點一個咚咚
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((
            By.XPATH, "//div[@class='btn']")))
        driver.find_element_by_xpath("//div[@class='btn']").click()

        # 輸入 data 的 columns range, 先清除再填入資料
        driver.find_element_by_xpath("//input[@name='data-values']").clear()
        value_columns = data_beg_alphabet + '-' + data_end_alphabet
        driver.find_element_by_xpath("//input[@name='data-values']").send_keys(value_columns)

        # 點 preview 確保資料有進去
        driver.find_element_by_xpath("//*[@name='show-pane' and @value='preview']").click()

        time.sleep(3)

        # 進到超大頁面取得網址
        preview_url = f"https://app.flourish.studio/visualisation/{flourish_id}/preview"

        # 取得網址
        driver.get(preview_url)

        # 把網頁載下來，載下來不包含 css ，但好像都共用 所以沒問題 , encoding="utf-8"
        current_url = driver.current_url

        return current_url

    def open_local_web(self, web_name):

        driver = self.driver
        # 打開 local 儲存的檔案
        local_url = join(ROOT_PATH, f'web_download\\{web_name}.html')
        driver.get(local_url)

    @staticmethod
    def download_web(url, web_name):
        res = requests.get(url)
        with open(join(ROOT_PATH, f'web_download\\{web_name}.html'), 'wb') as html_file:
            html_file.write(res.content)

    def close(self):
        self.driver.quit()

