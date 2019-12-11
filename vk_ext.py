import vk_api
import settings

vk_session = vk_api.VkApi(token=settings.token)
vk = vk_session.get_api()

def silent_kick(user_id):
	sk_vk_session = vk_api.VkApi(token=settings.sk_token)
	sk_vk = sk_vk_session.get_api()
	try:
		sk_vk.messages.removeChatUser(chat_id=settings.sk_chat_id, user_id=user_id)
		return True
	except:
		return False



def send(message):
	try:
		vk.messages.send(chat_id=settings.chat_id, message=message, random_id=0)
		return True
	except:
		return False


def tell(user_id, message):
	try:
		vk.messages.send(user_id=user_id, message=message, random_id=0)
		return True
	except:
		return False


def get_user_id(message_id):
	from re import findall
	items = vk.messages.getById(message_ids=message_id)['items'][0]
	user_ids = findall(r"\[id(\d+)\|", items['text'])
	if user_ids == []:
		if 'reply_message' in items:
			user_ids.append(items['reply_message']['from_id'])
		elif items['fwd_messages'] != []:
			for fwd in items['fwd_messages']:
				user_ids.append(fwd['from_id'])
	return user_ids


def kick(user_id):
	try:
		vk.messages.removeChatUser(chat_id=settings.chat_id, user_id=user_id)
		return True
	except:
		return False


def get_name(user_id, last_name=True, name_case='nom'):
	response = vk.users.get(user_ids=user_id, name_case=name_case)[0]
	if last_name:
		name = response['first_name'] + ' ' + response['last_name']
	else:
		name = response['first_name']
	return name


def invite(user_id):
	friend_status = vk.friends.areFriends(user_ids=user_id)[0]['friend_status']
	if friend_status in [2, 3]:
		vk.friends.add(user_id=user_id)
		try:
			vk.messages.addChatUser(chat_id=settings.chat_id, user_id=user_id)
		except Exception as e:
			print(e)
		return True
	else:
		return False

def id_to_mention(user_id, name_case='nom'):
	mention = '[id' + str(user_id) + '|' + get_name(user_id, True, name_case) + ']'
	return mention


def generate_mentions(online, from_id=0):
	chat_users = vk.messages.getChat(chat_id=settings.chat_id, fields='nickname, screen_name, online')['users']

	mentions = []
	for user in chat_users:
		if user['id'] > 0 and 'online' in user and (online == 0 or user['online'] == 1) and user['id'] != from_id and 'screen_name' in user.keys():
			mention = '[' + user['screen_name'] + '|' + user['first_name'] + ' ' + user['last_name'] + ']'
			mentions.append(mention)
	return mentions


