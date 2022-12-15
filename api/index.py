from flask import Flask, request, jsonify,redirect,url_for
from flask_cors import CORS
from snscrape.modules import twitter
import json

# Initialize the Flask application
app = Flask(__name__)

# Enable CORS
CORS(app)

tts = twitter.TwitterTrendsScraper
tss = twitter.TwitterSearchScraper
tus = twitter.TwitterUserScraper

max_results = 100


@app.route('/gettrends', methods=['GET'])
def respond():
    
    
    scraper = tts()
    json_output = []
    for i,tweet in enumerate(scraper.get_items()):
        if i > max_results:
            break
        tweet_json = json.loads(tweet.json())
        if '_type' in tweet_json:
            del tweet_json['_type']
        json_output.append(tweet_json)

    lst = json_output
    
    return jsonify({
        'message': lst
    })

@app.route('/')
def index():
    return redirect(url_for('respond'))
    

@app.route('/search', methods=['GET'])
def searchrespond():
    # Retrieve the query from the url parameter /search?query=

    max_results = 50
    query = request.args.get('query')
    scraper = tss(query.replace("+"," "))
    json_output = []
    for i,tweet in enumerate(scraper.get_items()):
        if i > max_results:
            break
        tweet_json = json.loads(tweet.json())
        if '_type' in tweet_json:
            del tweet_json["_type"]
        json_output.append(tweet_json)

    lst = json_output
    
    return jsonify({
        'message': lst
    })


@app.route('/user', methods=['GET'])
def userrespond():
    # Retrieve the username from the url parameter /user?username=
    
    scraper = tus(request.args.get('username',False))
    json_output = []
    for i,tweet in enumerate(scraper.get_items()):
        if i > max_results:
            break
        tweet_json = json.loads(tweet.json())
        if '_type' in tweet_json:
            del tweet_json['_type']
        json_output.append(tweet_json)

    lst = json_output
    
    return jsonify({
        'message': lst
    })
  
@app.route('/hashtag', methods=['GET'])
def hashtagrespond():
    # Retrieve the hashtag from the url parameter /hashtag?query=
    
    scraper = tss("#"+request.args.get('query'))
    json_output = []
    for i,tweet in enumerate(scraper.get_items()):
        if i > max_results:
            break
        tweet_json = json.loads(tweet.json())
        if '_type' in tweet_json:
            del tweet_json['_type']
        json_output.append(tweet_json)

    lst = json_output
    
    return jsonify({
        'message': lst
    })
