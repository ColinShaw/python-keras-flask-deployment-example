from keras.applications import imagenet_utils
from scipy.misc         import imread, imresize
from flask              import request
from io                 import BytesIO
from base64             import b64decode
import numpy as np


class Image(object):        

    @staticmethod
    def decode(name):
        image = request.files[name].read()
        image = imread(BytesIO(image))
        image = imresize(image, (224,224)).astype(np.float32)
        image = imagenet_utils.preprocess_input(image)
        image = np.reshape(image, (1,224,224,3))
        return image

