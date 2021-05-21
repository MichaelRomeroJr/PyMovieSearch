# -*- coding: utf-8 -*-
import pathlib
from selenium import webdriver

import config
from Netflix import netflix
from Hulu import hulu
from PrimeVideo import primevideo
from HBOMax import hbomax  
from DisneyPlus import disneyplus

def setup(driver, exclude_list):
	if "DisneyPlus" not in exclude_list:
		disneyplus.login(driver)
	if "HBOMax" not in exclude_list:
		hbomax.login(driver)
	if "Hulu" not in exclude_list:	
		hulu.login(driver)
	if "Netflix" not in exclude_list:	
		netflix.login(driver)
	if "PrimeVideo" not in exclude_list:	
		primevideo.login(driver)
	
	return

def create_movie_args_dict(args_list):
	count = len(args_list)

	movies_dict = {}
	for n in range(count):
		movies_dict[n] = ""

	return movies_dict

def movie_dict_format(list, dictionary):

	index=0
	movies_dict={}
	got_title = False

	# iterate though list from args.movies [movie, title, one, movie, title, two]
	for elem in list:
		dictionary[index] = dictionary[index] + " " + elem 
		if "," in elem:
			index+=1
	
	movies = {}
	index=0
	for key in dictionary:
		if len(dictionary[key]) > 0:
			title = dictionary[key]

			if title[0] == " ": # remove leading space
				title = title[1:]

			if title[-1] == ",": # remove trailing comma
				title = title[:-1]
			movies[index] = title
			index+=1

	return	movies
