# -*- coding: utf-8 -*-
import config
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

def login(driver):
	
	driver.get("https://www.disneyplus.com/home")
	input("sign into Disney+ press Enter to continue: ")

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
		#nested_elements = web_element.find_elements_by_class_name("sc-hMqMXs") #5/20
		nested_elements = web_element.find_elements_by_class_name("sc-cvbbAY") # 6/24

		for elem in nested_elements:
			# first subfield
			element_id = elem.get_attribute('data-testid')

			#if "search-result"element_id == "movie-title": # 5/24
			if "search-result" in element_id:
				# second subfield where aria label w/ name is located
				sub_elements = elem.find_elements_by_class_name("sc-kpOJdX") 

				for e in sub_elements:
					current_title = e.get_attribute('aria-label')
					print(f"current_title: {current_title}")
					if movie_title in current_title:
						print(f"Found '{movie_title}' as '{current_title}' ")
						movie_found = True

	return movie_found

def search(driver, movie_title):
	
	driver.get("https://www.disneyplus.com/home")
	sleep(5)

	movie_search(driver, movie_title=movie_title)
	
	is_on_disneyplus = scan_results(driver, movie_title=movie_title)

	return is_on_disneyplus
