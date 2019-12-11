# -*- coding: utf-8 -*-
from vk_api.longpoll import VkLongPoll, VkEventType
from bot_locale import chat_ru as loc
import vk_ext
import config
import time

longpoll = VkLongPoll(vk_ext.vk_session)

vk_ext.send("Бот запущен!\n\n«раз катя откинулась из совка, то мейби поменяешь text?»\n© Ася Вурхиз")


# FUNCS
def access(status, send_msg=1):
	if config.status.get(event.user_id) >= status:
		return True
	else:
		vk_ext.send(loc['status']['access'][0] + str(status) + loc['status']['access'][1])
		return False


def compare(user_id1, user_id2):
	if config.status.get(user_id1) > config.status.get(user_id2):
		return True
	else:
		vk_ext.send(vk_ext.get_name(user_id2) + loc['status']['compare'])
		return False

# MAIN

marry_request = {'from_id': 0, 'to_id': 0}

def new_chat_message(cmd, text_split):

	global marry_request
	
	if ' '.join(cmd).find('трапы геи') != -1:
		vk_ext.send('ТРАПЫ НЕ ГЕИ!!!')
		vk_ext.kick(event.user_id)

	# БОТ
	if cmd[0] in loc['bot']['names']:
		import random
		text = ' '.join(text_split[2:])

		if len(cmd) == 1:
			pass
	
		# КТО
		elif cmd[1] in loc['bot']['cmd_kto']:
			users = vk_ext.vk.messages.getChat(chat_id=vk_ext.settings.chat_id, fields='first_name')['users']
			rand_user = random.choice(users)
			vk_ext.send(random.choice(loc['bot']['who']) + ' [id' + str(rand_user['id']) + '|' + rand_user['first_name'] + ' ' + rand_user['last_name'] + '] ' + text)
		
		# НАРИСУЙ ХУЙ
		elif cmd[1:3] == loc['bot']['cmd_huy']:
			vk_ext.send("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n░░░░░░░░░░░░░░░░░░░░░░░░░░░██████░░░░░░░\n░░░░░░░░░░░░░░░░░░░░░░░░███░░░█░██░░░░░░\n░░░░░░░░░░░░░░░░░░░░░░░██░░░░█░░░██░░░░░\n░░░░░░░░░░░░░░░░░░░░░██░██░░█░░░░░█░░░░░\n░░░░░░░░░░░░░░░░░░░░██░░░█████░░███░░░░░\n░░░░░░░░░░░░░░░░░░░██░░░░░░░░█████░░░░░░\n░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░█░░░░░░░\n░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░█░░░░░░░░\n░░░░░░░░░░░░░░░░██░░░░░░░░░░░░██░░░░░░░░\n░░░░░░░░░░░░░░░░█░░░░░░░░░░░░██░░░░░░░░░\n░░░░░░░░░░░░░░░█░░░░░░░░░░░░██░░░░░░░░░░\n░░░░░░░░░░░░░░██░░░░░░░░░░░██░░░░░░░░░░░\n░░░░░░░░░░░░░░█░░░░░░░░░░░██░░░░░░░░░░░░\n░░░░░░░░░░░░░█░░░░░░░░░░░██░░░░░░░░░░░░░\n░░░░░░░░██████░░░░░░░░░░██░░░░░░░░░░░░░░\n░░░░░██████░███░░░░░░░░██░░░░░░░░░░░░░░░\n░░░░██░░░░░░░░██░░░░░░██░░░░░░░░░░░░░░░░\n░░░░█░░░░░░░░░░██░█████████░░░░░░░░░░░░░\n░░░░█░░░░░░░░░░░██░░░░░░░░███░░░░░░░░░░░\n░░░░█░░░░░░░░░░██░░░░░░░░░░░██░░░░░░░░░░\n░░░░██░░░░░░░░███░░░░░░░░░░░░█░░░░░░░░░░\n░░░░░██░░░░░████░░░░░░░░░░░░░█░░░░░░░░░░\n░░░░░░░█████░░██░░░░░░░░░░░░░█░░░░░░░░░░\n░░░░░░░░░░░░░░░███░░░░░░░░░███░░░░░░░░░░\n░░░░░░░░░░░░░░░░░███████████░░░░░░░░░░░░\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")
		
		# ИНФА
		elif cmd[1] in loc['bot']['cmd_infa']:
			vk_ext.send(text + ' на ' + str(random.randint(0, 100)) + '%')
		
		# ПРАВДА ЧТО
		elif cmd[1:3] == ['правда', 'что']:
			texts = ['Да', 'Нет', 'Скорее да', 'Скорее нет', 'А хуй его знает', 'Естественно', 'Ты че ебанутый, нет конечно']
			vk_ext.send(random.choice(texts))
			

	# TEST
	elif cmd[0] in loc['cmd']['test']:
		vk_ext.send('SEMGA PIDORAS')

	# STOP
	elif cmd[0] in loc['cmd']['stop'] and access(10):
		from sys import exit as sys_exit
		sys_exit()
	
	# HELP
	elif cmd[0] in loc['cmd']['help']:
		msg = loc['help']['main']
		for h in loc['cmd']:
			msg += "\n" + ' '.join(loc['cmd'][h])
		vk_ext.send(msg)

	# KICK/BAN
	elif (cmd[0] in loc['cmd']['kick'] and access(8)) or (cmd[0] in loc['cmd']['ban'] and access(9)):
		for user_id in vk_ext.get_user_id(event.message_id):
			compare(event.user_id, user_id) and vk_ext.kick(user_id)
			if cmd[0] in loc['cmd']['ban']:
				config.ban(user_id)

	# UNBAN
	elif cmd[0] in loc['cmd']['unban'] and access(9):
		for user_id in vk_ext.get_user_id(event.message_id):
			config.unban(user_id)
			vk_ext.invite(user_id)

	# EVERYONE/HERE
	elif (cmd[0] in loc['cmd']['everyone'] and access(8)) or (cmd[0] in loc['cmd']['here'] and access(8)):
		if cmd[0] in loc['cmd']['everyone']:
			online = 0
		else:
			online = 1
		message = vk_ext.id_to_mention(event.user_id) + ' > ' + ' '.join(text_split[1:]) + "\n\n" + ', '.join(vk_ext.generate_mentions(online, event.user_id))
		vk_ext.send(message)

	# INVITE
	elif cmd[0] in loc['cmd']['invite'] and access(8):
		for user_id in vk_ext.get_user_id(event.message_id):
			if user_id in config.data['banned']:
				vk_ext.send(vk_ext.get_name(user_id) + loc['welcome']['ban'])
			else:
				if not vk_ext.invite(user_id):
					if vk_ext.tell(user_id, vk_ext.get_name(event.user_id) + loc['im']['tell_invite']):
						vk_ext.send(loc['invite']['send'])
					else:
						vk_ext.send(loc['invite']['error'])

	# STATUS
	elif cmd[0] in loc['cmd']['status'] and access(10):
		if cmd[1].isdigit():
			for user_id in vk_ext.get_user_id(event.message_id):
				compare(event.user_id, user_id) and config.status.set(user_id, int(cmd[1]))
				vk_ext.send(loc['status']['success'])
		else:
			vk_ext.send(loc['help']['status'])

	elif cmd[0] in loc['cmd']['statuses']:
		msg = ''
		statuses = config.status.all()
		for user_id in statuses:
			msg += vk_ext.get_name(user_id) + ': ' + str(statuses[user_id]) + "\n"
		vk_ext.send(msg)


	# MARRY
	elif cmd[0] in loc['cmd']['marry']:
		user_ids_to = vk_ext.get_user_id(event.message_id)

		if len(cmd) >= 2 and cmd[1] in loc['marry']['divorce']:
			if config.marry_check(event.user_id):
				config.marry_divorce(event.user_id)
				vk_ext.send('Теперь ты не состоишь в браке')
			else:
				vk_ext.send('Ты и так не состоишь в браке')

		elif len(cmd) >= 2 and cmd[1] in loc['marry']['accept']:
			if int(event.user_id) == int(marry_request['to_id']):
				
				if config.marry_check(event.user_id):
					vk_ext.send('Ты и так уже состоишь в браке, так шо иди нахуй')
				else:
					config.marry(marry_request['from_id'], marry_request['to_id'])
					vk_ext.send('Супер, можете идти ебаться!')
				marry_request = {'from_id': 0, 'to_id': 0}
			else: 
				vk_ext.send('Это не тебе, дурашка')

		elif len(cmd) >= 2 and cmd[1] in loc['marry']['deny']:
			if int(event.user_id) == int(marry_request['to_id']):
				vk_ext.send('Тебя послали нахуй :(')
				marry_request = {'from_id': 0, 'to_id': 0}
			else: 
				vk_ext.send('Это не тебе, дурашка')

		elif len(user_ids_to) == 1:

			if config.marry_check(event.user_id):
				vk_ext.send('Ты и так уже состоишь в браке, так шо иди нахуй')
			else:
				user_id_to = user_ids_to[0]
				users = vk_ext.vk.users.get(user_ids=str(event.user_id) + ', ' + str(user_id_to), fields='sex')
				text1 = loc['marry']['text1'][2 - users[1]['sex']]
				text2 = loc['marry']['text2'][2 - users[0]['sex']]
				vk_ext.send(vk_ext.id_to_mention(user_id_to)+ ', ' + text1 + ' ли ты ' + text2 + ' ' + vk_ext.id_to_mention(event.user_id, 'acc') + "?\nСогласиться - /marry accept\nОтказаться - /marry deny")
				
				marry_request = {'from_id': event.user_id, 'to_id': user_id_to}

		elif len(user_ids_to) == 0:
			vk_ext.send('Блять ты криворукое говно непарвильно комманду юзаешь')
		else:
			vk_ext.send('Мы шо арабы несколько жен иметь шоли?')

	# MARRIAGES
	elif cmd[0] in loc['cmd']['marriages']:
		marry_dict = config.data['marry']
		antiduplicate = []
		text = ''
		for user_id1 in marry_dict:
			if not int(user_id1) in antiduplicate:
				
				user_id2 = marry_dict[user_id1]
				antiduplicate.append(int(user_id2))
				text += (vk_ext.get_name(user_id1) + ' и ' + vk_ext.get_name(user_id2)) + "\n"
		vk_ext.send(text)



	# YANDERE
	elif cmd[0] in loc['cmd']['yandere']:
		import requests, json

		unblock = 'https://unblocksites.space/?cdURL='
		ddg_proxy = 'https://proxy.duckduckgo.com/iu/?u='

		yandere = 'https://yande.re/post.json?tags=order:random+'

		if len(cmd) == 1 or not cmd[1] in ['s', 'q', 'e']:
			vk_ext.send(loc['help']['yandere'])
		else:
			if len(cmd) == 2:
				tags = cmd[1]
			else:
				tags = cmd[1] + '+' + '+'.join(text_split[2:])


			url = unblock + yandere + 'rating:' + tags

			try:
				data = json.loads(requests.get(url).text)
				img = ddg_proxy + data[0]['file_url']
				short_img = vk_ext.vk.utils.getShortLink(url=img)['short_url']
				vk_ext.send(short_img)
			except Exception as e:
				vk_ext.send('Error')


def new_im_message(cmd, text_split):
	if cmd[0] in loc['im']['cmd_invite']:
		if event.user_id in config.data['banned']:
			vk_ext.tell(event.user_id, loc['im']['ban'])
		else:
			if vk_ext.invite(event.user_id):
				vk_ext.tell(event.user_id, loc['im']['success'])
			else:
				vk_ext.tell(event.user_id, loc['im']['no_friend'])
	elif cmd[0] in loc['im']['cmd_silent_kick'] and access(10, 0):
		for user_id in vk_ext.get_user_id(event.message_id):
			if vk_ext.silent_kick(user_id):
				vk_ext.tell(event.user_id, loc['im']['sk_success'])
			else:
				vk_ext.tell(event.user_id, loc['im']['sk_error'])

def chat_update():
	if event.type_id == 7: # LEAVE
		vk_ext.kick(event.info['user_id'])
	elif event.type_id == 6: # NEW
		if event.info['user_id'] in config.data['banned']:
			vk_ext.send(vk_ext.get_name(
				event.info['user_id']) + loc['welcome']['ban'])
			vk_ext.kick(event.info['user_id'])
		else:
			vk_ext.send(loc['welcome']['main'])

telega_piar_time = time.time()

def telega_piar():
	global telega_piar_time
	if (time.time() - telega_piar_time) > 21600:
		#vk_ext.vk.messages.send(chat_id=vk_ext.settings.chat_id, message='https://tgmsg.ru/ad_sovok', attachment='photo-172204662_456239027', dont_parse_links=1, random_id=0)
		telega_piar_time = time.time()

if __name__ == '__main__':
	for event in longpoll.listen():

		telega_piar()

		if event.type == VkEventType.CHAT_UPDATE and event.chat_id == vk_ext.settings.chat_id:
			chat_update()

		if event.type == VkEventType.MESSAGE_NEW:
			cmd = event.text.lower().replace('ё', 'е').split(' ')
			text_split = event.text.split(' ')

			if event.to_me and event.from_chat and event.chat_id == vk_ext.settings.chat_id and event.user_id > 0:
				new_chat_message(cmd, text_split)
			elif event.to_me and event.from_user:
				new_im_message(cmd, text_split)
