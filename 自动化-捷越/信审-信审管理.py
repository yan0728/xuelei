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

# 开始工作件查询
def SelectWoker():
    time.sleep(3)
    browser.find_element_by_id('firstMenu3').click()
    print("2-1:进入信审管理")
    time.sleep(3)
    # browser.get('http://credit.risk.jc3.jieyue.com/loan-credit/workfile/toQueryPage')
    browser.find_element_by_xpath("//span[text() = ' 工作件查询']").click()
    print('2-2:进入工作件查询')

    # 工作件查询
    time.sleep(3)
    browser.switch_to.frame(browser.find_element_by_xpath("//iframe[contains(@src,'loan-credit/workfile/toQueryPage')]"))
    time.sleep(2)
    # 展开
    browser.find_element_by_link_text('展开 >').click()
    #进件编号
    browser.find_element_by_xpath("//form[@class='searchFrom']/div[1]/input").send_keys("120154630635")
    #客户姓名
    browser.find_element_by_xpath("//form[@class='searchFrom']/div[2]/input").send_keys("闫学雷")
    #证件号码
    browser.find_element_by_xpath("//form[@class='searchFrom']/div[3]/input").send_keys("110224199007285618")
    #申请一级项目
    #申请二级项目
    #所属门店
    #进件来源
    Select( browser.find_element_by_xpath("//form[@class='searchFrom']/div[8]/select")).select_by_value('4')
    #进件状态
    Select(browser.find_element_by_xpath("//form[@class='searchFrom']/div[9]/select")).select_by_value('1700')
    # 手机
    browser.find_element_by_xpath("//form[@class='searchFrom']/div[10]/input").send_keys("13810957727")
    #审批类型
    Select(browser.find_element_by_xpath("//form[@class='searchFrom']/div[11]/select")).select_by_value('1')
    # 重置
    time.sleep(2)
    browser.find_element_by_xpath("//div[@class='searchBtn']/button[2]").click()
    print("2-3:输入项输入正确，重置按键正常")
    #查询
    browser.find_element_by_xpath("//form[@class='searchFrom']/div[1]/input").send_keys("120154630635")
    browser.find_element_by_xpath("//div[@class='searchBtn']/button").click()
    print("2-4:查询成功")


#签约环节客户放弃申请查询
def GiveUpAudit():
    time.sleep(2)
    browser.switch_to.default_content()
    time.sleep(2)
    browser.find_element_by_xpath("//span[text() = ' 签约环节客户放弃申请查询']").click()
    print('3-1-进入 签约环节客户放弃审核')
    time.sleep(2)
    browser.switch_to.frame(browser.find_element_by_xpath("//iframe[contains(@src,'/prepareExecute/toQueryLbTRefuseGiveUpReport')]"))
    time.sleep(2)
    # 进件编号
    browser.find_element_by_name("intoAppId").send_keys("120154629979")
    # 客户姓名
    browser.find_element_by_name("custName").send_keys("辅助黄志伟")
    #申请类型
    Select(browser.find_element_by_name("reportType")).select_by_value('1')
    #审核结果
    Select(browser.find_element_by_name("auditResult")).select_by_value('1')
    #同意原因
    Select(browser.find_element_by_name("agreeReason")).select_by_visible_text("审核错误")
    #一级不同意原因
    Select(browser.find_element_by_name("oneDisagreeReason")).select_by_visible_text("不认定风险")
    #二级不同意原因
    Select(browser.find_element_by_name("twoDisagreeReason")).select_by_visible_text("风险认定标准不统一")
    #提交时间
    browser.find_element_by_name("createTime_start").send_keys("2019-10-15")
    browser.find_element_by_name("createTime_end").send_keys("2019-10-16")

    # 重置
    time.sleep(2)
    browser.find_element_by_xpath("//div[@class='searchBtn']/button[2]").click()
    print("3-2:输入项均可输入，重置键正常")
    time.sleep(2)
    browser.find_element_by_name("intoAppId").send_keys("120154629979")
    # 查询
    browser.find_element_by_xpath("//div[@class='searchBtn']/button").click()
    print("3-3:签约环节客户放弃审核 查询成功")

if __name__ == '__main__':
    login()
    SelectWoker()
    GiveUpAudit()
    browser.quit()
    print("完毕")