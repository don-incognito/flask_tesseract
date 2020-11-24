# By Julio Daniel 12 November 2020

from flask import Flask, render_template, request

from Flaskr.function_ocr import ocr_core

# folder to store and later server the image
UPLOAD_FOLDER = '/static/uploads'

# allow files of a specific type
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/')
# def home_page():
#     return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':

        if 'file' not in request.files:
            return render_template('upload.html', msg='File not found')
        file = request.files['file']

        if file.filename =='':
            return render_template('upload.html', msg='No file selected')

        if file and allowed_file(file.filename):

            extracted_text = ocr_core(file)

            return render_template('upload.html', msg='Successfully processed',
                                   extracted_text=extracted_text,
                                   img_src= UPLOAD_FOLDER + file.filename)
    elif request.method == 'GET':
        return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)


    #  https://github.com/ro6ley/python-ocr-example