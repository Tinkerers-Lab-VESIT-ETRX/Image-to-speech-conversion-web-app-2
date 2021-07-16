'''from flask import *  
app = Flask(__name__)  
 
@app.route('/')  
def upload():  
    return render_template("file_upload_form.html")  
 
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']  
        f.save(f.filename)  
        return render_template("success.html", name = f.filename)  
  
if __name__ == '__main__':  
    app.run(debug = True) '''

'''from flask import Flask
import os
import cv2

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

 @app.route("/success")   
def main():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'there is no image in the form'
        f = request.files['file']
        f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(f)
        dang = cv2.imread(UPLOAD_FOLDER+"/"+file.filename)
        os.remove(UPLOAD_FOLDER+"/"+file.filename)
       



	return render_template('index.html')'''

from flask import Flask,render_template,request
import os,pytesseract
from flask_uploads import UploadSet, IMAGES
from PIL import Image

project_dir = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__,static_url_path='',static_folder='static',template_folder='templates')

photos = UploadSet('photos',IMAGES)

app.config['DEBUG'] = True
app.config['UPLOAD_FOLDER'] = 'images'

class GetText(object):
    def __init__(self,file):
        self.file = pytesseract.image_to_string(Image.open(project_dir + '/images/' + file))

@app.route('/',methods = ['GET', 'POST'] )
def home():
    if request.method == 'POST':
        if 'photo' not in request.files:
            return 'there is no photo in form'
        name = request.form['img-name'] + '.jpg'
        photo = request.files['photo']
        path = os.path.join(app.config['UPLOAD_FOLDER'],name)
        photo.save(path)

        textObject = GetText(name)

        return textObject.file
    return render_template('index.html')

if __name__ == '__main__':
    app.run()