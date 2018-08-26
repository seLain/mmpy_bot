from datetime import datetime, timedelta
from tests.behavior_tests.fixture import driver


def test_bot_reply_specific_time(driver):
    t_time = datetime.now() + timedelta(seconds=5)
    str_t_time = t_time.strftime('%b-%d-%Y_%H:%M:%S')
    driver.send_direct_message(
        'reply "{0}" at {0}'.format(str_t_time), tobot=True)
    driver.wait_for_bot_direct_message(str_t_time)


def test_bot_reply_every_seconds(driver):
    driver.send_direct_message('reply "alive" every 5 seconds', tobot=True)
    driver.wait_for_bot_direct_message('alive')
    driver.wait_for_bot_direct_message('alive')
    driver.send_direct_message('cancel jobs', tobot=True)
    driver.wait_for_bot_direct_message('all jobs canceled.')
