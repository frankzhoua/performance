﻿
#id用 #container   class用 .plant
from ast import Name, Str
from cgitb import text
from os import link, name
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import datetime

def P_operate(name,Primary,description):
    wd = webdriver.Edge() 
    wd.implicitly_wait(10)
    wd.get('https://benchmarktool.azurewebsites.net/')
    wd.find_element(By.XPATH,"/html/body/div/div/header/nav/div/div/ul/li/a").click()
    wd.find_element(By.XPATH,"/html/body/div/main/div/div/section/form/div/p/button").click()
    sleep(5)
    #wd.find_element(By.XPATH,"//*[contains(@aria-label,'xinzhang6')]").click()
    sleep(10)
    description_1 = description
    for i in range(1,11):
        #跑一次改一次备注，方便你我
        #C和P的数值不一样，注意修改！
        #ssl-BC6
        name = name
        Primary =Primary
        description = description_1 + str(i).zfill(2)
        
        wd.find_element(By.XPATH,"/html/body/div/div/header/nav/div/div/ul/li[2]/a").click()
        input_element = WebDriverWait(wd,20).until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div/div/div/div/div[1]/div/form/div[2]/input")))
        input_element.clear()
    
        #修改Name of the test
        input_element.send_keys(name)

        text_style = WebDriverWait(wd,20).until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div/div/div/div/div[1]/div/form/div[8]/select")))
        text_style.click()
        sleep(2)
        
        input_style = WebDriverWait(wd,20).until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div/div/div/div/div[1]/div/form/div[8]/select/option[1]")))
        input_style.click()

        input_element=wd.find_element(By.XPATH,"/html/body/div/div/div/div/div/div[1]/div/form/div[4]/div/input")
        input_element.clear()
    
        #修改Primary String (host:port,password={password},ssl={True or False})
        input_element.send_keys(Primary)

        wd.find_element(By.XPATH,"/html/body/div/div/div/div/div/div[1]/div/form/div[12]/div[1]/div[2]/input").click()

        input_element=wd.find_element(By.XPATH,"/html/body/div/div/div/div/div/div[1]/div/form/div[9]/textarea")
        input_element.clear()
    
        #修改Enter a description
        input_element.send_keys(description)


        input_element=wd.find_element(By.XPATH,"/html/body/div/div/div/div/div/div[1]/div/form/div[12]/div[1]/div[5]/div/input")
        input_element.clear()
        input_element.send_keys("500")

        input_element=wd.find_element(By.XPATH,"/html/body/div/div/div/div/div/div[1]/div/form/div[12]/div[1]/div[6]/div/input")
        input_element.clear()
        input_element.send_keys("1024")

        wd.find_element(By.XPATH,"/html/body/div/div/div/div/div/div[1]/div/form/div[12]/div[5]/button").click()
        sleep(5)
        wd.find_element(By.XPATH,"/html/body/div/div/header/nav/div/div/ul/li[3]/a").click()
        

def C_operate(name,Primary,description):
    wd = webdriver.Edge() 
    wd.implicitly_wait(10)
    wd.get('https://benchmarktool.azurewebsites.net/')
    wd.find_element(By.XPATH,"/html/body/div/div/header/nav/div/div/ul/li/a").click()
    wd.find_element(By.XPATH,"/html/body/div/main/div/div/section/form/div/p/button").click()
    sleep(5)
    #wd.find_element(By.XPATH,"//*[contains(@aria-label,'xinzhang6')]").click()
    sleep(10)
    description_1 = description
    for i in range(9,10):
        #跑一次改一次备注，方便你我
        #C和P的数值不一样，注意修改！
        #ssl-BC6
        name = name
        Primary =Primary
        description = description_1 + str(i).zfill(2)
        
        wd.find_element(By.XPATH,"/html/body/div/div/header/nav/div/div/ul/li[2]/a").click()
        
        input_element = WebDriverWait(wd,20).until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div/div/div/div/div[1]/div/form/div[2]/input")))
        input_element.clear()
    
        #修改Name of the test
        input_element.send_keys(name)
        #点击Select a region
        wd.find_element(By.XPATH,"/html/body/div/div/div/div/div/div[1]/div/form/div[7]/select").click()
        sleep(1)
        locator_1 = (By.XPATH,'/html/body/div/div/div/div/div/div[1]/div/form/div[7]/select/option[1]')
        test_box_style = WebDriverWait(wd, 100).until(EC.element_to_be_clickable(locator_1))#error
        test_box_style.click()

        input_element=wd.find_element(By.XPATH,"/html/body/div/div/div/div/div/div[1]/div/form/div[4]/div/input")
        input_element.clear()
    
        #修改Primary String (host:port,password={password},ssl={True or False})
        input_element.send_keys(Primary)

        wd.find_element(By.XPATH,"/html/body/div/div/div/div/div/div[1]/div/form/div[12]/div[1]/div[2]/input").click()
        #清空description
        input_element=wd.find_element(By.XPATH,"/html/body/div/div/div/div/div/div[1]/div/form/div[8]/textarea")
        input_element.clear()
    
        #修改Enter a description
        input_element.send_keys(description)


        # input_element=wd.find_element(By.XPATH,"/html/body/div/div/div/div/div/div[1]/div/form/div[12]/div[1]/div[5]/div/input")
        # input_element.clear()
        # input_element.send_keys("500")

        input_element=wd.find_element(By.XPATH,"/html/body/div/div/div/div/div/div[1]/div/form/div[12]/div[1]/div[6]/div/input")
        input_element.clear()
        input_element.send_keys("1024")

        #点击run
        wd.find_element(By.XPATH,"/html/body/div/div/div/div/div/div[1]/div/form/div[12]/div[5]/button").click()

        sleep(5)
        
        #点击history
        wd.find_element(By.XPATH,"/html/body/div/div/header/nav/div/div/ul/li[3]/a").click()

#更改日期，拼接cache名字上的时间
#当天
#current_date = datetime.datetime.utcnow().strftime("%m%d")
#前一天        
#current_date = (datetime.datetime.utcnow() - datetime.timedelta(days=1)).strftime("%m%d")
#前两天        
current_date = (datetime.datetime.utcnow() - datetime.timedelta(days=2)).strftime("%m%d")
# current_date = '1126'

#创建P1-P5
for j in range(1,6):
    #查找P
    FindName = "P"+str(j)+"-CUSE"
    FindNOPrimary = "P"+str(j)+"-CUSE-{}.redis.cache.windows.net:6379".format(current_date)
    #'P1-CUSE-1110.redis.cache.windows.net:6379'
    FindNODescription = "P"+str(j)+"-CUSE-{}.redis.cache.windows.net:6379".format(current_date)
    
    # FindSSLPrimary = "P"+str(j)+"-CUSE-{}.redis.cache.windows.net:6380".format(current_date)
    # FindSSLDescription = "P"+str(j)+"-CUSE-{}.redis.cache.windows.net:6380".format(current_date)
    
    UseName = ""
    UseNOPrimary = ""
    UseNODescription = ""
    # UseSSLPrimary = ""
    # UseSSLDescription = ""
    
    #查找Name //"D:\Tests\Benchmark\Attributes\Name - P.txt"
    with open(r"D:\Tests\Benchmark\Attributes\Name - P.txt", "r") as file:
        for line in file:
            if FindName in line:
                UseName = line.strip()  # 去除行末尾的换行符和空格
                break
    #查找no-ssl-Primary//"D:\Tests\Benchmark\2Attributes\Primary String - P.txt"
    with open(r"D:\Tests\Benchmark\Attributes\Primary String - P.txt", "r") as file:
        for line in file:
            if FindNOPrimary in line:
                UseNOPrimary = line.strip()  # 去除行末尾的换行符和空格
                break
    #查找ssl-Primary
    # with open(r"C:\Users\SSA-User\Desktop\insert number.txt", "r") as file:
    #     for line in file:
    #         if FindSSLPrimary in line:
    #             UseSSLPrimary = line.strip()  # 去除行末尾的换行符和空格
    #             break
            
    # 查找no-ssl-Description  
    with open(r"D:\Tests\Benchmark\Attributes\Description - P.txt", "r") as file:
        for line in file:
            if FindNODescription in line:
                UseNODescription = line.strip()  # 去除行末尾的换行符和空格
                break
    # 查找ssl-Description  
    # with open(r"C:\Users\SSA-User\Desktop\Performance Benchmark Tool\Description - P.txt", "r") as file:
    #     for line in file:
    #         if FindSSLDescription in line:
    #             UseSSLDescription = line.strip()  # 去除行末尾的换行符和空格
    #             break
     
    #跳过调用P1的操作
    #P_operate(UseName,UseNOPrimary,UseNODescription)
    # P_operate(UseName,UseSSLPrimary,UseSSLDescription)

#创建S-C0
for j in range(2,3):
    #查找SC
    FindName = "C"+str(j)+"-CUSE-Standard"
    FindNOPrimary = "C"+str(j)+"-CUSE-Standard-{}.redis.cache.windows.net:6379".format(current_date)
    FindNODescription = "C"+str(j)+"-CUSE-Standard-{}.redis.cache.windows.net:6379".format(current_date)
    
    # FindSSLPrimary = "C"+str(j)+"-CUSE-Standard-{}.redis.cache.windows.net:6380".format(current_date)
    # FindSSLDescription = "C"+str(j)+"-CUSE-Standard-{}.redis.cache.windows.net:6380".format(current_date)
    
    UseName = ""
    UseNOPrimary = ""
    UseNODescription = ""
    # UseSSLPrimary = ""
    # UseSSLDescription = ""
    
    #查找Name
    with open(r"D:\Tests\Benchmark\Attributes\Name - C.txt", "r") as file:
        for line in file:
            if FindName in line:
                UseName = line.strip()  # 去除行末尾的换行符和空格
                break
    #查找no-ssl-Primary
    with open(r"D:\Tests\Benchmark\Attributes\Primary String - C.txt", "r") as file:
        for line in file:
            if FindNOPrimary in line:
                UseNOPrimary = line.strip()  # 去除行末尾的换行符和空格
                break
    #查找ssl-Primary
    # with open(r"C:\Users\SSA-User\Desktop\insert number.txt", "r") as file:
    #     for line in file:
    #         if FindSSLPrimary in line:
    #             UseSSLPrimary = line.strip()  # 去除行末尾的换行符和空格
    #             break
            
    # 查找no-ssl-Description  
    with open(r"D:\Tests\Benchmark\Attributes\Description - C.txt", "r") as file:
        for line in file:
            if FindNODescription in line:
                UseNODescription = line.strip()  # 去除行末尾的换行符和空格
                break
    # 查找ssl-Description  
    # with open(r"C:\Users\SSA-User\Desktop\Performance Benchmark Tool\Description - C.txt", "r") as file:
    #     for line in file:
    #         if FindSSLDescription in line:
    #             UseSSLDescription = line.strip()  # 去除行末尾的换行符和空格
    #             break
     
    #不执行SC
    C_operate(UseName,UseNOPrimary,UseNODescription)
    # C_operate(UseName,UseSSLPrimary,UseSSLDescription)
    

#创建B-C0
for j in range(1,7):
    #查找BC
    FindName = "C"+str(j)+"-CUSE-Basic"
    FindNOPrimary = "C"+str(j)+"-CUSE-Basic-{}.redis.cache.windows.net:6379".format(current_date)
    FindNODescription = "C"+str(j)+"-CUSE-Basic-{}.redis.cache.windows.net:6379".format(current_date)
    
    FindSSLPrimary = "C"+str(j)+"-CUSE-Basic-{}.redis.cache.windows.net:6380".format(current_date)
    FindSSLDescription = "C"+str(j)+"-CUSE-Basic-{}.redis.cache.windows.net:6380".format(current_date)
    
    UseName = ""
    UseNOPrimary = ""
    UseNODescription = ""
    UseSSLPrimary = ""
    UseSSLDescription = ""
    
    #查找Name
    with open(r"D:\Tests\Benchmark\Attributes\Name - C.txt", "r") as file:
        for line in file:
            if FindName in line:
                UseName = line.strip()  # 去除行末尾的换行符和空格
                break
    #查找no-ssl-Primary
    with open(r"D:\Tests\Benchmark\Attributes\Primary String - C.txt", "r") as file:
        for line in file:
            if FindNOPrimary in line:
                UseNOPrimary = line.strip()  # 去除行末尾的换行符和空格
                break
    #查找ssl-Primary
    # with open(r"C:\Users\SSA-User\Desktop\insert number.txt", "r") as file:
    #     for line in file:
    #         if FindSSLPrimary in line:
    #             UseSSLPrimary = line.strip()  # 去除行末尾的换行符和空格
    #             break
            
    # 查找no-ssl-Description  
    with open(r"D:\Tests\Benchmark\Attributes\Description - C.txt", "r") as file:
        for line in file:
            if FindNODescription in line:
                UseNODescription = line.strip()  # 去除行末尾的换行符和空格
                break
    # 查找ssl-Description  
    # with open(r"C:\Users\SSA-User\Desktop\Performance Benchmark Tool\Description - C.txt", "r") as file:
    #     for line in file:
    #         if FindSSLDescription in line:
    #             UseSSLDescription = line.strip()  # 去除行末尾的换行符和空格
    #             break
            
    #C_operate(UseName,UseNOPrimary,UseNODescription)
    # C_operate(UseName,UseSSLPrimary,UseSSLDescription)
    







