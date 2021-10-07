from utils import loadCookies, getReward, isClaimed, claimReward, parseReward, logging
import datetime
import os
import sys
import time

COOKIE = os.environ.get('COOKIE')

def cronJob():
	logging("Starting...")
	if not COOKIE:
		print("There's no COOKIE set, bot can't run without that. Quiting with error...", file=sys.stderr)
		quit(1)
	multicookies = []
	for cookie in COOKIE.split("\n"):
		multicookies.append(loadCookies(cookie))
	if len(multicookies) >= 2:
		print("Multi account detected, logging in with {} accounts".format(len(multicookies)))
	acccount = 0
	for cookies in multicookies:
		acccount += 1
		counter_str = f"[{acccount}] " if len(multicookies) >= 2 else ""
		logging("{}Connecting to server...".format(counter_str))
		try:
			reward = getReward(cookies)
			check, day = isClaimed(cookies)
		except Exception as err:
			logging(f"{counter_str}Unexpected Error [1]: {repr(err)}", 3)
			continue
		if str(check).lower() == "not logged in":
			logging(f"{counter_str}Failed to logged in, maybe wrong cookie?", 3)
			continue
		if not check:
			logging(f"{counter_str}Claiming daily...")
			try:
				c = claimReward(cookies)
			except Exception as err:
				logging(f"{counter_str}Unexpected Error [2]: {repr(err)}", 3)
				continue
			if c:
				icon, name, count = parseReward(reward, day + 1)
				logging(f"{counter_str}{name} ×{count} claimed successfully!", 4, icon)
			else:
				logging(f"{counter_str}Failed to claim daily! {c['message']}", 2)
		else:
			if type(check) == bool:
				logging(f"{counter_str}Already claimed")
			else:
				logging(counter_str + check)

def manualJob():
	print("Inline job isn't supported yet, but you can do cron job by running script 'python3 daily.py cron'", file=sys.stderr)
	quit(1)

	# TODO
	logging("Starting...")
	if not COOKIE:
		print("There's no COOKIE set, bot can't run without that. Quiting with error...", file=sys.stderr)
		quit(1)
	cookies = loadCookies(COOKIE)
	CLAIMED_COUNT = 0
	while True:
		logging(f"[Day {CLAIMED_COUNT}] Connecting to server...")
		try:
			reward = getReward(cookies)
			check = isClaimed(cookies)
		except Exception as err:
			logging(f"Unexpected Error [1]: {repr(err)}", 3)
			raise err
		if not check:
			logging(f"[Day {CLAIMED_COUNT}] Claiming daily...")
			try:
				c = claimReward(cookies)
			except Exception as err:
				logging(f"Unexpected Error [2]: {repr(err)}", 3)
				raise err
			if c:
				CLAIMED_COUNT = c['data']['total_sign_day']
				icon, name, count = parseReward(reward, c)
				logging(f"[Day {CLAIMED_COUNT}] {name} ×{count} claimed successfully!", 4, icon)
			else:
				logging(f"[Day {CLAIMED_COUNT}] Failed to claim daily! {c['message']}", 2)
		else:
			if type(check) == bool:
				logging(f"[Day {CLAIMED_COUNT}] Already claimed")
			else:
				logging(check)
		shtime = 1
		while shtime > 0:
			shtime = int(checkSleepTime()) - int(checkShanghaiTime())
			sys.stdout.write(f"[Day {CLAIMED_COUNT}] Waiting for next day | {time_formatter(shtime)}\r")
			sys.stdout.flush()
			time.sleep(1)


def checkShanghaiTime():
	return (datetime.datetime.utcnow() + datetime.timedelta(hours=+8)).timestamp()

def checkSleepTime():
	currtime = (datetime.datetime.utcnow() + datetime.timedelta(hours=+8))
	sleep_until = time.strftime("%m/%d/%Y 22:00", currtime.timetuple())
	return time.mktime(time.strptime(sleep_until, "%m/%d/%Y %H:%M"))

def time_formatter(seconds):
	minutes, seconds = divmod(seconds, 60)
	hours, minutes = divmod(minutes, 60)
	days, hours = divmod(hours, 24)
	tmp = (
		((str(days) + " day(s), ") if days else "") +
		((str(hours) + " hour(s), ") if hours else "") +
		((str(minutes) + " minute(s), ") if minutes else "") +
		((str(seconds) + " second(s), ") if seconds else "")
	)
	return tmp[:-2]


if len(sys.argv) >= 2 and sys.argv[1] == "cron":
	cronJob()
else:
	manualJob()
