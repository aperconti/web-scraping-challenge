# importing dependencies
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
import requests
import time


urls = [
    'https://mars.nasa.gov/news/',
    'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars',
    'https://space-facts.com/mars/',
    'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
]


def append_to_final_list(title, img_url, hemisphere_image_urls=[]):
    hemisphere_image_urls.append({"title": title, "img_url": img_url})
    hemisphere_image_urls = list(
        {v['title']: v for v in hemisphere_image_urls}.values()
    )


def mars_news():
    url = 'https://mars.nasa.gov/news/'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find_all('div', class_="content_title")[0]
    new_title = title.contents[1].contents[0].strip()
    news = soup.find_all('div', class_="rollover_description_inner")[0]
    news_p = news.contents[0].strip()

    return new_title, news_p


def mars_featured_image():
    # URL of page to be scraped
    domain = "https://www.jpl.nasa.gov"
    url = f'{domain}/spaceimages/?search=&category=Mars'
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=True)
    match_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(match_url)
    browser.links.find_by_partial_text("FULL IMAGE").click()
    seconds = 15
    time.sleep(seconds)
    rendered_html = browser.html
    soup = BeautifulSoup(rendered_html, 'html.parser')
    featured_image_url = soup.find_all(
        "img", class_="fancybox-image")[0]['src']
    return featured_image_url


def mars_fact_table():
    # URL of interest
    url = 'https://space-facts.com/mars/'
    # Extract tables
    dfs = pd.read_html(url)
    # Get first table from url of interest
    df = dfs[0]
    fact_table = df.to_html()

    return fact_table


def schiaparelli_hemisphere():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=True)
    match_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(match_url)
    browser.links.find_by_partial_text(
        "Schiaparelli Hemisphere Enhanced").click()
    seconds = 15
    time.sleep(seconds)
    rendered_html = browser.html
    soup = BeautifulSoup(rendered_html, 'html.parser')
    # Title for Schiaparelli Hemisphere Enhanced
    image_title = soup.find_all("h2", class_="title")[0]
    title = image_title.contents[0].strip()
    # image for Schiaparelli Hemisphere Enhanced
    image = soup.find(text="Sample")
    image_url = image.parent['href']

    return title, image_url


def cerberus_hemisphere():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=True)
    match_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(match_url)
    browser.links.find_by_partial_text(
        "Cerberus Hemisphere Enhanced").click()
    seconds = 15
    time.sleep(seconds)
    rendered_html = browser.html
    soup = BeautifulSoup(rendered_html, 'html.parser')
    # Title for Cerberus Hemisphere Enhanced
    image_title = soup.find_all("h2", class_="title")[0]
    cerberus_title = image_title.contents[0].strip()
    # image for Cerberus Hemisphere Enhanced
    image = soup.find(text="Sample")
    cerberus_image_url = image.parent['href']

    return cerberus_title, cerberus_image_url


def syrtism_major_hemisphere():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=True)
    match_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(match_url)
    browser.links.find_by_partial_text(
        "Syrtis Major Hemisphere Enhanced").click()
    seconds = 15
    time.sleep(seconds)
    rendered_html = browser.html
    soup = BeautifulSoup(rendered_html, 'html.parser')
    # Title for Syrtis Major Hemisphere Enhanced
    image_title = soup.find_all("h2", class_="title")[0]
    syrtis_title = image_title.contents[0].strip()
    # image for Syrtis Major Hemisphere Enhanced
    image = soup.find(text="Sample")
    syrtis_image_url = image.parent['href']

    return syrtis_title, syrtis_image_url


def valles_marineris_hemisphere():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=True)
    match_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(match_url)
    browser.links.find_by_partial_text(
        "Valles Marineris Hemisphere Enhanced").click()
    seconds = 15
    time.sleep(seconds)
    rendered_html = browser.html
    soup = BeautifulSoup(rendered_html, 'html.parser')
    # Title for Syrtis Major Hemisphere Enhanced
    image_title = soup.find_all("h2", class_="title")[0]
    valles_title = image_title.contents[0].strip()
    # image for Syrtis Major Hemisphere Enhanced
    image = soup.find(text="Sample")
    valles_image_url = image.parent['href']
    return valles_title, valles_image_url


def scrape():
    data = {}

    featured_image = mars_featured_image()
    data["featured_image"] = featured_image

    new_title, news_p = mars_news()
    data["news_title"] = new_title
    data["news_p"] = news_p

    mars_facts = mars_fact_table()
    data["mars_facts"] = mars_facts

    data["hemisphere_image_urls"] = []

    schiaparelli_title, schiaparelli_url = schiaparelli_hemisphere()
    data["hemisphere_image_urls"].append(
        {"title": schiaparelli_title, "img_url": schiaparelli_url})

    cerberus_title, cerberus_image_url = cerberus_hemisphere()
    data["hemisphere_image_urls"].append(
        {"title": cerberus_title, "img_url": cerberus_image_url})

    syrtis_title, syrtis_image_url = syrtism_major_hemisphere()
    data["hemisphere_image_urls"].append(
        {"title": syrtis_title, "img_url": syrtis_image_url})

    valles_title, valles_image_url = valles_marineris_hemisphere()
    data["hemisphere_image_urls"].append(
        {"title": valles_title, "img_url": valles_image_url})

    return data


# print(scrape())
