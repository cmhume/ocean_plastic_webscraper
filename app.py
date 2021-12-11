from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/ocean_app"
mongo = PyMongo(app)

@app.route("/")
def index():
   ocean = mongo.db.ocean.find_one()
   return render_template("index.html", ocean=ocean)

@app.route("/scrape")
def scrape():
   ocean = mongo.db.ocean
   ocean_data = scraping.scrape_all()
   ocean.update({}, ocean_data, upsert=True)
   return redirect('/', code=302)

if __name__ == "__main__":
   app.run()