from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import os
import pandas as pd
import time
from selenium import webdriver
import pymongo

def scrape():
    mars_dict = {}

    # news title and description from NASA news
    url = "https://mars.nasa.gov/news/"
    driver = webdriver.Chrome()
    driver.get(url)
    soup = bs(driver.page_source, 'html.parser')
    list = soup.find('div', class_='list_text')
    news_title = list.find('div', class_='content_title').text
    news_p = list.find('div', class_='article_teaser_body').text

    mars_dict['news_title'] = news_title
    mars_dict['news_p'] = news_p


    # image url from NASA Mars space images
    imageurl = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    driver = webdriver.Chrome()
    driver.get(imageurl)
    soup = bs(driver.page_source, 'html.parser')
    article = soup.find('article', class_='carousel_item')
    a = article.find('a')
    featured_image_url_extension = a["data-fancybox-href"]
    featured_image_url = ("https://www.jpl.nasa.gov"+featured_image_url_extension)

    mars_dict['featured_image_url'] = featured_image_url


    # latest weather tweet from NASA twitter
    tweeturl = "https://twitter.com/marswxreport?lang=en"
    driver = webdriver.Chrome()
    driver.get(tweeturl)
    soup = bs(driver.page_source, 'html.parser')
    latest_tweet = soup.find('div', class_='js-tweet-text-container')
    mars_weather = latest_tweet.find('p').text

    mars_dict['weather'] = mars_weather


    # Mars facts table
    factsurl = "https://space-facts.com/mars/"
    factsTable = pd.read_html(factsurl)
    facts_df = factsTable[-1]
    facts_df = facts_df.rename(columns={0:"Description",1:"Value"})
    factsT_html = facts_df.to_html()

    mars_dict['facts_table'] = factsT_html


    # Mars hemisphers
    hemispheresurl = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    driver = webdriver.Chrome()
    driver.get(hemispheresurl)
    soup = bs(driver.page_source, 'html.parser')
    divs = soup.find_all('div', class_='description')
    hemisphere_dict = []
    for div in divs:
        title = div.find('h3').text
        title=title.replace(" Enhanced","")
        hemisphere_name = title.replace(" Hemisphere", "")
        hemisphere_string = hemisphere_name.replace(" ", "_")
        image_url = "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/" + str(hemisphere_string) + "_enhanced.tif/full.jpg"
        hemisphere_dict.append({"title":title, "image_url":image_url})

    mars_dict['hemisphere_dict'] = hemisphere_dict
    return mars_dict
