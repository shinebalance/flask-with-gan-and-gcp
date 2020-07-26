# run Generator(from DCGAN) on FlaskApp
* DCGANのNotebookから学習済モデルをDLし、本Flaskアプリに読み込ませることで、Generatorの生成結果を手軽にブラウザ上で確認することが出来る。
* FlaskアプリはGoogle App Engineへのデプロイまで検証済。


## How to run
### on Local
```
pip3 install -r requirements.txt
python3 main.py
```
### with pipenv
```
python3 -m pipenv --python 3.7 install -r requirements.txt
python3 -m pipenv run python main.py
# with gunicorn
python3 -m pipenv shell
gunicorn -b :$8080 main:app
```
### on Google AppEngine
```
gcloud app deploy app.yaml
```



## motivation
* 苦手なWebフレームワークを自分のニーズで動かす
* サーバレス系のPaaSを動かしてみたい
* GANのGeneratorの活用方法を考える


## Must to do
* [x] Generator(CIFAR-10)で生成したModelを保存して推論で動かす
* [ ] Generator(my own)で生成したModelを保存して推論で動かす
* [x] 推論処理をflaskに組み込む
* [ ] flaskをGAEにDeployする
* [ ] 推論処理をtflite化する

### if possible




## EOF