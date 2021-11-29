# Ocean Plastic Pollution Webscraping Project

## Overview:

In this project, we created a webscraping app using Flask to search for recent news articles on ocean plastic pollution.  The project provides background research for a California Benefit Corporation that pioneers in plastic offsets and saving the oceans from plastic pollution.  In addition, we compared the accuracy of results and ease of use for different web scraping libraries and methods.  The different webscraping methods can be seen here in our webscraping google colab notebook.  Our final web application used the Newspaper3k python library for webscraping. 

## Sources of Data:

The following websites have been used as sources for scraping plastic pollution related news:


1. https://news.un.org/
2. https://oceanconservancy.org
3. https://www.nytimes.com
4. https://ellenmacarthurfoundation.org

## Purpose:

The purpose of this project is to collect and display information from multiple websites on a single web based application. Instead of manually browsing through multiple websites, the information from all of the sources will be available on the web application through the click of a button. The app will automatically navigate through the sites, scrape information and display the results in an easy to read table.

## Tools and Technologies:

1. Newspaper3k: Newspaper3k is the python library that is used for extracting articles from URLs.
2. Python - Programming Language used to create the script to scrape data.
3. MongoDB - a NoSQL DB has been used as a flexible option to store the many different types of data that is scraped from the websites in BSON format.
4. Flask- The web framework used to create the web application.
5. Bootstrap - Bootstrap framework and its components have been used to build a flexible, mobile responsive web application. 
6. CSS - Stylesheets have been used to design the appearance of the web application.

## Application Design:

The following diagram illustrates the architecture and working of the web application.


<img width="1097" alt="design" src="https://user-images.githubusercontent.com/78699521/143925266-cb4dd99b-1d36-4d1e-b695-801bd8a1ce23.png">


## Application Snapshot:

The following is an image of the developed web application.

<img width="1439" alt="webapp" src="https://user-images.githubusercontent.com/78699521/143925079-98564677-2dad-423e-845c-8ce75afcd289.png">


## Project Learnings and Challenges:

1. The web page takes a little while to load and display the data after scraping.
2. We decided on using the Newspaper3k library for it's ease of use and ability to add websites without needing to change the web scraping code.
3. Certain websites (such as LinkedIn) did not return the required results due to the design of the source websites and were removed from the preferred datasources.


## Alternate Web Scraping Methods:


We used a google colab notebook to test different methods of webscraping. The google colab notebook is available [here]( https://github.com/cmhume/ocean_plastic_webscraper/blob/93e065bfd33493f98eb600466b23fd544823ca08/scraping_draft_cmh.ipynb)

### First Steps:


First we checked the robots.txt files for each website to see if web scraping was allowed.  This was done by adding /robots.txt to the main web page address like so:


https://www.un.org/robots.txt


https://www.worldwildlife.org/robots.txt


https://oceanconservancy.org/robots.txt


https://www.linkedin.com/robots.txt


https://ellenmacarthurfoundation.org/robots.txt


https://www.nytimes.com/robots.txt


With the robots.txt files we discovered the New York Times prefers web scrapers to use rss feeds and REST APIs for article information and LinkedIn does not like most types of web scraping.


### APIs


#### NewsAPI: https://newsapi.org/


We used the free developer version of NewsAPI, a JSON API service that searches multiple news sources from across the web.  After creating an API key we used the following code to search for articles about ocean plastic:


![news_api](https://user-images.githubusercontent.com/78699521/143921707-a6d52ad3-379a-455e-9c6b-b62b89902dff.png)



Search criteria is placed in the parameters' "q" section.  Details for using NewsAPI can be found on their website and information on using the python NewsAPI library is available here: https://github.com/mattlisiv/newsapi-python


The final table of our results was as follows:


![news_api_df](https://user-images.githubusercontent.com/78699521/143921657-91cb4c13-b33d-4099-9511-103f70541161.png)


#### New York Times API: https://developer.nytimes.com/apis

After creating an account and registering an App on developer.nytimes.com, we added an API key and enabled the Article Search and RSS feed APIs to our App.  We used the following code to retrieve article search results in JSON format, search criteria are after the 'q=' in the url:


![nyt_api](https://user-images.githubusercontent.com/78699521/143924682-5c2fa799-5918-4d00-9717-facdc87ed232.png)


The NYT JSON output had a lot more nested metadata than the previous NewsAPI and was a little harder to parse through, our final dataframe was simplified to just show the article abstract and link as shown below:


![nyt_df](https://user-images.githubusercontent.com/78699521/143922578-cbc7065d-5922-4652-bb7b-17e4b047bb49.png)


### API Conclusions


NewsApi is a great resource for personal use.  It is easy to use and change search criteria and provided interesting results from news sources from around the world.  For business use, NewsAPI is quite expensive especially for small businesses.  The New York Times API had so much nested metadata it was hard to parse through and printing out the JSON results took up a lot of space.  The information about word count, rank, and keywords the JSON output contained could be used in an analysis about news article features.  There may be a simpler way to parse through the New York Times API of which we are not aware.


## Recommendations for Future:
1. Explore webscraping and generating results using Beautiful Soup and  Selenium.
2. Explore webscraping and generating accurate results from websites that redirect to a different page (such as LinkedIn and WWF)
3. Explore ways to scrape data from PDFs on the web.
4. Adding a News feed on the page.




