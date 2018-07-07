import gym
import gym_token
env = gym.make('token-v1')

import datetime, pytz
def get_hour(unix_timestamp):
			date = datetime.datetime.fromtimestamp(int(unix_timestamp))
			utc_dt = date.astimezone(pytz.utc)
			return utc_dt.hour

print('------')
print(env.reset())

import random

for i in range(20):
	action = random.randint(0,2)
	trans_action = None
	if action==0:
		trans_action = 'Sell'
	elif action==1:
		trans_action = 'Hold'
	elif action==2:
		trans_action = 'Buy'

	print(f'>>step: {i}, action: {action} = {trans_action}')
	info = env.step(action)
	print(info)
	if info[2]==True:
		print('------')
		print(env.reset())
