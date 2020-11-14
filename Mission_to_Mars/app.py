from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
# Create an instance of our Flask app.
app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars")

# Connect to a database. Will create one if not already available.
db = mongo.mars_db
collection = db.items



# Set route
@app.route('/')
def index():
    #find record of data
    mars_data = collection.find_one()


    # Return the template with the teams list passed in
    return render_template('index.html', mars_data = mars_data)


@app.route('/scrape')
def scrape():
    result = scrape_mars.scraping()
    collection.insert_one(result)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
