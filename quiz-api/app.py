from flask import Flask, request, jsonify
from flask_cors import CORS
import hashlib
import jwt_utils
import questions_manager
import participation_manager
import database_manager

app = Flask(__name__)
CORS(app)

def get_formatted_token(tokenWithBearer):
	if tokenWithBearer == None:
		return None
	return tokenWithBearer[7:]

@app.route('/rebuild-db', methods=['POST'])
def rebuild_db():
	token = get_formatted_token(request.headers.get('Authorization'))
	if token:
		try:
			jwt_utils.decode_token(token)
		except jwt_utils.JwtError as e:
			return jsonify({'message': e.args[0]}), 401
		
		database_manager.rebuild_database()
		return 'Ok', 200
	else:
		return jsonify({'message': 'Unauthorized'}), 401

@app.route('/quiz-info', methods=['GET'])
def get_quiz_info():
	return participation_manager.get_quiz_infos()

@app.route('/participations', methods=['POST'])
def add_participation():
	data = request.get_json()
	player_name = data['playerName']
	answers = data['answers']
	return participation_manager.add_participation(player_name, answers)

@app.route('/participations/all', methods=['DELETE'])
def delete_all_participation():
	token = get_formatted_token(request.headers.get('Authorization'))
	if token:
		try:
			jwt_utils.decode_token(token)
		except jwt_utils.JwtError:
			return jsonify({'message': 'Unauthorized because of invalid or expired token'}), 401
		
		return participation_manager.delete_all_participation()
	else:
		return jsonify({'message': 'Unauthorized'}), 401

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
	token = get_formatted_token(request.headers.get('Authorization'))
	if token:
		try:
			jwt_utils.decode_token(token)
		except jwt_utils.JwtError:
			return jsonify({'message': 'Unauthorized because of invalid or expired token'}), 401

		id = questions_manager.create_question(request.get_json())
		return jsonify({'id': id}), 200
	else:
		return jsonify({'message': 'Unauthorized'}), 401
	
@app.route('/questions/<questionId>', methods=['DELETE'])
def delete_one_question(questionId):
	token = get_formatted_token(request.headers.get('Authorization'))
	if token:
		try:
			jwt_utils.decode_token(token)
		except jwt_utils.JwtError:
			return jsonify({'message': 'Unauthorized because of invalid or expired token'}), 401

		try:
			questions_manager.delete_question(questionId)
		except ValueError as e:
			return jsonify({'message': e.args[0]}), 404
		return jsonify({'message': 'No Content'}), 204
	else:
		return jsonify({'message': 'Unauthorized'}), 401
	
@app.route('/questions/all', methods=['DELETE'])
def delete_all_questions():
	token = get_formatted_token(request.headers.get('Authorization'))
	if token:
		try:
			jwt_utils.decode_token(token)
		except jwt_utils.JwtError:
			return jsonify({'message': 'Unauthorized because of invalid or expired token'}), 401

		questions_manager.delete_all_question()
		return jsonify({'message': 'No Content'}), 204
	else:
		return jsonify({'message': 'Unauthorized'}), 401
	
@app.route('/questions/<questionId>', methods=['PUT'])
def modify_one_question(questionId):
	token = get_formatted_token(request.headers.get('Authorization'))
	if token:
		try:
			jwt_utils.decode_token(token)
		except jwt_utils.JwtError:
			return jsonify({'message': 'Unauthorized because of invalid or expired token'}), 401

		try:
			questions_manager.update_question(request.get_json(), questionId)
		except ValueError as e:
			return jsonify({'message': e.args[0]}), 404
		return jsonify({'message': 'No Content'}), 204
	else:
		return jsonify({'message': 'Unauthorized'}), 401
	
@app.route('/questions/<questionId>', methods=['GET'])
def get_question_by_id(questionId):
	return questions_manager.get_question_by_id(questionId)

@app.route('/questions', methods=['GET'])
def get_question_by_position():
	position = request.args.get('position')
	return questions_manager.get_question_by_position(position)

if __name__ == "__main__":
    app.run()