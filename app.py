from flask import Flask, render_template, request, redirect

from prediction_pipeline import get_prediction

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


if __name__ == "__main__":
    app.run(debug = True)
