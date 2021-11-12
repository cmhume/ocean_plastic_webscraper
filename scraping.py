# Imports for Newspaper3k Library
import newspaper
from newspaper import Article
from newspaper import Source
from newspaper import news_pool
import pandas as pd
import nltk
nltk.download('punkt')
def scrape_all():
    # Run all scraping functions and store results in a dictionary
    data = {
        "ocean_scrape": ocean_scrape()
    }

    # Return data
    return data

def ocean_scrape():

    # Example from https://andrewhnberry.github.io/articles/2020-04/The-Easy-Way-to-Web-Scrape-Articles-Online

    un = newspaper.build('https://news.un.org/en/search/ocean%20plastic', memoize_articles=False)
    oc = newspaper.build('https://oceanconservancy.org/newsroom/press-releases/?_search=ocean%20plastic', memoize_articles=False)
    nyt = newspaper.build('https://www.nytimes.com/search?dropmab=false&query=ocean%20plastic&sort=newest', memoize_articles=False) 
    emf = newspaper.build("https://ellenmacarthurfoundation.org/topics/plastics/latest-content", memoize_articles=False) 
    #wwf = newspaper.build("https://www.worldwildlife.org/search?cx=003443374396369277624%3Av3nraqhmeyk&ie=UTF-8&x=ocean+plastic&cat=stories#gsc.tab=0&gsc.q=ocean%20plastic&gsc.sort=date", memoize_articles=False)  
    papers = [un, oc, emf, nyt]
    news_pool.set(papers, threads_per_source=5)
    news_pool.join()

    #Create our final dataframe
    final_df = pd.DataFrame()

    #Create a download limit per sources
    limit = 25

    for source in papers:
    #temporary lists to store each element we want to extract
        list_title = []
        list_authors = []
        list_url = []
        list_summary = []
        list_date = []

        count = 0
        for article_extract in source.articles:
            article_extract.download()
            article_extract.parse()
            article_extract.nlp()

            if count > limit: #Lets have a limit, so it doesnt take too long when you're
                break         #running the code.
            #appending the elements we want to extract
            list_title.append(article_extract.title)
            list_summary.append(article_extract.summary)
            list_authors.append(article_extract.authors)
            list_url.append(article_extract.url)
            list_date.append(article_extract.publish_date)
            #Update count
            count +=1

        temp_df = pd.DataFrame({'Date': list_date, 'Title': list_title, 'URL': list_url, 'Summary': list_summary, 'Authors': list_authors})
        #Append to the final DataFrame
        df = final_df.append(temp_df, ignore_index = True)
        print(df)

    # Convert dataframe into HTML format, add bootstrap
    return df.to_html(classes="table")
   
if __name__ == "__main__":
    # If running as script, print scraped data
    print(scrape_all()) 