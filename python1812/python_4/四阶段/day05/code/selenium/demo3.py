#encoding:utf-8

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
dirver_path = r"C:\www\chromedriver\chromedriver.exe"

driver = webdriver.Chrome(executable_path=dirver_path)
driver.get("http://www.baidu.com/")
#inputTag = driver.find_element_by_id('kw')
#inputTag = driver.find_element_by_name('wd')
#inputTag = driver.find_element_by_class_name('s_ipt')
#inputTag = driver.find_element_by_xpath('//*[@id="kw"]')
#inputTag = driver.find_element_by_css_selector(".quickdelete-wrap > input")
inputTag = driver.find_element(By.XPATH,"//*[@id='kw']")
# inputTag = driver.find_element(By.ID,"//*[@id='kw']")
# inputTag = driver.find_element(By.NAME,"//*[@id='kw']")
# inputTag = driver.find_element(By.CLASS_NAME,"//*[@id='kw']")
# inputTag = driver.find_element(By.CSS_SELECTOR,"//*[@id='kw']")
#By 其实就是find_element_by_xpath 的一个简化步骤
inputTag.send_keys("苍老师")
time.sleep(5)
driver.close()