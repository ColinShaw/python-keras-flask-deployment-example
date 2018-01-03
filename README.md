# Keras Flask Deployment

This is an example of deploying a Keras model using Flask for
image classification.  It is just the stock ImageNet VGG16 model
with some abstraction around the model and image pre-processing. A
convenient shell script is provided to launch the Flask app. You 
can submit the test image from command line:

```
curl -X POST -F 'image=@images/dog.jpg' http://localhost:5000/predict

```

