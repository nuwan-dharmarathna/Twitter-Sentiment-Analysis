from flask import Flask, render_template, request, redirect

from prediction_pipeline import get_prediction

data  = 'print weyan hutto'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', data = data)

@app.route('/', methods=['post'])
def my_post():
    text = request.form["text"]
    print(text)
    result = get_prediction(text)
    
    if result == 'Negative Comment':
        data = 'Negative Comment 👎'
    else:
        data = 'Positive Comment 👍'
    
    return redirect(request.url)


if __name__ == "__main__":
    app.run(debug = True)
