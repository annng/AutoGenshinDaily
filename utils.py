import time
import os
import requests

ACT_ID = 'e202102251931481'
DOMAIN_NAME = '.mihoyo.com'
TG_BOT_TOKEN = os.environ.get('TG_BOT_TOKEN')
OWNER_ID = os.environ.get('OWNER_ID')

def loadCookies(cookies):
	loadedCookies = {}
	for cookiedata in cookies.split("; "):
		d1, d2 = cookiedata.split("=")
		loadedCookies[d1] = d2
	return loadedCookies

def getReward(loadedCookies):
	headers = {
		'Accept': 'application/json, text/plain, */*',
		'Accept-Language': 'en-US,en;q=0.5',
		'Origin': 'https://webstatic-sea.mihoyo.com',
		'Connection': 'keep-alive',
	}

	params = (
		('lang', 'en-us'),
		('act_id', ACT_ID),
	)

	try:
		response = requests.get('https://hk4e-api-os.mihoyo.com/event/sol/home', headers=headers, params=params, cookies=loadedCookies)
		return response.json()
	except requests.exceptions.ConnectionError as e:
		print(f"Connection error! {e}")
		raise 'Cannot get Reward data\n' + repr(e)
	except Exception as e:
		print(f"Unknown error! {e}")
		raise 'Cannot get Reward data\n' + repr(e)

def getStatus(loadedCookies):
	headers = {
		'Accept': 'application/json, text/plain, */*',
		'Accept-Language': 'en-US,en;q=0.5',
		'Origin': 'https://webstatic-sea.mihoyo.com',
		'Connection': 'keep-alive',
		'Referer': f'https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id={ACT_ID}&lang=en-us',
		'Cache-Control': 'max-age=0',
	}
	params = (
		('lang', 'en-us'),
		('act_id', ACT_ID),
	)
	try:
		response = requests.get('https://hk4e-api-os.mihoyo.com/event/sol/info', headers=headers, params=params, cookies=loadedCookies)
		return response.json()
	except requests.exceptions.ConnectionError as e:
		print(f"Connection error! {e}")
		raise 'Cannot check user status\n' + repr(e)
	except Exception as e:
		print(f"Unknown error! {e}")
		raise 'Cannot check user status\n' + repr(e)

def parseReward(reward, info):
	#signdata = info['data']['total_sign_day']
	parsed = reward['data']['awards'][info-1]
	return parsed['icon'], parsed['name'], parsed['cnt']

def isClaimed(loadedCookies):
	resp = getStatus(loadedCookies)
	if resp:
		if not resp['data']:
			return resp['message'], 0
		return resp['data']['is_sign'], resp['data']['total_sign_day']
	else:
		return True, 0

def claimReward(loadedCookies):
	headers = {
		'Accept': 'application/json, text/plain, */*',
		'Accept-Language': 'en-US,en;q=0.5',
		'Content-Type': 'application/json;charset=utf-8',
		'Origin': 'https://webstatic-sea.mihoyo.com',
		'Connection': 'keep-alive',
		'Referer': f'https://webstatic-sea.mihoyo.com/ys/event/signin- sea/index.html?act_id={ACT_ID}&lang=en-us',
	}

	params = (
		('lang', 'en-us'),
	)

	data = {
		'act_id': ACT_ID
	}

	try:
		response = requests.post('https://hk4e-api-os.mihoyo.com/event/sol/sign', headers=headers, params=params, json=data, cookies=loadedCookies)
		return response.json()
	except requests.exceptions.ConnectionError as e:
		print(f"Connection error! {e}")
		raise 'Cannot claim daily check-in reward\n' + repr(e)
	except Exception as e:
		print(f"Unknown error! {e}")
		raise 'Cannot claim daily check-in reward\n' + repr(e)

def send_to_tg(text):
	if not OWNER_ID:
		print("Cannot send to Telegram, OWNER_ID is not set in Secrets")
		return 0
	TG_API = f"https://api.telegram.org/bot{TG_BOT_TOKEN}/sendMessage"
	data = {"chat_id": OWNER_ID, "text": text, "parse_mode": "html"}
	req = requests.post(TG_API, json=data).json()
	if not req['ok'] and TG_BOT_TOKEN:
		if req['error_code'] == 401:
			logging(f"Cannot send to Telegram: Bot Token Invalid")
		else:
			logging(f"Cannot send to Telegram: {req['description']}")
	return req['ok']

def send_pic_tg(text, photo):
	if not OWNER_ID:
		print("Cannot send to Telegram, OWNER_ID is not set in Secrets")
		return 0
	TG_API = f"https://api.telegram.org/bot{TG_BOT_TOKEN}/sendPhoto"
	data = {"photo": photo, "chat_id": OWNER_ID, "caption": text, "parse_mode": "html"}
	req = requests.post(TG_API, json=data).json()
	if not req['ok'] and TG_BOT_TOKEN:
		if req['error_code'] == 401:
			logging(f"Cannot send to Telegram: Bot Token Invalid")
		else:
			logging(f"Cannot send to Telegram: {req['description']}")
	return req['ok']

def logging(log, status=1, pic=None):
	if status == 1:
		print(log)
	elif status == 2:
		print(log)
		if TG_BOT_TOKEN:
			send_to_tg(log)
	elif status == 3:
		print(log)
		if TG_BOT_TOKEN:
			print("Sending report...")
			if send_to_tg("<b>GI-Daily</b>\n" + log):
				print("Done!")
	elif status == 4:
		print(log)
		if TG_BOT_TOKEN:
			send_pic_tg(log, pic)
	else:
		print(log)
	return True
