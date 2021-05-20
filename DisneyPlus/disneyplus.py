# -*- coding: utf-8 -*-
import config
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

def account_login(driver):
	sign_in_button = driver.find_elements_by_class_name("btn-secondary")

	for element in sign_in_button:
		#print(element.text)
		if "LOG IN" in element.text:
			input("First time Disney+ log in: ")
			return

	return

def movie_search(driver, movie_title):
	driver.get("https://www.disneyplus.com/search")
	sleep(2)

	# Send keys w/o clicking on element  
	actions = ActionChains(driver)
	actions.send_keys(movie_title)
	actions.perform()

	# After typing wait for page to load
	sleep(2) 
	return

def scan_results(driver, movie_title):

	movie_found = False

	defualt_elements = driver.find_elements_by_class_name("gv2-asset")
	for web_element in defualt_elements:
		# iterate through we elemets of images
		nested_elements = web_element.find_elements_by_class_name("sc-hMqMXs")
		for elem in nested_elements:
			# first subfield
			element_id = elem.get_attribute('data-testid') 
			if element_id == "movie-title":
				# second subfield where aria label w/ name is located
				sub_elements = elem.find_elements_by_class_name("sc-kpOJdX") 
				for e in sub_elements:
					current_title = e.get_attribute('aria-label')
					if movie_title in current_title:
						print(f"Found {movie_title} as {current_title}")
						movie_found = True

	return movie_found

def search(driver, movie_title):
	driver.get("https://www.disneyplus.com/home")
	sleep(5)

	account_login(driver)
	movie_search(driver, movie_title=movie_title)
	
	is_on_disneyplus = scan_results(driver, movie_title=movie_title)

	return is_on_disneyplus