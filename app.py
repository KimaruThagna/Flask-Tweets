from flask import Flask,render_template,request,jsonify
import tweepy as tw
import os
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
app = Flask(__name__)
# twitter authentication
auth = tw.OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
auth.set_access_token(os.environ["ACCESS_TOKEN"], os.environ["ACCESS_TOKEN_SECRET"])
api = tw.API(auth, wait_on_rate_limit=True)
api = ""
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/search",methods=["POST"])
def search():
    search_tweet = request.form.get("tweet_search")
    textblob_scores = []
    vader_scores = []
    tweets = api.search(search_tweet, tweet_mode='extended')

    for tweet in tweets:
        polarity = TextBlob(tweet.full_text).sentiment.polarity
        subjectivity = TextBlob(tweet.full_text).sentiment.subjectivity
        textblob_scores.append([tweet.full_text,polarity,subjectivity])
        # using Vader sentiment analysis library
        score = analyzer.polarity_scores(tweet.full_text)  # obtain polarity index of given sentence.
        vader_scores.append([tweet.full_text, score])

    return jsonify({"success":True,"tweet_analysis_textBlob":textblob_scores, "tweet_Analysis_Vader":vader_scores})

app.run()