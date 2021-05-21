# -*- coding: utf-8 -*-
import config
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

def login(driver):
	
	driver.get("https://play.hbomax.com/")
	input("Manually sign into Netflix press Enter to continue: ")

	return

def select_profile(driver):
	"""
		Set HBO Max profile name in the config file as HBOMAX_ACC
	"""

	defualt_elements = driver.find_elements_by_class_name("default")
	for web_element in defualt_elements:
		nested_elements = web_element.find_elements_by_class_name("class1")

		for element in nested_elements:
			e = element.find_elements_by_class_name("class7")

			for i in e:
				if config.HBOMAX_ACC in i.text:
					i.click()
					sleep(2)
					return
	return

def movie_search(driver, movie_title):

	driver.find_element_by_css_selector("[aria-label=Search]").click()
	sleep(1)

	# Send keys w/o clicking on element 
	actions = ActionChains(driver)
	actions.send_keys(movie_title)
	actions.perform()

	# After typing wait for page to load
	sleep(2) 
	return

def scan_results(driver, movie_title):

	movie_found = False

	defualt_elements = driver.find_elements_by_class_name("default")
	for web_element in defualt_elements:
		current_title = web_element.get_attribute('aria-label')	
		link = web_element.get_attribute('href')
		if current_title is not None:
			if movie_title in current_title:
				print(f"Found '{movie_title}' as '{current_title}' ")
				movie_found = True

	return movie_found

def search(driver, movie_title):
	driver.get("https://play.hbomax.com/")
	sleep(5)

	select_profile(driver)
	movie_search(driver, movie_title=movie_title)
	
	is_on_hbomax = scan_results(driver, movie_title=movie_title)

	return is_on_hbomax
