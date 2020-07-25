import os, sys
from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory
from tensorflow.python.keras.layers.preprocessing.image_preprocessing import RandomZoom
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import tensorflow as tf
# from dotenv import load_dotenv
# from tensorflow.keras.preprocessing.image import array_to_img # test

app = Flask(__name__)

# load_dotenv()
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
H5_MODEl = 'generator_model_10000.h5'

# disable eager mode
# tf.compat.v1.disable_eager_execution()

# model = load_model('obama_smalling_201908.h5')
model = load_model(H5_MODEl, compile=False)
# model.load_weights('generator_model_weights_10000.h5')
# adds
# graph = tf.compat.v1.get_default_graph()

# Run Flask()
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def is_allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return redirect(url_for('generate'))

# 追加
@app.route('/generate', methods=['GET', 'POST'])
def generate():
    """POSTされた場合のみgeneratorに対して乱数を入力、画像を生成する
    """
    if request.method == 'POST':
        # with graph.as_default():
        '''
        with tf.compat.v1.Session() as sess:
            # 重みの初期化
            # session = tf.compat.v1.keras.backend.get_session()
            init = tf.compat.v1.global_variables_initializer()
            sess.run(init)
            # run Prediction
            latent_dim = 32
            random_latent_vectors = np.random.normal(size=(10, latent_dim))
            generated_images = model.predict(random_latent_vectors)
        '''
        # 2.0 run
        latent_dim = 32
        random_latent_vectors = np.random.normal(size=(10, latent_dim))
        generated_images = model.predict(random_latent_vectors)

        # 結果の変換
        resultmsg = np.uint8(generated_images[0]*255.)
        # resultImg = array_to_img(generated_images[0] * 255., scale=False)
        resultImg = Image.fromarray(resultmsg)
        resultImg = resultImg.resize(
            (int(resultImg.width*10), int(resultImg.height*10))
            )
        filepath = './uploads/generated.jpg'
        resultImg.save(filepath)
        return render_template(
            'result.html', resultmsg=resultmsg, filepath=filepath)
    return render_template('generate.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file.')
            return redirect(url_for('predict'))
        file = request.files['file']
        if file.filename == '':
            flash('No file.')
            return redirect(url_for('predict'))
        if file and is_allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            
            img = Image.open(filepath).convert('RGB')
            img = img.resize((150, 150))
            x = np.array(img, dtype=np.float32)
            x = x / 255.
            x = x.reshape((1,) + x.shape)
            
            global graph  # これグローバル変数か…
            with graph.as_default():
                session = tf.compat.v1.keras.backend.get_session()
                init = tf.compat.v1.global_variables_initializer()
                session.run(init)
                # prediction
                pred = model.predict(x, batch_size=1, verbose=0)
                score = pred[0][0]
                if(score >= 0.5):
                    person = 'Smalling'
                else:
                    person = 'Obama'
                    score = 1 - score

            resultmsg = '[{}] {:.4%} Sure.'.format(person, score)
            
            return render_template('result.html', resultmsg=resultmsg, filepath=filepath)
    return render_template('predict.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    # app.run()
    app.run(host='127.0.0.1', port=8080, debug=True)