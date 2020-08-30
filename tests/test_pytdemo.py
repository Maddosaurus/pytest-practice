from unittest.mock import MagicMock

from pytdemo import pytdemo


# Test basic URL params
def test_base_URL():
    c = pytdemo.CrtSh()
    assert c.base_url == "https://crt.sh/"


def test_get_all_URL(crt_mock, monkeypatch):
    # Set up a mock that will replace the requests module in CrtSh and use it
    # The MagicMock class comes in handy as it does a lot in the background for us.
    requests_mock = MagicMock()
    monkeypatch.setattr(pytdemo.requests, "get", requests_mock)

    crt_mock.get_all("testhost.domain")

    # Check it the requests module was called with the correct URL
    requests_mock.assert_called_once_with(
        "https://test.local/",
        params={"Identity": "testhost.domain", "output": "json"}
    )


def test_get_wo_expired_URL(crt_mock, monkeypatch):
    requests_mock = MagicMock()
    monkeypatch.setattr(pytdemo.requests, "get", requests_mock)

    crt_mock.get_wo_expired("testhost.domain")

    requests_mock.assert_called_once_with(
        "https://test.local/",
        params={"Identity": "testhost.domain", "exclude": "expired", "output": "json"}
    )


def test_get_wo_duplicates_URL(crt_mock, monkeypatch):
    requests_mock = MagicMock()
    monkeypatch.setattr(pytdemo.requests, "get", requests_mock)

    crt_mock.get_wo_duplicates("testhost.domain")

    requests_mock.assert_called_once_with(
        "https://test.local/",
        params={"Identity": "testhost.domain", "deduplicate": "Y", "output": "json"}
    )


def test_get_wo_expired_and_duplicates_URL(crt_mock, monkeypatch):
    requests_mock = MagicMock()
    monkeypatch.setattr(pytdemo.requests, "get", requests_mock)

    crt_mock.get_wo_expired_and_duplicates("testhost.domain")

    requests_mock.assert_called_once_with(
        "https://test.local/",
        params={"Identity": "testhost.domain", "deduplicate": "Y", "exclude": "expired", "output": "json"}
    )
