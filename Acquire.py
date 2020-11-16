################################# Acquire Web Scraping Module #################################

# imports used in functions
import pandas as pd
from requests import get
from bs4 import BeautifulSoup
import os

################################ Acquire Codeup Blog Articles #################################
def get_blog_articles(urls, cached = False):
    '''
    Function to scape articles from Codeup Blog; If cached == False, runs code to scrape data
    from chosen url articles, add to dictionary, save as df in json file. If cached == True,
    reads the saved json file to a df.
    '''
    # if we already have the data and cached == True, read it locally
    if cached == True:
        df = pd.read_json('blogs.json')
    
    # if we don't have the data or we want to resave with any new data
    else:
        blogs = []
    
        # loops through urls passed in function
        for blog in urls:

            # web scraping
            headers = {'User-Agent': 'Codeup Data Science'}
            response = get(blog, headers=headers)
            # takes URL and returns a soup object of the text
            soup = BeautifulSoup(response.text)
            article = soup.find('div', class_='jupiterx-post-content')

            # creates empty dictionary to hold the article title and content
            article_dict = {'title':[], 'content':[]}
            # adds title to dict
            article_dict['title'] = soup.title.string
            # adds article to dict
            article_dict['content'] = article.text
        
            # adds this dict of the article to the blog list
            blogs.append(article_dict)
        
        # save it for next time
        blogs = pd.DataFrame(blogs)
        blogs.to_json('blogs.json')
        
    return blogs

    ################################ Acquire Codeup Blog Articles #################################
    def get_inshorts_data():

        