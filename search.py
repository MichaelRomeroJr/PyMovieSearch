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

import argparse

def configure_chrome_driver():  
	options = webdriver.ChromeOptions()  
	options.add_argument(f"user-data-dir={pathlib.Path(__file__).parent.absolute().joinpath('chrome-profile')}")  	
	the_driver = webdriver.Chrome(executable_path=config.DRIVER_EXECUTABLE_PATH, options=options)  

	#the_driver = webdriver.Chrome('/mnt/c/Python/chromedriver.exe') # hardcode path
	return the_driver

def arg_parse():
	"""
		Parse arguements to the detect module
	"""
	
	parser = argparse.ArgumentParser(description='Python app to query streaming platforms for movie title. ')
	parser.add_argument('--movie', '--movie-list', help="list of movies to query different streaming platforms.", nargs='+', default=[])
	#parser.add_argument("--movie", help = "Enter movie title to query different platforms.", default = "")

	return parser.parse_args()
	

if __name__ == '__main__':

	args = arg_parse()
	movie = ' '.join([str(elem) for elem in args.movie])

	driver = configure_chrome_driver()


	print(f"Looking for '{movie}' ")

	print(f"Querying Disney+: ",  end = " ")
	if disneyplus.search(driver, movie):
		print(f"'{movie}' is on Disney+")
	else:
		print(f"not available. ")

	print(f"Querying HBO Max: ", end = " ")
	if hbomax.search(driver, movie):
		print(f"'{movie}' is on HBO Max")
	else:
		print(f"not available. ")

	print(f"Querying Netflix: ",  end = " ")
	if netflix.search(driver, movie):
		print(f"'{movie}' is on Netflix")
	else:
		print(f"not available. ")

	print(f"Querying Hulu: ", end = " ")
	if hulu.search(driver, movie):
		print(f"'{movie}' is on Hulu")
	else:
		print(f"not available. ")

	print(f"Querying PrimeVideo: ", end = " ")
	if primevideo.search(driver, movie):
		print(f"'{movie}' is on PrimeVideo")
	else:
		print(f"not available. ")

	#driver.close()
