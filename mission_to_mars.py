#!/usr/bin/env python
# coding: utf-8

# In[227]:


# importing dependencies
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
import requests
import time


# In[228]:


# URL of page to be scraped
url = 'https://mars.nasa.gov/news/'


# In[229]:


# Retrieve page with the requests module
response = requests.get(url)
hemisphere_image_urls = []
def append_to_final_list(title, img_url):
    global hemisphere_image_urls
    hemisphere_image_urls.append({"title": title, "img_url": img_url})
    hemisphere_image_urls = list({v['title']:v for v in hemisphere_image_urls}.values())


# In[230]:


# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(response.text, 'html.parser')


# In[231]:


# Examine the results, then determine element that contains sought info
print(soup.prettify())


# In[232]:


###################################
#NASA Mars News
###################################
# results are returned as an iterable list
title = soup.find_all('div', class_="content_title")[0]
new_title = title.contents[1].contents[0].strip()
news = soup.find_all('div', class_="rollover_description_inner")[0]
news_p = news.contents[0].strip()


# In[233]:


# URL of page to be scraped
domain = "https://www.jpl.nasa.gov"
url = f'{domain}/spaceimages/?search=&category=Mars'


# In[234]:


# https://splinter.readthedocs.io/en/latest/drivers/chrome.html
get_ipython().system('which chromedriver')


# In[235]:


executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[236]:


match_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(match_url)


# In[237]:


browser.links.find_by_partial_text("FULL IMAGE").click()
seconds = 15
print(f"Sleeping for {seconds} seconds.")
time.sleep(seconds)
rendered_html = browser.html


# In[238]:


soup = BeautifulSoup(rendered_html, 'html.parser')


# In[239]:


####################################
#JPL Mars Space Images - Featured Image
####################################

# extracting the image url
featured_image_url = soup.find_all("img", class_="fancybox-image")[0]['src']
featured_image_url


# In[240]:


# URL of interest
url = 'https://space-facts.com/mars/'
# Extract tables
dfs = pd.read_html(url)


# In[241]:


#####################################
#Mars Facts
#####################################

# Get first table from url of interest
df = dfs[0]
df


# In[242]:


df.to_html()


# In[243]:


# https://splinter.readthedocs.io/en/latest/drivers/chrome.html
get_ipython().system('which chromedriver')


# In[244]:


executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[245]:


match_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(match_url)


# In[246]:


browser.links.find_by_partial_text("Schiaparelli Hemisphere Enhanced").click()
seconds = 15
print(f"Sleeping for f{seconds} seconds.")
time.sleep(seconds)
rendered_html = browser.html


# In[247]:


#################################
#Mars Hemispheres
#################################


#Schiaparelli Hemisphere Enhanced
soup = BeautifulSoup(rendered_html, 'html.parser')


# In[248]:


#Title for Schiaparelli Hemisphere Enhanced
image_title = soup.find_all("h2", class_ = "title")[0]
title = image_title.contents[0].strip()
title


# In[249]:


# image for Schiaparelli Hemisphere Enhanced
image = soup.find(text="Original")
image_url = image.parent['href']


# In[250]:


# making dict with Schiaparelli Hemisphere Enhanced info
append_to_final_list(title, image_url)
hemisphere_image_urls


# In[251]:


#Cerberus Hemisphere Enhanced

# https://splinter.readthedocs.io/en/latest/drivers/chrome.html
get_ipython().system('which chromedriver')


# In[252]:


executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[253]:


match_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(match_url)


# In[254]:


browser.links.find_by_partial_text("Cerberus Hemisphere Enhanced").click()
seconds = 15
print(f"Sleeping for f{seconds} seconds.")
time.sleep(seconds)
rendered_html = browser.html


# In[255]:


soup = BeautifulSoup(rendered_html, 'html.parser')
image_title = soup.find_all("h2", class_ = "title")[0]
title = image_title.contents[0].strip()
title


# In[256]:


# image for Schiaparelli Hemisphere Enhanced
image = soup.find(text="Original")
image_url = image.parent['href']
image_url


# In[257]:


# making dict with Cerberus Hemisphere Enhanced info
append_to_final_list(title, image_url)
hemisphere_image_urls


# In[258]:


#Syrtis Major Hemisphere Enhanced
# https://splinter.readthedocs.io/en/latest/drivers/chrome.html
get_ipython().system('which chromedriver')


# In[259]:


executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[260]:


match_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(match_url)


# In[261]:


browser.links.find_by_partial_text("Syrtis Major Hemisphere Enhanced").click()
seconds = 15
print(f"Sleeping for f{seconds} seconds.")
time.sleep(seconds)
rendered_html = browser.html


# In[262]:


soup = BeautifulSoup(rendered_html, 'html.parser')
image_title = soup.find_all("h2", class_ = "title")[0]
title = image_title.contents[0].strip()
title


# In[263]:


# image for Syrtis Major Hemisphere Enhanced
image = soup.find(text="Original")
image_url = image.parent['href']
image_url


# In[264]:


# making dict with Syrtis Major Hemisphere Enhanced info
append_to_final_list(title, image_url)
hemisphere_image_urls


# In[265]:


# https://splinter.readthedocs.io/en/latest/drivers/chrome.html
get_ipython().system('which chromedriver')


# In[266]:


executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[267]:


match_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(match_url)


# In[268]:


browser.links.find_by_partial_text("Valles Marineris Hemisphere Enhanced").click()
seconds = 15
print(f"Sleeping for f{seconds} seconds.")
time.sleep(seconds)
rendered_html = browser.html


# In[269]:


soup = BeautifulSoup(rendered_html, 'html.parser')
image_title = soup.find_all("h2", class_ = "title")[0]
title = image_title.contents[0].strip()
title


# In[270]:


# image for Valles Marineris Hemisphere Enhanced
image = soup.find(text="Original")
image_url = image.parent['href']
image_url


# In[271]:


# making dict with Valles Marineris Hemisphere Enhanced info
append_to_final_list(title, image_url)
hemisphere_image_urls


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


# https://splinter.readthedocs.io/en/latest/drivers/chrome.html
get_ipython().system('which chromedriver')


# In[ ]:


executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[ ]:


# Iterate through all pages
for x in range(50):
    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all elements that contain book information
    articles = soup.find_all('article', class_='carousel_item')
    # Iterate through each book

    for article in articles:
        # Use Beautiful Soup's find() method to navigate and retrieve attributes
        style = article.find('style')
        url = style.find("background-image:")
#         href = link['href']
#         title = link['title']
        print(url)
#         print(title)
#         print('http://books.toscrape.com/' + href)














