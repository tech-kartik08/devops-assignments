from flask import Flask,request,render_template,jsonify
import os
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv

# mongo URI
load_dotenv()
uri=os.getenv("ASS_URI")

# connect mongodb

client = MongoClient(uri)
try:
    client.admin.command('ping')
    print("MongoDB Connected")
except Exception as e:
    print("error Occured: ",e)

# choose db and collection
db = client['assignment-db']
collection = db['ass-data']

# flask application
app = Flask(__name__)

# home page
@app.route('/')
def home():

    return render_template('index.html')

# after submission
@app.route('/submit' , methods=['POST'])
def submit():

    form_data = dict(request.form)
    
    if not form_data.get('name') or not form_data.get('email'):
        error='Name and email are required'
        return render_template('index.html', error=error,form_data=form_data)

    collection.insert_one(form_data)
    name = form_data.get('name','user')
    return f"Hello {name} , your data has been successfuly submitted"

# get data
@app.route('/api')
def get_data():
    data = list(collection.find({},{'_id': 0}))
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)