import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
import random

# 驱动文件路径
driverfile_path = r'E:\python372\chromedriver.exe'
browser = webdriver.Chrome() # 声明浏览器
base_url = 'http://audit.risk.jc1.jieyue.com'
browser.maximize_window()
browser.get(base_url) # 访问网页

# 登录
def login():
    browser.find_element_by_id("username").send_keys("admin")
    browser.find_element_by_id("password").send_keys("Cs654321")
    browser.find_element_by_xpath("//form[@class = 'ant-form ant-form-horizontal']/div[3]/div/div/span").click()
    print("1-1：登录成功")

#快搜
def TakeNumber():
    browser.find_element_by_xpath("//div[@class = 'syscl-pro-components-top-nav-header-index-left']/div[2]/div/div/ul/li/div")






if __name__ == '__main__':
    login()
    TakeNumber()