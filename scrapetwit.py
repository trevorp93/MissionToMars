from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import time


def init_browser():
	executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
	return Browser('chrome', **executable_path, headless=False)


def scrape():
	browser = init_browser()

	# Retrieve Mars Weather
	url = 'https://twitter.com/marswxreport?lang=en'
	browser.visit(url)
	# time.sleep(1)

	html = browser.html
	weather_soup = BeautifulSoup(html, 'html.parser')

	# First, find a tweet with the data-name `Mars Weather`
	mars_weather_tweet = weather_soup.find('div', attrs={"class": "tweet", "data-name": "Mars Weather"})

	# Set weather
	mars_weather = mars_weather_tweet.find('p', 'tweet-text').get_text()
	
	print(mars_weather)
	
	return mars_weather

scrape()