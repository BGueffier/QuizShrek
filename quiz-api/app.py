from flask import Flask, request, jsonify
from flask_cors import CORS
import hashlib
import jwt_utils
import questionsManager

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
	x = 'worlds'
	return f"Hello, {x}"

@app.route('/quiz-info', methods=['GET'])
def get_quiz_info():
	return {"size": 0, "scores": []}, 200

@app.route('/login', methods=['POST'])
def log_in():
	payload = request.get_json()
	tried_password = payload['password'].encode('UTF-8')
	hashed = hashlib.md5(tried_password).digest()
	if hashed == b'\xd8\x17\x06PG\x92\x93\xc1.\x02\x01\xe5\xfd\xf4_@':
		token = jwt_utils.build_token()
		return jsonify({'token': token}), 200
	else:
		return jsonify({'message': 'Unauthorized'}), 401

@app.route('/questions', methods=['POST'])
def questions():
	tokenWithBearer = request.headers.get('Authorization')
	token = tokenWithBearer[7:]
	if (token is not None and jwt_utils.decode_token(token)):
		id = questionsManager.create_question(request.get_json())
		return jsonify({'id': id}), 200
	else:
		return jsonify({'message': 'Unauthorized'}), 401

if __name__ == "__main__":
    app.run()