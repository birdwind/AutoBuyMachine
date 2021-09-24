from datetime import datetime

import pause as pause
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from xPaths import (
    LOGIN_X_PATHS, BUY_PATHS
)

"""
匯入欲搶購的連結、登入帳號、登入密碼及其他個資
"""
from settings import (
    URL, ACCOUNT, PASSWORD
)

"""
設定 option 可讓 chrome 記住已登入帳戶，成功後可以省去後續"登入帳戶"的程式碼
"""
options = Options()
options.add_argument("--disable-notifications")

desired_capabilities = DesiredCapabilities.CHROME  # 修改页面加载策略
desired_capabilities["pageLoadStrategy"] = "none"  # 注释这两行会导致最后输出结果的延迟，即等待页面加载完成再输出

driver = webdriver.Chrome("./chromedriver", options=options)


def main():
    try:
        login()
    except:
        print('已經登入過或登入失敗')

    start_date_time_string = input("請輸入YYYY/MM/DD hh:mm:ss (24H)設定啟動時間:")
    start_date_time = datetime.strptime(start_date_time_string, "%Y/%m/%d %H:%M:%S")

    pause.until(start_date_time)

    driver.get(URL)
    check_buy_available(BUY_PATHS['buy'])
    click(BUY_PATHS['buy'], True)
    click(BUY_PATHS['confirm'], True)
    click(BUY_PATHS['checkout'], True)
    click(BUY_PATHS['creditCardInstallment'], True)
    click(BUY_PATHS['installmentLast'], True)
    input_value(BUY_PATHS['CCV'], 123)
    # click(BUY_PATHS['confirmCheckout'])


def check_buy_available(xpath):
    while True:
        if driver.find_elements_by_xpath(xpath):
            break
        else:
            driver.refresh()


def click(xpath, is_check):
    if is_check:
        WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable((By.XPATH, xpath)))
    driver.find_element_by_xpath(xpath).click()


def login():
    driver.get('https://m.momoshop.com.tw/mymomo/login.momo')
    WebDriverWait(driver, 2).until(
        expected_conditions.presence_of_element_located((By.XPATH, LOGIN_X_PATHS["account"]))
    )
    input_value(LOGIN_X_PATHS["account"], ACCOUNT)
    input_value(LOGIN_X_PATHS["password"], PASSWORD)
    click(LOGIN_X_PATHS["loginBtn"], True)
    print('成功登入')


def input_value(xpath, value):
    element = driver.find_element_by_xpath(xpath)
    element.clear()
    element.send_keys(value)


if __name__ == "__main__":
    main()
