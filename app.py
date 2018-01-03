from flask     import Flask
from src.model import Model

app   = Flask(__name__)
model = Model()

@app.route('/predict', methods=['POST'])
def predict():
    return model.predict()

@app.route('/train', methods=['POST'])
def train():
    return model.train()

