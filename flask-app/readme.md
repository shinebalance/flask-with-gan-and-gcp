# prototyping flaskk app
* load hdf5 file from [notebook](notebook)
* run Generator(DCGAN) on this flask app

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

## Must to do
* [x] Generator(CIFAR-10)で生成したModelを保存して推論で動かす
* [ ] Generator(my own)で生成したModelを保存して推論で動かす
* [x] 推論処理をflaskに組み込む
* [ ] flaskをGAEにDeployする
* [ ] 推論処理をtflite化する

### if possible




## EOF