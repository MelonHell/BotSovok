import json
import os

filename = os.path.dirname(os.path.abspath(__file__)) + '/config.json'

with open(filename, 'r') as f:
	data = json.load(f)


def save(data):
	with open(filename, 'w') as f:
		json.dump(data, f)


class status:
	def get(user_id):
		if str(user_id) in data['status']:
			status = data['status'][str(user_id)]
		else:
			status = 0
		return status

	def set(user_id, status):
		if status == 0:
			data.pop(user_id)
		else:
			data['status'][str(user_id)] = status
			save(data)

	def all():
		return data['status']


def ban(user_id):
	user_id = int(user_id)
	if user_id in data['banned']:
		return False
	else:
		data['banned'].append(user_id)
		save(data)
		return True


def unban(user_id):
	user_id = int(user_id)
	if user_id in data['banned']:
		data['banned'].remove(user_id)
		save(data)
		return True
	else:
		return False

def marry_check(user_id):
	if str(user_id) in data['marry']:
		return data['marry'][str(user_id)]
	else:
		return False

def marry(user_id1, user_id2):
	data['marry'][str(user_id1)] = int(user_id2)
	data['marry'][str(user_id2)] = int(user_id1)
	save(data)

def marry_divorce(user_id1):
	user_id2 = data['marry'][str(user_id1)]
	data['marry'].pop(str(user_id1))
	data['marry'].pop(str(user_id2))
	save(data)

