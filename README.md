# Keras deployment

This is an example of deploying a Keras model using Flask for
image classification.  It is just the stock ImageNet VGG16 model
with a Flask wrapper.  

Launch Flask:

```
export FLASK_APP=app.py
flask run
```

Submit the test image from command line:
```
curl -X POST -F 'image=@images/dog.jpg' http://localhost:5000/predict

```

You should be met with a JSON response that is reasonable.
