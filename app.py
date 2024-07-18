from flask import Flask, render_template, jsonify
import os
import praw

app = Flask(__name__)

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT"),
    client_secret=os.getenv("REDDIT_SECRET"),
    user_agent="web:firefox:1.0 (by /u/ThenAlternative6646)",
    username="ThenAlternative6646",
    password=os.getenv("REDDIT_PASSWORD")
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/trigger_action', methods=['POST'])
def trigger_action():
    # Perform any Python operations here
    # Example: print a message to the console
    reddit.subreddit("bearbrest").submit("Perfect", url="https://img2.hotnessrater.com/2724449/mia-khalifa-porn.jpg?w=4000&h=6000")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
