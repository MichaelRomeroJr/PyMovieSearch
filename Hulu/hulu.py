# -*- coding: utf-8 -*-
import config
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

def login(driver):

	driver.get("https://www.hulu.com/hub/home")
	input("Manually sign into Netflix press Enter to continue: ")
	return


def movie_search(driver, movie_title):
	driver.get("https://www.hulu.com/search")

	driver.find_element_by_class_name("SearchBar").click() #.send_keys("Some Movie")
	sleep(2)

	# # Send keys w/o clicking on element 
	actions = ActionChains(driver)
	actions.send_keys(movie_title)
	actions.perform()

	sleep(2) 
	return


def scan_results(driver, movie_title):

	movie_found = False
	movie_url = ""
	movie_elements = driver.find_elements_by_class_name("ListItem")
	for element in movie_elements:

		title = element.find_elements_by_class_name("ListItem__content")
		for elem in title:
			#print(f"Movie: {elem.text}")
			if movie_title in elem.text:
			 	#print(f"Found: {elem.text}")
			 	print(f"Found '{movie_title}' as '{elem.text}' ")
			 	movie_url = element.get_attribute('href')
			 	movie_found = True
			 	return movie_found, movie_url

	return movie_found, movie_url

def check_if_free(driver, available, movie_hulu_url):
	"""
		Check if "Watch Movie" button is there
		if not, it's likely available in a special package (Starz etc) or availabe for Rent on Hulu.
	"""
	is_free = False

	if available:
		driver.get(movie_hulu_url)
		sleep(3)
		
		watch_movie_button = driver.find_elements_by_class_name("WatchAction")
		for e in watch_movie_button:
			#print(e.text)	
			#print(e.get_attribute('href'))
			if e.text == "WATCH MOVIE":
				is_free = True

	return is_free

def search(driver, movie_title):

	driver.get("https://www.hulu.com/hub/home")

	movie_search(driver, movie_title=movie_title)	
	availability, movie_url = scan_results(driver, movie_title=movie_title)

	is_on_hulu= check_if_free(driver, available=availability, movie_hulu_url=movie_url)

	if availability and (not is_on_hulu):
		print(f"Hulu: available on Premium Package / Rental")

	return is_on_hulu
