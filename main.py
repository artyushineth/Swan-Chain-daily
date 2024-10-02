from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import pyautogui
import requests
import time

with open('id.txt', 'r') as file:
    user_ids = [line.strip() for line in file.readlines()]

for user_id in user_ids:
    try:
        open_url = f"http://local.adspower.net:50325/api/v1/browser/start?user_id={user_id}"
        close_url = f"http://local.adspower.net:50325/api/v1/browser/stop?user_id={user_id}"

        resp = requests.get(open_url).json()

        chrome_driver = resp["data"]["webdriver"]
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", resp["data"]["ws"]["selenium"])
        chrome_options.add_argument("window-size=1200,720")

        service = Service(executable_path=chrome_driver)
        driver = webdriver.Chrome(service=service, options=chrome_options)

        time.sleep(3)
        driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#unlock')
        time.sleep(6)
        password_field = driver.find_element(By.XPATH, '//*[@id="password"]')
        password_field.send_keys('qwerty1234')
        time.sleep(1)
        continue_button = driver.find_element(By.XPATH, '//button[contains(text(), "Разблокировать")]')
        continue_button.click()
        driver.get('https://mission.swanchain.io/')
        time.sleep(10)
        driver.find_element(by=By.XPATH, value='//*[@id="tab-OnchainMission"]').click()
        time.sleep(3)
        driver.find_element(by=By.XPATH, value='//*[@id="el-collapse-head-8"]/div/div/div[3]').click()
        time.sleep(10)
        driver.switch_to.new_window('window')
        time.sleep(2)
        driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#unlock')
        time.sleep(3)
        driver.find_element(by=By.XPATH, value='//*[@id="app-content"]/div/div[3]/div/div/div[3]/button[2]').click()
        time.sleep(5)

        driver.get('https://mission.swanchain.io/')
        time.sleep(5)
        driver.find_element(by=By.XPATH, value='//*[@id="tab-OnchainMission"]').click()
        time.sleep(3)
        driver.find_element(by=By.XPATH, value='//*[@id="el-collapse-head-9"]/div').click()
        time.sleep(3)
        driver.find_element(by=By.XPATH, value='//*[@id="el-collapse-content-9"]/div/div/span/span/span').click()
        time.sleep(3)

        window_size = driver.get_window_size()
        window_width = window_size['width']
        window_height = window_size['height']
        x_click = 800
        y_click = 480

        time.sleep(1)
        pyautogui.click(x_click, y_click)

        time.sleep(10)
        driver.switch_to.new_window('window')
        time.sleep(2)
        driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#unlock')
        time.sleep(3)
        driver.find_element(by=By.XPATH, value='//*[@id="app-content"]/div/div[3]/div/div/div[3]/button[2]').click()
        time.sleep(5)
        driver.get('https://mission.swanchain.io/')
        time.sleep(5)
        driver.find_element(by=By.XPATH, value='//*[@id="tab-OnchainMission"]').click()
        time.sleep(3)
        driver.find_element(by=By.XPATH, value='//*[@id="el-collapse-head-9"]/div').click()
        time.sleep(3)
        driver.find_element(by=By.XPATH, value='//*[@id="el-collapse-head-9"]/div/div/div[3]').click()
        time.sleep(10)

        resp = requests.get(close_url).json()
        print(f"Завершили работу для user_id: {user_id}")

    except Exception as e:
        print(f"Ошибка при работе с user_id {user_id}: {str(e)}")
        requests.get(close_url).json()
