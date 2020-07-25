import os
# from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory
from flask import Flask, request, redirect, url_for, render_template, send_from_directory
# from tensorflow.python.keras.layers.preprocessing.image_preprocessing import RandomZoom
# from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
# import tensorflow as tf

app = Flask(__name__)

# load_dotenv()
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
H5_MODEl = 'generator_model_10000.h5'

model = load_model(H5_MODEl, compile=False)

# Run Flask()
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 静的ファイル対策
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


@app.route('/')
def index():
    return redirect(url_for('generate'))

# 追加
@app.route('/generate', methods=['GET', 'POST'])
def generate():
    """POSTされた場合のみgeneratorに対して乱数を入力、画像を生成する
    """
    if request.method == 'POST':
        # load model and run
        latent_dim = 32
        random_latent_vectors = np.random.normal(size=(10, latent_dim))
        generated_images = model.predict(random_latent_vectors)

        # 結果の変換
        resultmsg = np.uint8(generated_images[0]*255.)
        resultImg = Image.fromarray(resultmsg)
        resultImg = resultImg.resize(
            (int(resultImg.width*10), int(resultImg.height*10))
            )
        filepath = './static/uploads/generated.jpg'
        resultImg.save(filepath)
        return render_template(
            'result.html', resultmsg=resultmsg, filepath=filepath)
    return render_template('generate.html')


@app.route('/static/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    # app.run()
    app.run(host='127.0.0.1', port=8080, debug=True)