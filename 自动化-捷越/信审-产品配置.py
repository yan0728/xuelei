import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
import random

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

# 开始产品级别配置
def ToQueryPage():
    time.sleep(3)
    browser.find_element_by_id('firstMenu8').click()
    print("2-1:进入产品配置")
    time.sleep(2)
    # browser.find_element_by_xpath("//div[@id = 'ui-id-9']/ul/li[2]/div/span").click()
    browser.find_element_by_xpath("//span[text() = ' 产品级别配置']").click()
    print('2-2:进入产品级别配置')
    time.sleep(3)
    #产品名称
    browser.switch_to.frame(browser.find_element_by_xpath("//iframe[contains(@src,'/lbtStoreProClasfRef/prepareExecute/toQueryPage')]"))
    time.sleep(2)
    Select(browser.find_element_by_name('productType')).select_by_visible_text('优悦贷C 停用')
    #选择产品级别
    Select(browser.find_element_by_name('classification')).select_by_visible_text('A')
    #查询
    browser.find_element_by_xpath("//div[@class='searchBtn']/button[1]").click()
    print("2-3:查询成功")
    time.sleep(2)
    #重置
    browser.find_element_by_xpath("//div[@class='searchBtn']/button[2]").click()
    print("2-4:重置成功")
    # 选择列表
    btns = browser.find_elements_by_tag_name('td')
    i = 0
    while (i < len(btns) and btns[i].text != '1'):
        i = i + 1
    btns[i].click()
    #删除
    browser.find_element_by_xpath("//a[text()='删除']").click()
    time.sleep(2)
    # browser.find_element_by_xpath("//div[@class = 'ui-dialog-buttonset']/button[1]").click()  # 点击确定
    browser.find_element_by_xpath("//div[@class = 'ui-dialog-buttonset']/button[2]").click() #点击关闭
    print("2-5:删除/关闭成功")

def EditPage():
    #编辑
    browser.find_element_by_xpath("//a[text()='编辑']").click()
    print("2-6:进入 产品配置编辑页面")
    time.sleep(3)
    Select(browser.find_element_by_id('dtoclassification')).select_by_visible_text("B") #选择设置产品级别
    browser.find_element_by_id('prodStr0').click() #选择产品
    time.sleep(5)
    browser.find_element_by_xpath("//a[text()='新增适用门店']").click()
    print("2-7:进入到选择机构页面")
    time.sleep(3)
    #选择机构
    browser.find_element_by_xpath("//div[@id = 'orgTree']/div/li/ul/li/span[2]").click()
    #获取确定按钮
    browser.find_element_by_xpath("//div[contains(@style,'display: block; z-index: 102;')]/div[3]/div/button[1]").click()
    time.sleep(2)
    print("2-8:添加机构完成")

    #删除机构
    browser.find_element_by_xpath("//form[@id = 'addNewsFormData']/div[2]/div[1]/div[2]/table/tbody/tr/td").click()
    time.sleep(2)
    browser.find_element_by_xpath("//form[@id = 'addNewsFormData']/div/a[2]").click()
    print("2-9:删除成功")

    #添加机构
    time.sleep(2)
    browser.find_element_by_xpath("//form[@id = 'addNewsFormData']/div[2]/div[1]/div[1]/table/tbody/tr/th/div/input").click()
    print("选择第一个元素成功")
    time.sleep(2)
    browser.find_element_by_xpath("//span[text()='保存']").click()
    print("2-10:新产品保存成功")

# 贷前业务规则
def BusinessRule():
    time.sleep(2)
    browser.switch_to.default_content()

    # time.sleep(3)
    # browser.find_element_by_id('firstMenu8').click()
    # print("2-1:进入产品配置")

    time.sleep(2)
    # browser.find_element_by_xpath("//div[@id = 'ui-id-9']/ul/li[3]/div/span").click()
    browser.find_element_by_xpath("//span[text() = ' 贷前业务规则']").click()
    time.sleep(2)
    print('3-1:进入贷前业务规则')
    browser.switch_to.frame(browser.find_element_by_xpath("//iframe[contains(@src,'/loan-credit//bizRuleConf/prepareExecute/toQueryPageMain')]"))
    time.sleep(2)
    browser.switch_to.frame(browser.find_element_by_xpath("//iframe[contains(@src,'/prepareExecute/toQueryPage')]"))
    # #重置
    browser.find_element_by_xpath("//form[@class = 'searchFrom']/div/input").send_keys("recon_partner_rule_001")
    browser.find_element_by_xpath("//form[@class = 'searchFrom']/div[2]/input").send_keys("recon_partner_rule_001")
    time.sleep(2)
    browser.find_element_by_xpath("//div[@class = 'searchBtn']/button[2]").click()
    print("3-2:重置成功")
    # 新增
    time.sleep(2)
    # browser.find_element_by_xpath("//a[text()='新增']").click()
    browser.find_element_by_link_text("新增").click()
    print("3-4:进入新增页面")
    time.sleep(2)
    randomCode =  random.randint(11111,99999)
    randomName =   random.randint(1000,9999)
    # browser.switch_to.default_content()  # 跳出frame
    browser.switch_to.frame(browser.find_element_by_xpath("//iframe[contains(@src,'prepareExecute/toAdd')]"))
    browser.find_element_by_id('dtoruleCode').send_keys(randomCode)
    browser.find_element_by_id('dtoruleName').send_keys(randomName)
    browser.find_element_by_id('dtoruleShoworder').send_keys(9999)
    browser.find_element_by_id('dtoruleRemark').send_keys("say something...")
    print("3-5:新增内容填写完毕")
    time.sleep(1)
    # browser.switch_to.frame(browser.find_element_by_xpath("//iframe[contains(@src,'/prepareExecute/toQueryPage')]"))
    browser.switch_to.parent_frame()
    time.sleep(2)
    browser.find_element_by_xpath("//div[@class = 'ui-dialog-buttonset']/button[1]").click() #保存
    # browser.find_element_by_xpath("//div[@class = 'ui-dialog-buttonset']/button[2]").click()  # 关闭
    print("3-6:保存或关闭成功")
    # 查询
    time.sleep(2)
    browser.find_element_by_xpath("//form[@class = 'searchFrom']/div/input").send_keys(randomCode)
    browser.find_element_by_xpath("//div[@class = 'searchBtn']/button[1]").click()
    print("3-3:查询成功")

    #修改
    time.sleep(2)
    btns = browser.find_elements_by_tag_name('td')
    i = 0
    while (i < len(btns) and btns[i].text != '1'):
        i = i + 1
    btns[i].click()
    time.sleep(2)
    browser.find_element_by_link_text("修改").click()
    print("3-7:进入修改页面")
    time.sleep(2)
    browser.switch_to.frame(browser.find_element_by_xpath("//iframe[contains(@src,'prepareExecute/toUpdate')]"))
    time.sleep(2)
    Select(browser.find_element_by_id('dtoruleState')).select_by_visible_text('失效')
    print("3-8:修改为失效成功")
    time.sleep(2)
    browser.switch_to.parent_frame()
    time.sleep(2)
    browser.find_element_by_xpath("//div[@class = 'ui-dialog-buttonset']/button[1]").click() #保存
    print("3-9:修改内容保持成功")
    time.sleep(2)
    browser.find_element_by_xpath("//div[@class = 'ui-dialog-buttonset']/button[2]").click()  # 关闭
    time.sleep(2)
    browser.find_element_by_xpath("//div[@class = 'searchBtn']/button[1]").click()
    print("3-10:修改内容查询成功")
    #删除
    time.sleep(2)
    btns = browser.find_elements_by_tag_name('td')
    i = 0
    while (i < len(btns) and btns[i].text != '1'):
        i = i + 1
    btns[i].click()
    time.sleep(2)
    browser.find_element_by_link_text("删除").click()
    print("3-11:点击删除按键")
    time.sleep(3)
    #弹框确定
    browser.switch_to.alert.accept()
    time.sleep(2)
    print("3-12:点击弹框成功")
    # 弹框确定
    browser.switch_to.alert.accept()
    time.sleep(2)
    print("3-13:点击弹框成功")

#产品配置管理
#产品信息-优悦贷
def ProductConfigManageIntoInfo():

    time.sleep(2)
    browser.switch_to.default_content() #切换到根文档
    time.sleep(3)

    # 调试用
    # browser.find_element_by_id('firstMenu8').click()
    # print("2-1:进入产品配置")

    # browser.find_element_by_xpath("//div[@id = 'ui-id-9']/ul/li[3]/div/span").click() #点击 进入到 产品配置管理------------jc4-----------
    browser.find_element_by_xpath("//span[text() = ' 产品配置管理']").click()
    # browser.get('http://credit.risk.jc3.jieyue.com/loan-credit/lbTProductConf/prepareExecute/ProductConfIndex')
    print('4-1:进入产品配置管理')
    time.sleep(2)
    browser.switch_to.frame(browser.find_element_by_xpath("//iframe[contains(@src,'lbTProductConf/prepareExecute/ProductConfIndex')]"))
    time.sleep(2)
    browser.find_element_by_xpath("//div[@id = 'RoleList']/div/li/ul/li").click() #定位优悦贷

#进件参数配置
def ProductEdit():
    time.sleep(2)
    browser.switch_to.frame(browser.find_element_by_xpath("//iframe[contains(@src,'prepareExecute/toQueryPage')]"))
    time.sleep(2)
    #修改
    btns = browser.find_elements_by_tag_name('td')
    i = 0
    while (i < len(btns) and btns[i].text != '1'):
        i = i + 1
    btns[i].click()
    time.sleep(2)
    browser.find_element_by_link_text("修改").click()
    time.sleep(2)
    productNameRandmom = random.randint(111,999)
    dtomaxPatchCountRandrom = random.randint(1,31)
    onceMoreApplyDayRandrom = random.randint(10,100)
    #清空输入框
    browser.find_element_by_id("dtomaxPatchCount").clear()
    browser.find_element_by_id("dtoonceMoreApplyDay").clear()
    #重新输入
    browser.find_element_by_id("dtomaxPatchCount").send_keys(dtomaxPatchCountRandrom)
    browser.find_element_by_id("dtoonceMoreApplyDay").send_keys(onceMoreApplyDayRandrom)
    print("4-2:进件参数配置修改成")
    browser.find_element_by_xpath("//div[@class = 'ui-dialog-buttonset']/button").click()
    time.sleep(2)
    browser.switch_to.alert.accept()
    print("4-2:修改成功")

    #删除
def ProductDel():
    time.sleep(2)
    btns = browser.find_elements_by_tag_name('td')
    i = 0
    while (i < len(btns) and btns[i].text != '1'):
        i = i + 1
    btns[i].click()
    time.sleep(2)
    browser.find_element_by_link_text("删除").click()
    time.sleep(2)
    browser.switch_to.alert.accept()
    time.sleep(2)
    browser.switch_to.alert.accept()
    print("4-3:删除成功")
    time.sleep(2)
def ProductAdd():
    browser.find_element_by_link_text("新增").click()
    time.sleep(2)
    dtomaxPatchCountRandrom = random.randint(20, 30)
    onceMoreApplyDayRandrom = random.randint(30, 90)
    browser.find_element_by_id("dtomaxPatchCount").send_keys(dtomaxPatchCountRandrom)
    browser.find_element_by_id("dtoonceMoreApplyDay").send_keys(onceMoreApplyDayRandrom)
    print("4-4:进件新增页面并输入成功")
    browser.find_element_by_xpath("//div[@class = 'ui-dialog-buttonset']/button").click()
    time.sleep(2)
    browser.switch_to.alert.accept()
    print("4-4:新增保存成功")

#流程时效设置
def FlowConfig():
    time.sleep(2)
    browser.switch_to.parent_frame() #跳转到上个frame
    time.sleep(2)
    browser.find_element_by_link_text("流程时效设置").click()
    print("5-1:进入 流程时效设置 ")
    time.sleep(2)
    browser.switch_to.frame(browser.find_element_by_xpath("//iframe[contains(@src,'lbTCreditIntervalConf/prepareExecute/toQueryPage')]"))
    time.sleep(3)
    #查询，重置
    Select(browser.find_element_by_name("creditFlowId")).select_by_visible_text("信审审批流程")
    time.sleep(2)
    browser.find_element_by_xpath("//div[@class = 'searchBtn']/button/span").click()
    print("5-2:查询成功")
    time.sleep(2)
    browser.find_element_by_xpath("//div[@class = 'searchBtn']/button[2]/span").click()
    print("5-3:重置成功")
def FlowConfigAdd():
    time.sleep(2)
    browser.find_element_by_link_text("新增").click()
    time.sleep(2)
    print("5-8:打开新增页面")
    #输入内容并保持
    Select(browser.find_element_by_id("creditFlowId")).select_by_visible_text("信审审批流程")
    browser.find_element_by_id("interval").send_keys(48)
    browser.find_element_by_id("remindHourCount").send_keys(24)
    browser.find_element_by_id("supDocOverTime").send_keys(1)
    time.sleep(2)
    print("5-9:内如输入成功")
    browser.find_element_by_xpath("//span[text()='保存']").click()
    time.sleep(2)
    browser.switch_to.alert.accept()
    print("5-10：保存成功")
def FlowConfigEdit():
    #先查询
    Select(browser.find_element_by_name("creditFlowId")).select_by_visible_text("信审审批流程")
    browser.find_element_by_xpath("//div[@class = 'searchBtn']/button/span").click()
    time.sleep(2)
    btns = browser.find_elements_by_tag_name('td')
    i = 0
    while (i < len(btns) and btns[i].text != '1'):
        i = i + 1
    btns[i].click()
    time.sleep(2)
    browser.find_element_by_link_text("修改").click()
    time.sleep(2)
    print("5-4:进入修改页面")
    browser.find_element_by_id("interval").send_keys(40)
    browser.find_element_by_id("remindHourCount").send_keys(20)
    browser.find_element_by_id("supDocOverTime").send_keys(10)
    time.sleep(2)
    print("5-5:内容输入完毕")
    time.sleep(2)
    browser.find_element_by_xpath("//span[text()='保存']").click()
    time.sleep(2)
    browser.switch_to.alert.accept()
    print("5-6:修改成功")
def FlowConfigDel():
    time.sleep(2)
    # 先查询
    Select(browser.find_element_by_name("creditFlowId")).select_by_visible_text("信审审批流程")
    browser.find_element_by_xpath("//div[@class = 'searchBtn']/button/span").click()
    time.sleep(2)
    btns = browser.find_elements_by_tag_name('td')
    i = 0
    while (i < len(btns) and btns[i].text != '1'):
        i = i + 1
    btns[i].click()
    time.sleep(2)
    browser.find_element_by_link_text("删除").click()
    time.sleep(2)
    browser.switch_to.alert.accept()
    time.sleep(2)
    browser.switch_to.alert.accept()
    time.sleep(2)
    print("5-7:删除成功")

#复议设置
def FuYiSet():
    time.sleep(2)
    browser.switch_to.parent_frame()  # 跳转到上个frame
    time.sleep(2)
    browser.find_element_by_link_text("复议设置").click()
    time.sleep(2)
    print("6-1:进入到  复议设置页面")
    browser.switch_to.frame(browser.find_element_by_xpath("//iframe[contains(@src,'lbTReconsiderationConf/prepareExecute/toQueryPage')]"))

def FuYiSetEdit():
    time.sleep(2)
    btns = browser.find_elements_by_tag_name('td')
    i = 0
    while (i < len(btns) and btns[i].text != '1'):
        i = i + 1
    btns[i].click()
    time.sleep(2)
    browser.find_element_by_link_text("修改").click()  #点击修改
    print("6-2:进入到 修改页面")
    time.sleep(2)
    browser.find_element_by_id("dtomaxCount").clear() #情况输入框
    browser.find_element_by_id("dtomaxCount").send_keys("4")  # 输入新的数据
    print("6-3:最大复议次数修改成功")
    time.sleep(2)
    browser.find_element_by_xpath("//div[@class = 'ui-dialog-buttonset']/button/span").click() #点击保存
    print("6-4:最大复议次数修改保存成功")
def FuYiSetDel():
    #选择列表第一个
    time.sleep(2)
    btns = browser.find_elements_by_tag_name('td')
    i = 0
    while (i < len(btns) and btns[i].text != '1'):
        i = i + 1
    btns[i].click()
    time.sleep(2)
    browser.find_element_by_link_text("删除").click() #点击删除
    time.sleep(2)
    browser.switch_to.alert.accept()
    print("6-5:列表删除成功")
def FuYiSetAdd():
    time.sleep(2)
    browser.find_element_by_link_text("新增").click()
    time.sleep(2)
    print("6-6:进入 新增页面")
    browser.find_element_by_id("dtomaxCount").send_keys("2")
    print("6-7:最大复议次数修输入成功")
    time.sleep(2)
    browser.find_element_by_xpath("//div[@class = 'ui-dialog-buttonset']/button/span").click()  # 点击保存
    print("6-8:新增复议保存成功")

#事务定义
def ShiWuDefine():
    time.sleep(2)
    browser.switch_to.parent_frame()  # 跳转到上个frame
    time.sleep(2)
    browser.find_element_by_link_text("事务定义").click()
    time.sleep(2)
    print("7-1:进入到  事务定义页面")

def ShiWuDefineQueryAndReset():
    time.sleep(2)
    browser.switch_to.frame(browser.find_element_by_xpath("//iframe[contains(@src,'lbTTrans/prepareExecute/toQueryPage')]"))
    time.sleep(2)
    #输入内容
    browser.find_element_by_name("transName").send_keys("线上稽核")
    browser.find_element_by_name("transGroup").send_keys("稽核")
    browser.find_element_by_name("transCode").send_keys("AUDIT_XSJH")
    time.sleep(2)
    browser.find_element_by_xpath("//div[@class = 'searchBtn']/button/span[2]").click() #点击查询
    time.sleep(2)
    print("7-2:查询成功")
    browser.find_element_by_xpath("//div[@class = 'searchBtn']/button[2]/span[2]").click()  # 点击重置
    time.sleep(2)
    print("7-3:重置成功")


if __name__ == '__main__':
    login()
    #产品级别配置
    ToQueryPage()
    EditPage()
    #贷前业务规则
    BusinessRule()
    # 产品配置管理-产品信息
    ProductConfigManageIntoInfo()
    #进件参数配置
    ProductEdit() #修改
    ProductDel() #删除
    ProductAdd() #添加
    #进入流程时效设置
    FlowConfig()
    FlowConfigEdit()
    FlowConfigDel()
    FlowConfigAdd()
    #复议设置
    FuYiSet()
    FuYiSetEdit()
    FuYiSetDel()
    FuYiSetAdd()
    #事务定义
    ShiWuDefine()
    ShiWuDefineQueryAndReset()
    browser.quit()
    print("测试完毕，浏览器已关")