# Ocean Plastic Webscraper
# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt
from webdriver_manager.chrome import ChromeDriverManager


def scrape_all():
    # Initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    emf_title, emf_paragraph = emf_news(browser)

    nyt_title, nyt_paragraph, nyt_title_2, nyt_paragraph_2 = nyt_news(browser)

    # Run all scraping functions and store results in a dictionary
    data = {
        "emf_title": emf_title,
        "emf_paragraph": emf_paragraph,
        # "emf_link": emf_link,
        # "emf_pic": emf_pic,
        "nyt_title": nyt_title,
        "nyt_paragraph": nyt_paragraph,
        "nyt_title_2": nyt_title_2,
        "nyt_paragraph_2": nyt_paragraph_2,
         
        # "nyt_link": nyt_link,
        # "nyt_pic": nyt_pic,
        "last_modified": dt.datetime.now()
    }

    # Stop webdriver and return data
    browser.quit()
    return data


def emf_news(browser):
# visit the Ellen Mcarthur Foundation website
    url = "https://ellenmacarthurfoundation.org/topics/plastics/latest-content"
    browser.visit(url)

# Optional delay for loading the page
    browser.is_element_present_by_css('div.tiles-container', wait_time=1)

    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    #html tags
    #<div class="text-content"><h4 class="tile-title css-rmwpnv e15dqdia11">The solution to plastic pollution</h4>
    # <p class="css-1o3qgj6 e15dqdia8">One of the most analytically robust studies produced on ocean plastics.</p></div>
    
    try:
        # Scrape the First News Title
        emf_title = news_soup.find('h4').get_text()
        # Use the parent element to find the paragraph text
        emf_paragraph = news_soup.find('div', class_="css-1o3qgj6 e15dqdia8").get_text()

    except AttributeError:
        return None, None

    return emf_title, emf_paragraph


def nyt_news(browser):
    # Visit URL
    url = 'https://www.nytimes.com/search?dropmab=false&endDate=20211008&query=ocean%20plastic&sort=best&startDate=20211001'
    browser.visit(url)
    # Optional wait time.
    browser.is_element_present_by_css('div.css-46b038', wait_time=1)
    # Find and click the date range button
    # <label class="css-1gd5qnr"><span class="css-1ly73wi e1tej78p0">Refine results via </span>Date Range</label>
    # <button type="button" value="Past Week" class="css-jba1a6 selected" aria-label="Past Week">Past Week</button>
    #date_range = browser.find_by_tag('button')[1]
    #date_range.click()

    # Find and click "Past Week" from drop down menu
    #past_week = browser.find_by_tag('button')[3]
    #past_week.click()
  
    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    nyt_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    #html tags
    # #site-content > div > div:nth-child(2) > div
    # 
    #<div class="text-content"><h4 class="tile-title css-rmwpnv e15dqdia11">The solution to plastic pollution</h4>
    # <p class="css-1o3qgj6 e15dqdia8">One of the most analytically robust studies produced on ocean plastics.</p></div>
    
    try:
        # Use the parent element to find the first 'a' tag and save it as 'news_title'
        nyt_title = nyt_soup.find('div', class_="tile-title css-rmwpnv e15dqdia11").get_text()
        # Use the parent element to find the paragraph text
        nyt_paragraph = nyt_soup.find('div', class_="css-1o3qgj6 e15dqdia8").get_text()
         # Use the parent element to find the first 'a' tag and save it as 'nyt_title_2' 
         # <h4 class="css-2fgx4k">Indra Nooyi, Ex-C.E.O. of Pepsi, Thinks Big Business Can Do Better</h4>
        nyt_title_2 = nyt_soup.find('div', class_="css-2fgx4k").get_text()
        # Use the parent element to find the paragraph text
        # <p class="css-16nhkrn">“It’s not about giving away money we’ve made. It’s about how we make money a different way.”</p>
        nyt_paragraph_2 = nyt_soup.find('div', class_="css-16nhkrn").get_text()

    except AttributeError:
        return None, None, None, None

    return nyt_title, nyt_paragraph, nyt_title_2, nyt_paragraph_2 


if __name__ == "__main__":

    # If running as script, print scraped data
    print(scrape_all())
