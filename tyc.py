# -*- coding: utf_8 -*-
__author__ = 'lyh'
__date__ = '2018/1/31 16:58'

# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
from selenium import webdriver
from time import sleep

print (123)

def Search():
	# f = open('company.csv', 'a')
	# sleep(1)
	# f.write(str(22) + '\n')
	# f.close()
 #    f.write(str(connect))
 #    f.close()
    chrome_opt = webdriver.ChromeOptions()
    # 无图浏览
    # prefs = {'profile.managed_default_content_settings.images': 2}
    # chrome_opt.add_experimental_option('prefs', prefs)
    chrome_opt.add_argument("user-data-dir=C:/gongju/Google/Chrome/Application/chromedriver")
    chrome_opt.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
    browser = webdriver.Chrome(chrome_options=chrome_opt)
    browser.get("https://www.tianyancha.com/login")
    browser.get("https://www.tianyancha.com/")
    # browser.find_element_by_xpath(".//*[@id='web-content']/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/input").send_keys('18870445595')
    # browser.find_element_by_xpath(".//*[@id='web-content']/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[3]/input").send_keys('lyh915348696')
    # browser.find_element_by_xpath(".//*[@id='web-content']/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[5]").click()
    sleep(20)
    companys = []
    #将公司文件导出到列表
    for ln in open('company.txt', 'rt'):
        #'\n'为对txt文件中的公司换行处理
        companys.extend(ln.strip().split('\n'))

    for i in range(len(companys)):
        company = companys[i]
        company = u'%s' %company
        # company.encode("utf-8")
        browser.get("https://www.tianyancha.com/")
        browser.get("https://www.tianyancha.com/")
        sleep(3)
        browser.find_element_by_xpath(".//*[@id='home-main-search']").send_keys(company)
        try:
        	# 
            # browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div[1]/form/div/ul/li[1]/div[2]/div/em").click()
            browser.find_element_by_xpath("//*[@id='web-content']/div/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div/span").click()
            #获取公司链接
            # href = browser.find_element_by_xpath(".//*[@id='web-content']/div/div/div/div[1]/div[3]/div[1]/div[2]/div[1]/a").get_attribute('href')
            sleep(2)
            # browser.get(href)
            print(1)
            company = browser.find_element_by_xpath("//*[@id='web-content']/div/div[1]/div[3]/div[2]/div[1]/div/div[3]/div[1]/a/em").text
            legal_person = browser.find_element_by_xpath("//*[@id='web-content']/div/div[1]/div[3]/div[2]/div[1]/div/div[3]/div[2]/div[1]/a").text
            fund = browser.find_element_by_xpath("//*[@id='web-content']/div/div[1]/div[3]/div[2]/div[1]/div/div[3]/div[2]/div[2]/span").text
            time = browser.find_element_by_xpath("//*[@id='web-content']/div/div[1]/div[3]/div[2]/div[1]/div/div[3]/div[2]/div[3]/span").text
            tel = browser.find_element_by_xpath("//*[@id='web-content']/div/div[1]/div[3]/div[2]/div[1]/div/div[3]/div[3]/div[1]/span[2]/span[1]").text
            email = browser.find_element_by_xpath("//*[@id='web-content']/div/div[1]/div[3]/div[2]/div[1]/div/div[3]/div[3]/div[2]/span[2]").text
            url = browser.find_element_by_xpath("//*[@id='web-content']/div/div[1]/div[3]/div[2]/div[1]/div/div[3]/div[1]/a/em").text

            # company = browser.find_element_by_xpath("//*[@id='company_web_top']/div[2]/div[2]/div[1]/h1").text
            # legal_person = ''
            # fund = ''
            # time = ''
            # tel = browser.find_element_by_xpath("//*[@id='company_web_top']/div[2]/div[2]/div[3]/div[1]/div[1]/span[2]").text
            # email = browser.find_element_by_xpath("//*[@id='company_web_top']/div[2]/div[2]/div[3]/div[1]/div[2]/span[2]").text
            # try:
            # 	company = browser.find_element_by_xpath("//*[@id='web-content']/div/div[1]/div[3]/div[2]/div[1]/div/div[3]/div[1]/a/em").text
            # except:
            # 	company = ''
            # try:
            # 	legal_person = browser.find_element_by_xpath("//*[@id='web-content']/div/div[1]/div[3]/div[2]/div[1]/div/div[3]/div[2]/div[1]/a").text
            # except:
            # 	legal_person = ''
            # try:
            # 	fund = browser.find_element_by_xpath("//*[@id='web-content']/div/div[1]/div[3]/div[2]/div[1]/div/div[3]/div[2]/div[2]/span").text
            # except:
            # 	fund = ''
            # try:
            # 	time = browser.find_element_by_xpath("//*[@id='web-content']/div/div[1]/div[3]/div[2]/div[1]/div/div[3]/div[2]/div[3]/span").text
            # except:
            # 	time = ''
            # try:
            # 	tel = browser.find_element_by_xpath("//*[@id='web-content']/div/div[1]/div[3]/div[2]/div[1]/div/div[3]/div[3]/div[1]/span[2]/span[1]").text
            # except:
            # 	tel = ''
            # # address = browser.find_element_by_xpath(".//*[@id='company_web_top']/div[2]/div[2]/div[2]/div[3]/div[2]/span[2]").text
            # try:
            # 	email = browser.find_element_by_xpath("//*[@id='web-content']/div/div[1]/div[3]/div[2]/div[1]/div/div[3]/div[3]/div[2]/span[2]").text
            # except:
            # 	email = ''
            # try:
            # 	url = browser.find_element_by_xpath("//*[@id='web-content']/div/div[1]/div[3]/div[2]/div[1]/div/div[3]/div[1]/a/em").text
            # except:
            # 	url = ''
            #对公司信息拼接
            connect = str(company) + ',' + str(legal_person) + ',' +str(fund) + ',' +str(time) + ',' +str(tel) + ',' + str(email) + ',' + str(url)
            f = open('company.csv', 'a')
            sleep(1)
            f.write(str(connect) + '\n')
            f.close()
            print (connect)
        except Exception:
            print (Exception)
        sleep(1)

if __name__ == '__main__':
    Search()