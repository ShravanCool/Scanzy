from flask import Flask, render_template, url_for, request, flash, redirect
from predict import predict
import os

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
model_path = './models/baseline.h5'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/details')
def model_details():
    return render_template('model_details.html')

# @app.route('/predictor')
# def predictor():
    # return render_template('predictor.html')

@app.route('/predictor', methods=['GET', 'POST'])
def predictor():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        f = request.files['file']

        if f.filename == '':
            flash('No file selected')
            return redirect(request.url)

        if f and allowed_file(f.filename):
            # f = secure_filename(f.filename)
            basepath = os.path.dirname(__file__)
            file_path = os.path.join(basepath, UPLOAD_FOLDER, f.filename)
            f.save(file_path)
            pred = predict(file_path, model_path)
            return render_template('predictor.html', pred=pred)
        else:
            flash('File Extension does not match!!')
            return redirect(request.url)
    else:
        return render_template('predictor.html')



@app.route('/bulletin')
def bulletin():
    return render_template('bulletin.html')


if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)
