from flask import Flask, jsonify
from pymongo.mongo_client import MongoClient
import certifi

ca = certifi.where()

app = Flask(__name__)


app = Flask(__name__)
uri = "mongodb+srv://"


client = MongoClient(uri, tlsCAFile=ca)
db = client['lottery']
collection = db['lottery']

@app.route('/lotto', methods=['GET'])
def get_lotto_data():
    """
    MongoDB에서 단일 로또 데이터를 조회합니다.
    데이터베이스에는 단 하나의 문서만 저장되어 있다고 가정합니다.
    """
    lotto_data = collection.find_one({}, {'_id': 0})  # MongoDB의 _id 필드는 제외하고 조회
    if lotto_data:
        return jsonify(lotto_data), 200
    else:
        return jsonify({'error': 'Data not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)

client = MongoClient('mongodb://localhost:27017/')
db = client['lottery']
collection = db['lottery']

@app.route('/lotto', methods=['GET'])
def get_lotto_data():
    """
    MongoDB에서 단일 로또 데이터를 조회합니다.
    데이터베이스에는 단 하나의 문서만 저장되어 있다고 가정합니다.
    """
    lotto_data = collection.find_one({}, {'_id': 0})  # MongoDB의 _id 필드는 제외하고 조회
    if lotto_data:
        return jsonify(lotto_data), 200
    else:
        return jsonify({'error': 'Data not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
