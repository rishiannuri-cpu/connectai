from flask import Flask,request,jsonify
from flask_cors import CORS
from textblob import TextBlob

app = Flask(__name__)
CORS(app)

@app.route("/ai",methods=["POST"])
def ai():
 text=request.json["text"]
 polarity=TextBlob(text).sentiment.polarity

 if polarity>0:
  r="Positive Emotion"
 elif polarity<0:
  r="Negative Emotion"
 else:
  r="Neutral Emotion"

 return jsonify({"result":r})

app.run()

