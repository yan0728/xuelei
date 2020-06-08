from selenium import webdriver

driverfile_path = r'D:\python37\学习\chromedriver.exe'
browser = webdriver.Chrome( executable_path=driverfile_path) # 声明浏览器

base_url = 'http://www.baidu.com'
browser.maximize_window()
browser.get(base_url) # 访问网页