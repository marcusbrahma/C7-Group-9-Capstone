from flask import Flask,jsonify,request
from flask_cors import CORS, cross_origin
 

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET'])
def getproduct():

    if(request.method == 'GET'):
        product = [{'Name': "product 1",
                   'Image': "Image 1",
                   'price': 100,
                },
                {'Name': "product 2",
                   'Image': "Image 2",
                   'price': 200,
                }]
        return jsonify(product)

if __name__ == '__main__':
	app.run(debug=True)
