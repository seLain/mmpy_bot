from datetime import datetime, timedelta
from tests.behavior_tests.fixture import driver

from mmpy_bot import settings


def test_bot_reply_specific_time(driver):
    settings.JOB_TRIGGER_PERIOD = 2
    t_time = datetime.now() + timedelta(seconds=5)
    str_t_time = t_time.strftime('%b-%d-%Y_%H:%M:%S')
    driver.send_direct_message(
        'reply "{0}" at {0}'.format(str_t_time), tobot=True)
    driver.wait_for_bot_direct_message(str_t_time, maxwait=60)
    settings.JOB_TRIGGER_PERIOD = 60


def test_bot_reply_every_seconds(driver):
    settings.JOB_TRIGGER_PERIOD = 2
    driver.send_direct_message('reply "alive" every 5 seconds', tobot=True)
    driver.wait_for_bot_direct_message('alive', maxwait=60)
    driver.wait_for_bot_direct_message('alive', maxwait=60)
    driver.send_direct_message('cancel jobs', tobot=True)
    driver.wait_for_bot_direct_message('all jobs canceled.', maxwait=60)
    settings.JOB_TRIGGER_PERIOD = 60
