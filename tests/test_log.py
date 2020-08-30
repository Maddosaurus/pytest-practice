"""WARNING! This testsuite has side effects on the log config! Keep that in mind!"""
import logging
from unittest.mock import MagicMock

from pytdemo import pytdemo


def test_get_all_no_results(monkeypatch):
    mock_log = MagicMock()
    monkeypatch.setattr(pytdemo.logging, "getLogger", mock_log)
    monkeypatch.setattr(pytdemo.CrtSh, "_call", MagicMock(return_value=[]))
    # We need to build a manual object to make sure the mocked logger calls get executed
    crt = pytdemo.CrtSh()
    crt.base_url = "https://local.host"

    crt.get_all("some.thing")

    # Hard to read, but this specific part contains the call with the message
    assert mock_log.mock_calls[1][1][0] == "No results returned. Maybe check the provided identity?"
