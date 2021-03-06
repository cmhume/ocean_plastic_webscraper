# Ocean Plastic Pollution Webscraping Project


## Contributors:


Neeraja Jayaraman-[GitHub](https://github.com/Njraman), [Branch](https://github.com/cmhume/ocean_plastic_webscraper/tree/Neeraja)


Corinne Hume-[GitHub](https://github.com/cmhume), [Branch](https://github.com/cmhume/ocean_plastic_webscraper/tree/Corinne)


Manupriya Sharma-[GitHub](https://github.com/Manupriya1), [Branch](https://github.com/cmhume/ocean_plastic_webscraper)


Elaine Ng-[GitHub](https://github.com/ElaineNg94), [Branch](https://github.com/cmhume/ocean_plastic_webscraper/tree/Elaine-tableau)


## Overview:

In this project, we created a webscraping app using Flask to search for recent news articles on ocean plastic pollution.  The project provides background research for a California Benefit Corporation that is a pioneer in developing plastic offsets and reducing ocean plastic pollution.  In addition, we compared the accuracy of results and ease of use for different web scraping libraries and methods.  The different webscraping methods can be seen [here]( https://github.com/cmhume/ocean_plastic_webscraper/blob/93e065bfd33493f98eb600466b23fd544823ca08/scraping_draft_cmh.ipynb) in our webscraping google colab notebook.  Our final web application used the Newspaper3k python library for webscraping. 

## Sources of Data:

The following websites are used as sources for scraping plastic pollution related news:


1. https://news.un.org/
2. https://oceanconservancy.org
3. https://www.nytimes.com
4. https://ellenmacarthurfoundation.org

## Purpose:

The purpose of this project is to collect and display information from multiple websites on a single web based application. Instead of manually browsing through multiple websites, the information from all the sources is made available on the web application with the click of a button. The app will automatically navigate through the sites, scrape information and display the results in an easy to read table.

## Tools and Technologies:

1. Newspaper3k - The python library used for extracting articles from URLs.
2. Python - Programming Language used to create the script to scrape data.
3. MongoDB - A NoSQL DB is used as a flexible option to store the many different types of data that is scraped from the websites in BSON format.
4. Flask- The web framework used to create the web application.
5. Bootstrap - Bootstrap framework and its components are used to build a flexible, mobile responsive web application. 
6. CSS - Stylesheets are used to design the appearance of the web application.

## Application Design:

The following diagram illustrates the architecture and function of the web application.


<img width="1097" alt="design" src="https://user-images.githubusercontent.com/78699521/143925266-cb4dd99b-1d36-4d1e-b695-801bd8a1ce23.png">


## Application Snapshot:

The following is an image of the developed web application.

<img width="1439" alt="webapp" src="https://user-images.githubusercontent.com/78699521/143925079-98564677-2dad-423e-845c-8ce75afcd289.png">


## Project Insights and Challenges:

1. The web page takes a little while to load and display the data after scraping.
2. We decided to use the Newspaper3k library for it's ease of use and ability to add websites without needing to change the web scraping code.
3. Certain websites (such as LinkedIn) did not return relevant results due to the design of the source websites and were removed as datasources.


## Alternate Web Scraping Methods:


We used a google colab notebook to test different methods of webscraping. The google colab notebook is available [here]( https://github.com/cmhume/ocean_plastic_webscraper/blob/93e065bfd33493f98eb600466b23fd544823ca08/scraping_draft_cmh.ipynb) and [here](https://drive.google.com/file/d/1VoPQvdVCFOVKXiej_jaZ2eq2w6RXq-aY/view?usp=sharing).

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


## Scraping data tables from websites


Three types of tables were scraped, an iframe table embedded in the html, a normal html table, and a table in a pdf document.


### Iframe table


To scrape the iframe table we used devops to inspect the page's html and found the link to the iframe table.  We then used this link to scrape data from the document link as shown in the dataframe below:


![iframe_df](https://user-images.githubusercontent.com/78699521/144690792-96a4d10e-f61b-4d5f-a17c-20447b0f60e2.png)



### HTML table


We used the following method to scrape data and save it as a csv file:


![html_table](https://user-images.githubusercontent.com/78699521/144690522-682adf0a-be30-47f4-a342-868ae5be5ece.png)


### PDF table


We use the tabula library to scrape tables found in a pdf document.  The basic method is shown below:


!pip install tabula-py


import tabula


import os


tables = tabula.read_pdf("/content/Brooks_aat0131_SM_L1.pdf", pages="all", output_format="dataframe", stream=True)


An excellent tutorial on using Tabula can be found [here](https://github.com/alod83/data-science/tree/master/DataCollection/PDF)


### Scraping Tables: Conclusions


There are many ways to scrape html tables, we used the simplest method that can be used on most webpages without modifing the code.  Iframe tables are not picked up when looking for the "table" html tags, but can be scraped by visiting the source for the iframe found when inspecting the html of the webpage.  The tabula library is easy to use but does not always pick up every table in a pdf document.  The results from using tabula need to be checked and cleaned after exporting as csv files, some tables are split into multiple files.


## Creating a News Feed 


We created an RSS news feed with https://rss.app/.  We used the free developer version of this service and created our own RSS feed from the following websites:

https://www.nature.com/search?q=ocean%20plastic&order=relevance&date_range=2021-2021

https://phys.org/search/?search=ocean+plastic&s=1


The free version can create two news feeds, allowing one to be used per webpage.  The paid versions allow multiple newsfeeds and the combination of news sources per feed. 

Widget codes:

Phys.org:


<rssapp-carousel id="9ypTyOvk8q9e0DZM"></rssapp-carousel><script src="https://widget.rss.app/v1/carousel.js" type="text/javascript" async></script>


![phys_feed](https://user-images.githubusercontent.com/78699521/144693510-68089a29-4190-4dda-ab06-89d6a139fce8.png)



Nature:

<rssapp-carousel id="CuCIHXEP9XYrg5yK"></rssapp-carousel><script src="https://widget.rss.app/v1/carousel.js" type="text/javascript" async></script>


![nat_feed](https://user-images.githubusercontent.com/78699521/144693518-f208a57c-18ef-40fe-aba4-d172f270f555.png)



In addition to news feeds, rss.app also can be used to send an e-mail digest 


## Creating a Google News Alert and RSS Feed


We created a Google Search RSS feed shown below:


https://news.google.com/rss/search?q=ocean%20plastic&hl=en-US&gl=US&ceid=US%3Aen


This feed can be easily changed for any search results by changing the keywords after q= in the url above.


## Recommendations for the Future:
1. Explore webscraping using Beautiful Soup and Selenium.
2. Improve accuracy of results from scraping websites that redirect to a different page (such as LinkedIn and WWF)

