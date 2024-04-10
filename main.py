from flask import Flask, render_template, request
from analyzer import analyze_sentiment
import os

app = Flask(__name__)
app.config['TEMPLATES'] = os.path.join(os.path.dirname(__file__), 'templates')



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        sentiment = analyze_sentiment(text)
    else:
        text = ""
        sentiment = ""
    return render_template('index.html', text=text, sentiment=sentiment)


if __name__ == '__main__':
    app.run(debug=True)