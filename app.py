from fileinput import filename
from random import randint
import numpy
import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file_post():
   if request.method == 'POST':
      f = request.files['file']
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename("1.PNG")))
      file = open(r'C:\\Users\\kulvir\\Desktop\\DEV\\Flask-Image\\ENCRYPT.py', 'r').read()
      exec(file)
      return redirect(url_for('static', filename='uploads/' + "encrypted.PNG"), code=301)

@app.route('/decrypt')
def upload_encrypted_image():
    return render_template('decrypt.html')

@app.route('/decrypter', methods = ['GET', 'POST'])
def decrypt_image():
    if request.method == 'POST':
        im = request.files['file']
        key = request.files['keys']
        im.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename("2.PNG")))
        key.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename("keys.txt")))
        file = open(r'C:\\Users\\kulvir\\Desktop\\DEV\\Flask-Image\\DECRYPT.py', 'r').read()
        exec(file)

		
if __name__ == '__main__':
   app.run(debug = True)