from flask import Flask
import json
from scrape_mars import scrape
import pymongo
from bson.json_util import dumps
from jinja2 import Environment, FileSystemLoader
from flask import Markup

app = Flask(__name__)

templateLoader = FileSystemLoader(searchpath="./templates")
env = Environment(loader=templateLoader)

# Establish connection to local host 27017
conn = 'mongodb://localhost:27017'

# Connect to MongoClient
client = pymongo.MongoClient(conn)

# Begin by dropping any previous version of the MongoDB instance.
# client.drop_database('scrape_mars')

# Create database by naming db here
db = client.scrape_mars

# Create collection by naming collection here
collection = db.data


@app.route('/scrape')
def new_data():
    try:
        data = scrape()
        collection.insert_one(data)
    except:
        return json.dumps({'success': False}), 500, {'ContentType': 'application/json'}
    else:
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route("/")
def index():
    new_data = collection.find().limit(1)
    response = list(new_data)[0]

    template = env.get_template('index.html')

    return template.render(
        news_p=response['news_p'],
        news_title=response['news_title'],
        featured_image=response['featured_image'],
        hemisphere_image_urls=response['hemisphere_image_urls'],
        facts_table=Markup(response['mars_facts'].replace(
            "border=\"1\"", "").replace("dataframe", "table-sm table table-striped"))
    )
    # return dumps({'success': list(new_data)}), 200, {'ContentType': 'application/json'}


if __name__ == '__main__':
    app.run()
