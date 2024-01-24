
#idÓÃ #container   classÓÃ .plant
from ast import Name, Str
from math import e
from os import close, link, name
from time import sleep
from tkinter import Pack
from tkinter.tix import Tree
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import datetime

def Download_file(path,Information):
    # 设置Edge浏览器下载路径
    options = webdriver.EdgeOptions()
    # prefs = {"download.default_directory": r"C:\Users\SSA-User\Desktop\Performance Benchmark Tool\Down\P1", "download.prompt_for_download": False}
    prefs = {"download.default_directory": path, "download.prompt_for_download": False}

    options.add_experimental_option('prefs',prefs)
    options.add_experimental_option('detach',True)

    wd = webdriver.Edge(options=options) 

    wd.implicitly_wait(10)
    wd.get('https://benchmarktool.azurewebsites.net/')
    #点击login
    wd.find_element(By.XPATH,"/html/body/div/div/header/nav/div/div/ul/li/a").click()
    #点击login with Microsoft account
    wd.find_element(By.XPATH,"/html/body/div/main/div/div/section/form/div/p/button").click()
    #选择登录的账号
    #wd.find_element(By.XPATH,"//*[contains(@aria-label,'xinzhang6')]").click()
    sleep(10)

    for i in range(1,11):
        #点击History页面
        wd.find_element(By.XPATH,"/html/body/div/div/header/nav/div/div/ul/li[3]/a").click() 
        
        xpath_expression = Information
        # 将'01-10'替换为'01-01'
        modified_xpath = xpath_expression.replace("01-10", "01-{:02d}".format(i))
        
        wd.find_element(By.XPATH, modified_xpath).click()
        # wd.find_element(By.XPATH,"//tr[td[contains(text(), 'Verifyperformance-P1-EUS2E.redis.cache.windows.net:6380; SSL; GET; Clients:500; P1; 02-10')]]//a[@class='btn btn-outline-info btn-sm']").click()
        sleep(2)
        current_url = wd.current_url#"D:\Tests\Benchmark\statistics\Statistics.txt"
        with open(r"D:\Tests\Benchmark\statistics\Statistics.txt", "a", encoding="utf-8") as file:
        # 写入数据，并添加换行符
            file.write(current_url + "\n")
        element = wd.find_element(By.XPATH,"/html/body/div/div/div/div/table/tbody/tr/td[2]/button") #点击下载
        element.click()
        sleep(3)
    wd.close()
        
#修改日期
#获取当前日期的前一天(取昨天)
# current_date = (datetime.datetime.utcnow() - datetime.timedelta(days=1)).strftime("%m-%d")  
# previous_date = (datetime.datetime.utcnow() - datetime.timedelta(days=1)).strftime("%m%d")
#前三天(周五挂、周一取)
#current_date = (datetime.datetime.utcnow() - datetime.timedelta(days=3)).strftime("%m-%d")
previous_date = (datetime.datetime.utcnow() - datetime.timedelta(days=3)).strftime("%m%d")
#当天日期
# previous_date = (datetime.datetime.utcnow() - datetime.timedelta(days=1)).strftime("%m%d")
current_date = datetime.datetime.utcnow().strftime("%m-%d")

# current_date = '12-25'
# previous_date = '1225'

#NO-SSL-P1-P5
for i in range(1,6):#"D:\Tests\Benchmark\statistics\Down"
    path = r"D:\Tests\Benchmark\statistics\Down\P" + str(i)
    Information = "//tr[td[contains(text(), 'Verifyperformance-P{}-EUS2E-{}.redis.cache.windows.net:6379; Non-SSL; GET; Clients:500; P{}; {}; 01-10')]]//a[@class='btn btn-outline-info btn-sm']".format(i,previous_date,i,current_date)
    Download_file(path,Information)
          
# SSL-P1-P5  ssl
# for i in range(1,6):
#     path = r"D:\Tests\Benchmark\Down\P{} - ¸ssl" + format(i)
#     Information = "//tr[td[contains(text(), 'Verifyperformance-P{}-EUS2E-{}.redis.cache.windows.net:6380; SSL; GET; Clients:500; P{}; {}; 02-10')]]//a[@class='btn btn-outline-info btn-sm']".format(i,previous_date,i,current_date)
#     Download_file(path,Information)

#NO-SSL-SC0-SC6
for i in range(0,7):
    path = r"D:\Tests\Benchmark\statistics\Down\SC" + str(i)
    Information = "//tr[td[contains(text(), 'Verifyperformance-C{}-EUS2E-Standard-{}.redis.cache.windows.net:6379; Non-SSL; GET; Clients:100; C{}; {}; 01-10')]]//a[@class='btn btn-outline-info btn-sm']".format(i,previous_date,i,current_date)
    Download_file(path,Information)
    
#SSL-SC0-SC6  ssl
# for i in range(0,7):
#     path = r"D:\Tests\Benchmark\Down\SC{} - ¸±±¾" + format(i)
#     Information = "//tr[td[contains(text(), 'Verifyperformance-C{}-EUS2E-Standard-{}.redis.cache.windows.net:6380; SSL; GET; Clients:100; C{}; {}; 02-10')]]//a[@class='btn btn-outline-info btn-sm']".format(i,previous_date,i,current_date)
#     Download_file(path,Information)

# #NO-SSL-BC0 - BC6
for i in range(0,7):
    path = r"D:\Tests\Benchmark\statistics\Down\BC"+ str(i)
    Information = "//tr[td[contains(text(), 'Verifyperformance-C{}-EUS2E-Basic-{}.redis.cache.windows.net:6379; Non-SSL; GET; Clients:100; C{}; {}; 01-10')]]//a[@class='btn btn-outline-info btn-sm']".format(i,previous_date,i,current_date)
    Download_file(path,Information)
#SSL-BC0 - BC6  
# for i in range(0,7):
#     path = r"D:\Tests\Benchmark\Down\BC{} - ,ssl".format(i)
#     Information = "//tr[td[contains(text(), 'Verifyperformance-C{}-EUS2E-Basic-{}.redis.cache.windows.net:6380; SSL; GET; Clients:100; C{}; {}; 02-10')]]//a[@class='btn btn-outline-info btn-sm']".format(i,previous_date,i,current_date)
#     Download_file(path,Information)







