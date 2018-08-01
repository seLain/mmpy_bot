import sys
import os
import json
import pytest
from mmpy_bot.dispatcher import MessageDispatcher

@pytest.fixture(scope="function")
def message():
    with open(os.sep.join(
        ['tests','unit_tests','testdata_message.json']), 'r') as f:
        return json.load(f)

def test_get_message(message):
    if MessageDispatcher.get_message(message) != "hello":
        raise AssertionError()
