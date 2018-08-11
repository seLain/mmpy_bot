import os

PLUGINS = [
	'test_plugins',
	'mmpy_bot.plugins',
]

BOT_URL = os.environ.get("BOT_URL", 'http://carnation.ee.ncku.edu.tw/api/v4')
BOT_LOGIN = os.environ.get("TESTBOT_LOGIN", 'amy@nature.ee.ncku.edu.tw')
BOT_NAME = os.environ.get("TESTBOT_NAME", 'amy')
BOT_PASSWORD = os.environ.get("TESTBOT_PASSWORD", 'colors')

# this team name should be the same as in driver_settings
BOT_TEAM = os.environ.get("BOT_TEAM", 'reactlog')

# default public channel name
BOT_CHANNEL = os.environ.get("BOT_CHANNEL", 'off-topic')

# a private channel in BOT_TEAM
BOT_PRIVATE_CHANNEL = os.environ.get("BOT_PRIVATE_CHANNEL", 'test')

SSL_VERIFY = True
