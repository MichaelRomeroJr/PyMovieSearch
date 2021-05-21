# -*- coding: utf-8 -*-
import config
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

def login(driver):

	driver.get("https://www.amazon.com/gp/video/storefront")
	input("Manually sign into Netflix press Enter to continue: ")
	
	return


def movie_search(driver, movie_title):

	driver.find_element_by_class_name("nav-search-field ").click()
	sleep(2)

	# Send keys w/o clicking on element 
	actions = ActionChains(driver)
	actions.send_keys(movie_title)
	actions.perform()

	driver.find_element_by_id("nav-search-submit-button").click()

	return


def scan_results(driver, movie_title):

	movie_found = False

	first_movie_elems = driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[1]/div/span[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div[1]/h2/a/span")
	for elem in first_movie_elems:
		title = elem.text
		if movie_title in title: 
			# is "Without Remose" in "Tom Clancy's Without Remorse"
			movie_found = True
			print(f"Found '{movie_title}' as '{title}' ")

	return movie_found


def check_if_free(driver, available):
	"""
		Check if "Watch Movie" button is there
		if not, it's likely available in a special package (Starz etc) or availabe for Rent on Hulu.
	"""
	is_free = False

	if available:
		watch_movie_button = driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[1]/div/span[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div[3]/div[1]/div/div[2]/span/span/a")
		
		for e in watch_movie_button:
			#print(e.text)	
			#print(e.get_attribute('href'))
			if e.text == "Watch now":
				is_free = True

	return is_free

def search(driver, movie_title):
	driver.get("https://www.amazon.com/gp/video/storefront")

	movie_search(driver, movie_title=movie_title)

	availability = scan_results(driver, movie_title=movie_title)		
	is_on_prime = check_if_free(driver, available=availability)

	if availability and (not is_on_prime):
		print(f"primevideo: available as Rental / Purchase")

	return is_on_prime
