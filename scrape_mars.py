from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
from splinter import Browser
import pandas as pd
from flask import Flask, render_template
from flask_pymongo import PyMongo

def init_browser():

    # @NOTE: Replace the path with your actual path to the chromedriver
    # executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser("chrome", headless=False)




def strip():

	url = 'https://mars.nasa.gov/news/'
	response = requests.get(url)
	soup = bs(response.text, 'html.parser')

	tresult = soup.find('div', class_="content_title").find('a').text
	title = tresult.strip()
	paragraph = soup.find('div',class_="rollover_description_inner").text.strip()

	browser = init_browser()

	url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
	browser.visit(url)

	html = browser.html
	soup = bs(html, "html.parser")
	a =soup.find('footer').a['data-fancybox-href']
	featuredimageurl ="https://www.jpl.nasa.gov"+a
	url = "https://twitter.com/marswxreport?lang=en"
	browser.visit(url)

	html = browser.html
	url = 'https://twitter.com/marswxreport?lang=en'
	browser.visit(url)
	# time.sleep(1)

	html = browser.html
	weather_soup = bs(html, 'html.parser')

	# First, find a tweet with the data-name `Mars Weather`
	# mars_weather_tweet = weather_soup.find('div', attrs={"class": "tweet", "data-name": "Mars Weather"})

	# Set weather
	mars_weather = weather_soup.find('p', 'tweet-text').get_text()


	url = "https://space-facts.com/mars/"

	tables = pd.read_html(url)

	hemisphere_image_urls = [
	    {"title": "Valles Marineris Hemisphere", "img_url": "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
	    {"title": "Cerberus Hemisphere", "img_url": "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
	    {"title": "Schiaparelli Hemisphere", "img_url": "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
	    {"title": "Syrtis Major Hemisphere", "img_url": "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
	]

	dictionary = [mars_weather,hemisphere_image_urls]

	return dictionary

	