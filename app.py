from flask import Flask,render_template,request,jsonify
import tweepy
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

app.run()