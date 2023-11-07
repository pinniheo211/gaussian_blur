from flask import Flask, request, render_template, jsonify , send_from_directory
import os
import cv2
from werkzeug.utils import secure_filename
app = Flask(__name__)

UPLOAD_FOLDER = os.path.join('static', 'uploads')
SAVE_FOLDER = os.path.join('static', 'saveimages')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SAVE_FOLDER'] = SAVE_FOLDER

def remove_background(image_path, blur_value):
    img = cv2.imread(image_path)
    blurred_img = cv2.GaussianBlur(img, (blur_value, blur_value), 0)
    return blurred_img

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/feature')
def feature():
    return render_template('feature.html')

@app.route('/remove_background', methods=['POST'])
def remove_background_route():
    if 'file' not in request.files:
        return jsonify({"success": False, "message": "No file part"})

    file = request.files['file']
    if file.filename == '':
        return jsonify({"success": False, "message": "No selected file"})

    try:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        img_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        return jsonify({"success": True, "image_path": img_path})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})

@app.route('/apply_blur', methods=['POST'])
def apply_blur():
    try:
        blur_value = int(request.json.get('blur', 200))
        if blur_value < 1:
            blur_value = 1
        if blur_value > 200:
            blur_value = 200

        image_path = os.path.join(app.config['UPLOAD_FOLDER'], os.listdir(app.config['UPLOAD_FOLDER'])[0])
        processed_image = remove_background(image_path, blur_value)

        result_filename = 'processed_' + os.path.basename(image_path)

        result_img_path = os.path.join(app.config['SAVE_FOLDER'], result_filename)
        cv2.imwrite(result_img_path, processed_image)

        return jsonify({"success": True, "image_path": result_img_path})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})




if __name__ == '__main__':
    app.run()