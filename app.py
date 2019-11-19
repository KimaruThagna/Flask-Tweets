from flask import Flask,render_template,request,jsonify
import tweepy, os
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
app = Flask(__name__)
# twitter authentication
auth = tw.OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
auth.set_access_token(os.environ["ACCESS_TOKEN"], os.environ["ACCESS_TOKEN_SECRET"])
api = tw.API(auth, wait_on_rate_limit=True)

@app.route("/")
def index():
    return render_template('index.html')

app.run()