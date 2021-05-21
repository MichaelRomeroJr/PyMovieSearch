# -*- coding: utf-8 -*-
import config
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

def login(driver):
	driver.get("https://www.netflix.com/")
	input("Manually sign into Netflix press Enter to continue: ")

	return


def select_profile(driver):
	"""
		Set Netflix profile name in the config file as NETFLIX_ACC
	"""
	
	try:
		# Select profile
		profiles = driver.find_elements_by_class_name("profile-name")
		for profile in profiles:
			#print(profile.text) # print names of Netflix account names
			if config.NETFLIX_ACC == profile.text:
				profile.click()
				return
	except:
		print(f"select_profile fail")
		
	return


def movie_search(driver, movie_title):
	driver.find_element_by_class_name("icon-search").click()
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

	movie_titles = driver.find_elements_by_class_name("fallback-text")
	for movie in movie_titles:
		#print(f"Title: {movie.text}")
		if movie.text == movie_title:
			movie_found = True

	return movie_found


def search(driver, movie_title):
	driver.get("https://www.netflix.com/")

	select_profile(driver)
	movie_search(driver, movie_title=movie_title)
	
	is_on_netflix = scan_results(driver, movie_title=movie_title)

	return is_on_netflix
