# Ocean Plastic Webscraper plastic_app.py

# Import dependencies
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

# Set up Flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/plastic_app"
mongo = PyMongo(app)

@app.route("/")
def index():
   print('Start here:')
   news = mongo.db.news.find_one()
   print('Ocean Plastic News')
   return render_template("index.html", news=news)

@app.route("/scrape")
def scrape():
   news = mongo.db.news
   news_data = scraping.scrape_all()
   news.update({}, news_data, upsert=True)
   return redirect('/', code=302)

if __name__ == "__main__":
   app.run()