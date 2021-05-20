# -*- coding: utf-8 -*-
import config
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

def account_login(driver):
	
	# Landing on log in page, if you are already signed in it re-directs to /browse page
	if "browse" not in driver.current_url:
		# Click "Sign In" button
		try: 
			sign_in_button = driver.find_element_by_partial_link_text('Sign In')
			sign_in_button.click()
			sleep(3)

			# Send email/pass
			username = config.NETFLIX_EMAIL
			email_field = driver.find_element_by_name("userLoginId")
			email_field.send_keys(username)

			password = config.NETFLIX_PASS
			password_field = driver.find_element_by_name("password")
			password_field.send_keys(password)
			sleep(1)

			# Click to log in
			sign_in_button = driver.find_element_by_xpath("//button[@class='btn login-button btn-submit btn-small']")
			sign_in_button.click()
			sleep(3)
		except:
			input(f"failed at Netflix log in")
	try:
		# Select profile
		profiles = driver.find_elements_by_class_name("profile-name")
		for profile in profiles:
			#print(profile.text) # print names of Netflix account names
			if config.NETFLIX_ACC == profile.text:
				profile.click()
	except:
		# Prompt to select Netflix account isn't there 
		pass
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

	account_login(driver)
	movie_search(driver, movie_title=movie_title)
	
	is_on_netflix = scan_results(driver, movie_title=movie_title)

	return is_on_netflix
