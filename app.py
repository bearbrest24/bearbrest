from flask import Flask, render_template, request, jsonify
import os
import praw

app = Flask(__name__)

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT"),
    client_secret=os.getenv("REDDIT_SECRET"),
    user_agent="web:firefox:1.0 (by /u/Holiday-Disk-4732)",
    username="Holiday-Disk-4732",
    password=os.getenv("REDDIT_PASSWORD")
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/trigger_action', methods=['POST'])
def trigger_action():
    data = request.get_json()
    input_text1 = data.get('input_text1', '')
    input_text2 = data.get('input_text2', '')
    # Perform any Python operations with the input_text1 and input_text2 here
    print(f"Received input text1: {input_text1}")
    print(f"Received input text2: {input_text2}")
    reddit.subreddit("bearbrest_archive").submit(title=input_text1, url=input_text2)

    return jsonify({'status': 'Action triggered successfully!', 'input_text1': input_text1, 'input_text2': input_text2})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
