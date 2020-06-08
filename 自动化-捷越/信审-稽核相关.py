import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

# 驱动文件路径
driverfile_path = r'E:\python372\chromedriver.exe'
browser = webdriver.Chrome() # 声明浏览器
base_url = 'http://credit.risk.jc4.jieyue.com/loan-credit/user/home'
browser.maximize_window()
browser.get(base_url) # 访问网页

# 登录
def login():
    browser.find_element_by_id("username").send_keys("admin")
    browser.find_element_by_id("pwd").send_keys("Cs654321")
    browser.find_element_by_class_name("btn").click()
    print("1-1：登录成功")

def AuditResult():
    time.sleep(2)
    browser.find_element_by_id('firstMenu12').click()
    print("2-1:进入 稽核结果")

# 开始工作件查询
def AuditResultSelect():
    time.sleep(2)
    browser.find_element_by_xpath("//div[@id = 'ui-id-13']/ul/li[4]/div").click()
    # browser.get('http://credit.risk.jc3.jieyue.com/loan-credit/lnadRauReconsider/prepareExecute/toQueryPage')
    print('2-2:进入 稽核复议查询')
    time.sleep(2)
    browser.switch_to.frame(browser.find_element_by_xpath("//iframe[contains(@src,'/lnadRauReconsider/prepareExecute/toQueryPage')]"))

    #重置
    time.sleep(2)
    browser.find_element_by_name("intoAppId").send_keys("120154631226")
    browser.find_element_by_name("customerName").send_keys("儿轩祁")
    browser.find_element_by_name("createName").send_keys("万里娜")
    Select(browser.find_element_by_name("result")).select_by_visible_text("同意")
    time.sleep(2)
    browser.find_element_by_xpath("//div[@class = 'searchBtn']/button[2]").click()
    print("2-3:重置成功")

    #查询
    time.sleep(2)
    browser.find_element_by_name("intoAppId").send_keys("120154631226")
    time.sleep(2)
    browser.find_element_by_xpath("//div[@class = 'searchBtn']/button[1]").click()
    print("2-4:查询成功")

def QuestionWoker():
    time.sleep(2)
    browser.switch_to.default_content()  # 跳出frame
    print("跳出frame")
    browser.find_element_by_xpath("//div[@id = 'ui-id-13']/ul/li[5]/div").click()
    print("3-1:进入集合问题统计（信审员）页面")
    time.sleep(2)
    browser.switch_to.frame(browser.find_element_by_xpath("//iframe[contains(@src,'lnadRouAuditInfo/prepareExecute/toQueryZyMistakePage')]"))
    time.sleep(2)
    #统计
    browser.find_element_by_xpath("//div[@class = 'searchBtn']/button[1]")
    time.sleep(2)
    print("3-2：统计结果查询成")
    # 重置
    browser.find_element_by_xpath("//div[@class = 'searchBtn']/button[2]")
    print("3-3:重置成功")

def QuestionAdmin():
    time.sleep(2)
    browser.switch_to.default_content()  # 跳出frame
    print("跳出frame")
    browser.find_element_by_xpath("//div[@id = 'ui-id-13']/ul/li[6]/div").click()
    print("4-1:进入集合问题统计（信审主管）页面")
    time.sleep(2)
    browser.switch_to.frame(browser.find_element_by_xpath("//iframe[contains(@src,'lnadRouAuditInfo/prepareExecute/toQueryZgMistakePage')]"))
    time.sleep(2)

    #查询
    browser.find_element_by_name("countDate_start").send_keys("2019-10-10")
    browser.find_element_by_name("countDate_end").send_keys("2019-10-12")
    time.sleep(2)
    browser.find_element_by_name("creditUser").click()
    print("4-2:跳转到选择信审人页面成功")
    browser.switch_to.default_content()  # 跳出frame
    time.sleep(2)
    browser.switch_to.frame(browser.find_element_by_xpath( "//iframe[contains(@src,'&callFun=setBrefCallFun&tabTitle=稽核问题统计（信审主管）&orgType=LOAN')]"))
    time.sleep(2)
    browser.find_element_by_name("userName").send_keys("吴昊飞")
    browser.find_element_by_name('userNo').send_keys("10017606")
    time.sleep(2)
    browser.find_element_by_xpath("//div[@class = 'searchBtn']/button/span[2]").click()
    time.sleep(2)
    print("4-3:查询成功")
    browser.find_element_by_class_name("oddTr").click()
    time.sleep(2)
    browser.find_element_by_link_text("确认").click()
    print("4-4:选择信审员成功")
    time.sleep(2)
    browser.switch_to.default_content()  # 跳出frame
    time.sleep(2)
    browser.switch_to.frame(browser.find_element_by_xpath("//iframe[contains(@src,'lnadRouAuditInfo/prepareExecute/toQueryZgMistakePage')]"))
    time.sleep(2)
    browser.find_element_by_xpath("//div[@class = 'searchBtn']/button[1]/span[2]").click()
    time.sleep(2)
    print("4-5:查询成功")

    #重置
    time.sleep(2)
    browser.find_element_by_xpath("//div[@class = 'searchBtn']/button[2]/span[2]").click()
    time.sleep(2)
    print("4-6:重置成功")



if __name__ == '__main__':
    login()
    #进入集合结果
    AuditResult()
    AuditResultSelect()
    QuestionWoker()
    QuestionAdmin()
    browser.quit()
    print("测试完毕，浏览器关闭")

