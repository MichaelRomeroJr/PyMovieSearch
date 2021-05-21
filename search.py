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

import utils

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
	parser.add_argument('--movie', '--movies', help="list of movies (seperated by commas) to query different streaming platforms.", nargs='+', default=[])
	parser.add_argument("--setup", dest = "setup", help = "First run is for streaming platform sign ins.", default = False)
	parser.add_argument('--exclude', help="platforms to exclude from search", nargs='+', default=[])
	
	return parser.parse_args()
	


if __name__ == '__main__':

	args = arg_parse()	

	# convert [movie, title, one, movie, title, two]
	# to {0: "movie title one" 1: "movie title two"}
	movies_dict = utils.create_movie_args_dict(args_list=args.movie)
	movies_dict = utils.movie_dict_format(list=args.movie, dictionary=movies_dict)

	print(f"movies to query: ")
	for key in movies_dict:
		print(f"{movies_dict[key]}")

	driver = configure_chrome_driver()
	for key in movies_dict:
		movie = movies_dict[key]

		# First setup is just logging in
		if args.setup:
			print("First run: ")
			utils.setup(driver)

		print(f"Looking for '{movie}' ")

		if "DisneyPlus" not in args.exclude:
			print(f"Querying Disney+: ",  end = " ")
			if disneyplus.search(driver, movie):
				print(f"'{movie}' is on Disney+")
			else:
				print(f"not available. ")

		if "HBOMax" not in args.exclude:
			print(f"Querying HBOMax: ", end = " ")
			if hbomax.search(driver, movie):
				print(f"'{movie}' is on HBO Max")
			else:
				print(f"not available. ")
		
		if "Hulu" not in args.exclude:
			print(f"Querying Hulu: ", end = " ")
			if hulu.search(driver, movie):
				print(f"'{movie}' is on Hulu")
			else:
				print(f"not available. ")

		if "Netflix" not in args.exclude:
			print(f"Querying Netflix: ",  end = " ")
			if netflix.search(driver, movie):
				print(f"'{movie}' is on Netflix")
			else:
				print(f"not available. ")

		if "PrimeVideo" not in args.exclude:
			print(f"Querying PrimeVideo: ", end = " ")
			if primevideo.search(driver, movie):
				print(f"'{movie}' is on PrimeVideo")
			else:
				print(f"not available. ")

		print()
	#driver.close()
