# Flask with GAN
* my prototyping flask app for running tiny generator from GAN.

## components
* google colab notebook (DCGAN) for learning task.
* flask app for running generator from notebook.
* (optional) deploy flask app to Google App Engine.

### requirements
* Google Colab Account
* python 3.7 + any
* Google Cloud Account


## How to run
* generate hdf5 file from google colab notebook (DCGAN).
* put hdf file and run flask app on local
  * see [flask-app directory](flask-app)
* (optional)deploy the app to your any Google App Engine 
  * see [flask-app directory](flask-app)


## TO DO
* [x] Data preparation with icrawler
* [x] Training with GAN (as simpy: DCGAN)
  * [x] modify network size
  * [ ] save a best .pb and copy to GCS
* [ ] Run Flask on GAE
  * [ ] make hello-world app
  * [ ] run sample flask app
  * [ ] modify sample app  
* [ ] Run Generator on GAE

### if can...
* [ ] with Cloud Run
* [ ] TF Serving on AI Platform
  

## EOF