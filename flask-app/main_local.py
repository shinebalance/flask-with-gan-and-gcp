import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image

app = Flask(__name__)

# h5モデルファイルの読み込み
# H5_MODEl = 'cifar-10_airplane_model_5000.h5'
# H5_MODEl = 'cifar-10_airplane_model_10000.h5'
# H5_MODEl = 'cifar-10_airplane_model_20000.h5'
# H5_MODEl = 'cifar-10_airplane_model_30000.h5'
H5_MODEl = 'model_cifar-10_ship.h5'

model = load_model(H5_MODEl, compile=False)

# Run Flask()
app = Flask(__name__)

# @app.context_processor:テンプレート共通で利用したい関数を置く
# 静的ファイル対策(static)
@app.context_processor
def override_url_for():
    """url_for()をdated_url_forでオーバーライド
    """
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    """endpoint==staticのときのみファイルクエリにタイムスタンプを付加する
    """
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


@app.route('./tmp/<filename>')
def uploaded_file(filename):
    return send_from_directory('/tmp', filename)


@app.route('/generate', methods=['GET', 'POST'])
def generate():
    """POSTされた場合のみgeneratorに対して乱数を入力、画像を生成する
    """
    if request.method == 'POST':
        # load model and run
        latent_dim = 32
        random_latent_vectors = np.random.normal(size=(1, latent_dim))
        generated_images = model.predict(random_latent_vectors)

        # 結果の変換
        resultmsg = np.uint8(generated_images[0]*255.)
        resultImg = Image.fromarray(resultmsg)
        resultImg = resultImg.resize(
            (int(resultImg.width*10), int(resultImg.height*10))
            )
        # 保存とタイムスタンプの取得(静的ファイルのキャッシュ対策)
        filepath = 'generated.jpg'
        savePath = './tmp/'+filepath  # GAEデプロイ時は.を外す
        resultImg.save(savePath)
        timeStamps = int(os.stat(savePath).st_mtime)
        # レンダリング時はドット(.)が不要
        filepath = f'/tmp/{filepath}?q={timeStamps}'
        # templateにわたす
        return render_template(
            'result.html', resultmsg=H5_MODEl, filepath=filepath)
    return render_template('generate.html')


if __name__ == '__main__':
    # app.run()
    app.run(host='127.0.0.1', port=8080, debug=True)