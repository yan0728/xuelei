import time
from selenium import webdriver
from selenium.webdriver.support.select import Select


# 驱动文件路径
driverfile_path = r'E:\python372\chromedriver.exe'
browser = webdriver.Chrome(executable_path=driverfile_path) # 声明浏览器
base_url = 'http://dk.asset.jc3.jieyue.com/loan/user/home'
browser.maximize_window()
browser.get(base_url) # 访问网页
# 登录
browser.find_element_by_id("username").send_keys("10033493")
browser.find_element_by_id("pwd").send_keys("Cs654321")
browser.find_element_by_class_name("btn").click()

# 开始质检
time.sleep(5)
browser.find_element_by_xpath(".//*[text()='进件管理']").click()
time.sleep(5)
browser.find_element_by_xpath("//span[text()=' 交叉质检']").click()
time.sleep(5)

for i in range(20):
    print("开始质检第{}次".format(i+1))
    browser.switch_to.default_content() #跳出frame
    browser.switch_to.frame(browser.find_element_by_xpath("//iframe[contains(@src,'queryEachCheckLbTIntoInfo')]"))
    time.sleep(3)
    # 点击第一行
    btns = browser.find_elements_by_tag_name("td")
    i = 0
    while (i < len(btns) and btns[i].text !='1'):
        i = i + 1
    btns[i].click()
    browser.find_element_by_xpath("//a[text()='质检']").click()
    time.sleep(3)
    browser.switch_to.default_content()
    browser.switch_to.frame(browser.find_element_by_xpath("//iframe[contains(@src,'/loan/lbTIntoInfo/prepareExecute/eachCheckLbTIntoInfo?id=')]"))
    browser.find_element_by_id("remark").send_keys("say something...")
    Select(browser.find_element_by_id("eachCheckResultCode")).select_by_value("10")
    time.sleep(5)
    browser.find_element_by_id("doSubmitInto").click()
    time.sleep(5)

    if i == 1:
        break

browser.close() # 关闭浏览器
print("质检通过完成")