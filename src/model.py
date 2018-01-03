from keras.applications import VGG16
from flask              import jsonify
from os.path            import isfile
from image              import Image
import numpy  as np
import labels as l


MODEL_WEIGHTS_FILE = 'model_weights.h5'


class Model(object):

    def __init__(self):
        self.__model = VGG16()
        if isfile(MODEL_WEIGHTS_FILE):
            self.__model.load_weights(MODEL_WEIGHTS_FILE)

    def predict(self): 
        image = Image().decode('image')
        label = self.__model.predict(image)
        label = np.argmax(label[0])
        return jsonify(label = l.labels[label])

