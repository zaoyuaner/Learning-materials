#encoding:utf-8

from selenium import webdriver
import time
dirver_path = r"C:\www\chromedriver\chromedriver.exe"

driver = webdriver.Chrome(executable_path=dirver_path)
driver.get("http://www.baidu.com/")

time.sleep(3)

# driver.quit()
driver.close()