from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/details')
def model_details():
    return render_template('model_details.html')

@app.route('/predictor')
def predictor():
    return render_template('predictor.html')

@app.route('/bulletin')
def bulletin():
    return render_template('bulletin.html')


if __name__ == "__main__":
    app.run(debug=True)
