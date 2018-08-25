# -*- encoding: utf-8 -*-

from datetime import datetime
from mmpy_bot.bot import respond_to
from mmpy_bot.scheduler import schedule


@respond_to('reply (.*) at (.*)', re.IGNORECASE)
def reply_specific_time(message, content, trigger_time):
	t_time = datetime.strptime(trigger_time)
	schedule.once(t_time).do(message.reply, content)


@respond_to('reply (.*) every (.*) seconds', re.IGNORECASE)
def reply_every_seconds(message, content, seconds):
	schedule.every(int(seconds)).seconds.do(message.reply, content)


@respond_to('cancel jobs', re.IGNORECASE)
def cancel_jobs(message, content, seconds):
	schedule.clear()
	message.reply('all jobs canceled.')
