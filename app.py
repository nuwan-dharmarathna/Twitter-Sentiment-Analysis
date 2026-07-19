from flask import Flask, jsonify, redirect, render_template, request

from prediction_pipeline import get_prediction
from xquik_export import load_xquik_rows

from logger import logging

data  = '--Your Comment Status--'

app = Flask(__name__)

logging.info('Flask server Started')

@app.route('/')
def index():
    logging.info('========== Open Home Page ==========')
    
    return render_template('index.html', data = data)

@app.route('/', methods=['post'])
def my_post():
    comment = request.form["text"]
    result = get_prediction(comment)
    
    global data
    
    if result == 'Negative Comment':
        data = 'Negative Comment 👎'
    else:
        data = 'Positive Comment 👍'
    
    return redirect(request.url)


@app.route('/xquik-export', methods=['POST'])
def analyze_xquik_export():
    rows = load_xquik_rows(request.get_data())
    results = [
        {
            "tweet": row["tweet"],
            "sentiment": get_prediction(row["tweet"]),
            "created_at": row["created_at"],
            "username": row["username"],
        }
        for row in rows
    ]
    return jsonify({"count": len(results), "results": results})


if __name__ == "__main__":
    app.run(debug = True)
