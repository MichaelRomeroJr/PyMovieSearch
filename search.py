# -*- coding: utf-8 -*-
import pathlib
from selenium import webdriver
from time import sleep

import config
from Netflix import netflix
from Hulu import hulu
from PrimeVideo import primevideo
from HBOMax import hbomax  
from DisneyPlus import disneyplus

def configure_chrome_driver():  
	options = webdriver.ChromeOptions()  
	options.add_argument(f"user-data-dir={pathlib.Path(__file__).parent.absolute().joinpath('chrome-profile')}")  	
	the_driver = webdriver.Chrome(executable_path=config.DRIVER_EXECUTABLE_PATH, options=options)  

	#the_driver = webdriver.Chrome('/mnt/c/Python/chromedriver.exe') # hardcode path
	return the_driver


if __name__ == '__main__':
	driver = configure_chrome_driver()
	movie = "Without Remorse" # Prime
	#movie = "Hellboy II" # Hulu
	#movie = "Mortal Kombat" # HBOMax
	#movie = "Coco" # Disney+

	print(f"Looking for '{movie}'")
	print(f"Querying Disney+: ")
	if disneyplus.search(driver, movie):
		print(f"'{movie}' is on Disney+")

	print(f"Querying HBO Max: ")
	if hbomax.search(driver, movie):
		print(f"'{movie}' is on HBO Max")

	print(f"Querying Netflix: ")
	if netflix.search(driver, movie):
		print(f"'{movie}' is on Netflix")

	print(f"Querying Hulu: ")
	if hulu.search(driver, movie):
		print(f"'{movie}' is on Hulu")

	print(f"Querying PrimeVideo: ")
	if primevideo.search(driver, movie):
		print(f"'{movie}' is on PrimeVideo")

	driver.close()