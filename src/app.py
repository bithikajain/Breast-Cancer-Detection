import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import pdb

app = Flask(__name__)
api = Api(app)

# argument parsing
parser = reqparse.RequestParser()
parser.add_argument('data')

model_dir = "/home/bithika/src/Breast_Cancer_Detection/src/Trained_Forest_CV"

class predict(Resource):
    def get(self):
        args = parser.parse_args()
        # use parser and find the user's query
        print("Args:", args)
        user_query = args['data']
        print("User query:", user_query)

        data = user_query.split(',')
        data = [float(i) for i in data]

        loaded_model = pickle.load(open(model_dir, 'rb'))
        pred = loaded_model.predict([data])
        print(pred)

        # create JSON object
        if pred == 1:
            output = {'prediction': 'Malignant'}
        else:
            output = {'prediction': 'Benign'}

        return output

api.add_resource(predict, '/')

if __name__ == '__main__':
    app.run(port=3000, debug=True)
