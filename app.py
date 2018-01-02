from keras.applications import VGG16, imagenet_utils
from scipy.misc         import imread, imresize
from flask              import Flask, request, jsonify
from io                 import BytesIO
from base64             import b64decode
import src.labels as l
import numpy      as np
import base64


app   = Flask(__name__)
vgg16 = VGG16()

@app.route('/predict', methods=['POST'])
def predict():
    image = request.files['image'].read()
    image = imread(BytesIO(image))
    image = imresize(image, (224,224)).astype(np.float32)
    image = imagenet_utils.preprocess_input(image)
    image = np.reshape(image, (1,224,224,3))
    logit = vgg16.predict(image)
    label = np.argmax(logit[0])
    return jsonify(
        classification = l.labels[label]
    )

