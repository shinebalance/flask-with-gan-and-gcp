# FlaskAp on GAE

## Want to do
* GANで生成したGeneratorのモデルを読み込み、Web画面上で生成して表示する
* 最終的にGoogle App Engine上にDeployして動かす

## Must to do
* [ ] Generator(CIFAR-10)で生成したModelを保存して推論で動かす
* [ ] Generator(my own)で生成したModelを保存して推論で動かす
* [ ] 推論処理をflaskに組み込む
* [ ] flaskをGAEにDeployする
* [ ] 推論処理をtflite化する

## Work notes
* [x] 手頃なサンプルを集めてきて動かす
 * '_flask_samples'にて、GAEクイックスタートとFlask自体のサンプル、オバマ判定サンプルを動かした
 * オバマ判定サンプルをたたきに自分のアプリを作ることにする


## commands memo
```
python3 -m pipenv --python 3.7 install -r requirements.txt
python3 -m pipenv run python main.py
```

# EOF