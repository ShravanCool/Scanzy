from flask import Flask, render_template, url_for
from predict import predict

app = Flask(__name__)
model_path = './models/baseline.h5'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/details')
def model_details():
    return render_template('model_details.html')

@app.route('/predictor')
def predictor():
    return render_template('predictor.html')

@app.route('/predictor', methods=['POST'])
def predictor():
    if request.method == 'POST':
        f = request.files['file']

        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, 'uploads', f.filename)
        f.save(file_path)

        pred = predict(file_path, model_path)
        return render_template('predictor.html', pred=pred)

@app.route('/bulletin')
def bulletin():
    return render_template('bulletin.html')


if __name__ == "__main__":
    app.run(debug=True)
