import pytest

from pytdemo import util


def test_partly_pretty_format_success():
    data = {
        "common_name": "test.name",
        "not_before": "2200-01-01T00:00:01",
        "not_after": "2200-01-01T00:00:02",
        "issuer_name": "C=US, O=Let's Encrypt, CN=Let's Encrypt Authority X3",
        "garbage": "data",
        "something": "else",
    }

    result = util.partly_pretty_format(data)

    assert result == "common_name: test.name -> 2200-01-01T00:00:01 - 2200-01-01T00:00:02 issuer_name: C=US, O=Let's Encrypt, CN=Let's Encrypt Authority X3"


def test_partly_pretty_format_missing_field_raises():
    data = {
        "common_name": "test.name",
        "not_after": "2200-01-01T00:00:02",
        "issuer_name": "C=US, O=Let's Encrypt, CN=Let's Encrypt Authority X3",
    }

    # This test checks explicitely that the KeyError exception is raised.
    # If another Exception (or none at all!) is raised, the test fails
    with pytest.raises(KeyError):
        util.partly_pretty_format(data)


def test_partly_pretty_format_wrong_data_raises():
    data = 42

    # This test checks explicitely that the KeyError exception is raised.
    # If another Exception (or none at all!) is raised, the test fails
    with pytest.raises(TypeError):
        util.partly_pretty_format(data)
