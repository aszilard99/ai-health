from flask import Flask, flash, request, redirect
from InferenceService import predict, isImageGrayscale, isValidImageSize

app = Flask(__name__)
app.secret_key = "super secret key"

ALLOWED_EXTENSIONS = {'jpg', 'jpeg'}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/predict', methods=['GET', 'POST'])
def getPrediction():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            if allowed_file(file.filename):
                if not isValidImageSize(file):
                    return "Image resolution too small, it has to be atleast 50x50x3", 472
                if not isImageGrayscale(file):
                    return "Image has to be grayscale", 415
                res = predict(file)
                return f"{res}"
            else:
                flash('File extension not allowed')
                return "File extension is not supported", 422


if __name__ == "__main__":
    app.run(debug=True)
