from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from datetime import date
import time
from info import *

driver = webdriver.Chrome()
wait30 = WebDriverWait(driver,30)
driver.set_window_size(1124, 850)

def rerun_on_error(func):
    def wrapper():
        while True:
            try:
                func()
                break
            except:
                pass
    return wrapper

def login():
		time.sleep(1)
		driver.get('https://stafftravel.goindigo.in/')
		driver.find_element_by_id("memberId").send_keys(ID)
		driver.find_element_by_id("mobilePass").send_keys(PASSWORD)
		driver.find_element_by_class_name("buttonText").click()
		wait30.until(ec.presence_of_element_located((By.NAME,"or-src")))
		print("Logged in")				#login ends

@rerun_on_error
def reach_page():
		wait30.until(ec.element_to_be_clickable((By.NAME,"or-src")))
		time.sleep(1)
		driver.find_element_by_name("or-dest").clear()
		driver.find_element_by_name("or-dest").send_keys("CCU"+Keys.ENTER)
		time.sleep(1)
		driver.find_element_by_xpath("//*[contains(@class,'ui-datepicker-today')]").click()
		time.sleep(1)
		driver.find_element_by_name("or-depart").send_keys(Keys.ENTER)
		wait30.until(ec.presence_of_element_located((By.XPATH,"//*[contains(@class,'trip-filter-head')]")))

def enter(text,element):
	action = ActionChains(driver)
	action.move_to_element_with_offset(element,100,120)
	action.click()
	action.send_keys(text+Keys.ENTER)
	action.perform()
	time.sleep(1)


def getPrice(from_,to_):
	driver.find_element_by_xpath("//*[contains(@class,'changeBtn  btn-re-gray-md')]").click()
	enter(from_,driver.find_element_by_name("origin"))
	enter(to_,driver.find_element_by_name("destination"))
	enter(date.today().strftime("%d"),driver.find_element_by_id("fieldDepart"))
	driver.find_element_by_class_name("btn-md-dark").click()

	for day in range(1,7):
		price = ' '
		wait30.until(ec.presence_of_element_located((By.XPATH,"//*[contains(@class,'trip-filter-head')]")))
		trips = driver.find_elements_by_xpath("//*[contains(@class,'row trips-row')]")
		if len(trips) == 0:
			driver.find_element_by_xpath(f"//*[contains(@data-index,'{day}')]").click()
			continue
		price = driver.find_element_by_xpath("//*[contains(@class,'price ')]").text

	time.sleep(0.3)
	return price
