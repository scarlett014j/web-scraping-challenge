import scrape_mars
from flask import Flask, render_template
from flask_pymongo import PyMongo

# Create an instance of our Flask app.
app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = client.mars_db
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
    result = scrape_mars.scrape_info()
    collection.insert_one(result)
    return redirect('/', code = 302)

if __name__ == "__main__":
    app.run(debug=True)
