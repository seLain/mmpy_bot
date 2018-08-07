.. _testing:

Testing
============

mmpy_bot develops all tests based on pytest. If you need to add your own tests and run tests, please install pytest first.

.. code-block:: bash

	$ pip install -U pytest``

All the tests are put in `mmpy_bot\tests`.
There are two test packages: **unit_tests** and **behavior_tests**.

Tests which can be performed by single bot without mattermost server or other bots should be kept in unit_tests package.
Other tests requiring interactions between bots on mattermost server belong to behavior_tests package.

Add unit test
-------------

There are multiple test modules inside unit_tests package.
Each module collects tests of specific mmpy_bot class or module.
The naming convention of these modules are *test_classname* or *test_modulename*.
Inside each module, there will be several test functions with naming convention *test_functionname* or *test_methodname*.
Each test function performs unit test against specific class or module.
If you need to add more unit tests, please consider follow these conventions.

Add behavior test
-----------------

The behavior tests are done by interactions between a **DriverBot** and a **TestBot**.



Run all the tests:
------------------

You will need a Mattermost server to run test cases. 

 * Create two user accounts for bots to login, ex. **driverbot** and **testbot**
 * Create a team, ex. **test-team**, and add **driverbot** and **testbot** into the team
 * Make sure the default public channel **off-topic** exists
 * Create a private channel (ex. "test") in team **test-team**, and add **driverbot** and **testbot** into the private channel
 * Give **drivebot** ADMIN previledge on your testing server, and set **pytest_config.DRIVER_ADMIN_PRIVILEGE = True** if you like to test webhooks and other behaviors which requires admin previledge.

To run the **behavior_tests**, you have to configure **behavior_tests\bot_settings.py** and **behavior_tests\driver_settings.py**. Example configuration:

**driver_settings.py**:

.. code-block:: python

	PLUGINS = [
	]

	BOT_URL = 'http://mymattermost.server/api/v4'
	BOT_LOGIN = 'driverbot@mymail'
	BOT_NAME = 'driverbot'
	BOT_PASSWORD = 'password'
	BOT_TEAM = 'test-team'  # this team name should be the same as in bot_settings
	BOT_CHANNEL = 'off-topic' # default public channel name
	BOT_PRIVATE_CHANNEL = 'test' # a private channel in BOT_TEAM
	SSL_VERIFY = True

**bot_settings.py**:

.. code-block:: python

	PLUGINS = [
	]

	BOT_URL = 'http://mymattermost.server/api/v4'
	BOT_LOGIN = 'testbot@mymail'
	BOT_NAME = 'testbot'
	BOT_PASSWORD = 'password'
	BOT_TEAM = 'test-team'  # this team name should be the same as in driver_settings
	BOT_CHANNEL = 'off-topic'   # default public channel name
	BOT_PRIVATE_CHANNEL = 'test' # a private channel in BOT_TEAM
	SSL_VERIFY = True

Please notice that **BOT_URL**, **BOT_TEAM**, **BOT_CHANNEL**, and **BOT_PRIVATE_CHANNEL** must be the same in both setting files.

After the settings files are done, switch to root dir of mattermost, and run `pytest` to execute test cases.


Test coverage:
--------------

Install pytest-cov_:

.. _pytest-cov: https://pypi.org/project/pytest-cov/

.. code-block:: bash

	$ pip install pytest-cov

Set necessary configuration as described in section **Run the tests**. Then switch to root dir of mattermost, and run:

.. code-block:: bash

	$ py.test --cov=mmpy_bot tests\

It automatically runs tests and measure code coverage of modules under mmpy_bot root dir.
Using **--cov-report** parameter to write report into **cov_html** by **html** format.

.. code-block:: bash

	py.test --cov-report html:logs\cov_html --cov=mmpy_bot tests\