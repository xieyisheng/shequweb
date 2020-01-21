from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.varconfig import chromedriverpath
import time

def browser():
    chrome_options = Options()
    #chrome_options.add_argument('disable-infobars')  # 去除“chrome正受到自动化测试。。。”的弹出提示框
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    chrome_options.add_argument('disable-popup-blocking')  # 禁用弹窗拦截
    #chrome_options.add_argument('headless') 启用静默模式，后台运行
    #可能会有用：禁用下载时的安全提示
    download_dir = "/pathToDownloadDir"
    preferences = {"download.default_directory": download_dir,
                   "directory_upgrade": True,
                   "safebrowsing.enabled": True}
    chrome_options.add_experimental_option("prefs", preferences)
    driver = webdriver.Chrome(executable_path=chromedriverpath, chrome_options=chrome_options)
    return driver

if __name__=='__main__':
    dr=browser()
    dr.get("http://www.baidu.com")
    time.sleep(5)
    dr.quit()