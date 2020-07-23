# GAE quickstart
* URL
  * https://cloud.google.com/appengine/docs/standard/python3?hl=ja

## memo
* gcloudの使い方になれない

## sample app
* もってくる
 * `git clone https://github.com/GoogleCloudPlatform/python-docs-samples`

cd \
    python-docs-samples/appengine/standard_python37/hello_world

* これだけ
```
https://github.com/GoogleCloudPlatform/python-docs-samples/appengine/standard_python37/hello_world
```

* どっちかというとpipenvシリーズのコマンドを忘れている

```
% python3 -m pipenv --python 3.7 install -r requirements.txt
% python3 -m pipenv run python main.py
```

### Deploy
* これだけ？？？
```
gcloud app deploy app.yaml --project alwaysfree-hooktack
```
* コンソールで無効になっていたのを有効化
* こんなメッセージが出る
```
% gcloud app deploy app.yaml --project alwaysfree-hooktack
Services to deploy:

descriptor:      [/Users/fukutake.hiroaki/myRepos/Py/app_with_gan/GAE/quickstart/hello_world/app.yaml]
source:          [/Users/fukutake.hiroaki/myRepos/Py/app_with_gan/GAE/quickstart/hello_world]
target project:  [alwaysfree-hooktack]
target service:  [default]
target version:  [20200723t092422]
target url:      [https://alwaysfree-hooktack.wl.r.appspot.com]


Do you want to continue (Y/n)?  
```

* ちなみに複数動かせないの？というところはいかが解答
 * サービス単位みたいね
  * https://www.serversus.work/topics/vyly8dwer5uql5ra5xdg/