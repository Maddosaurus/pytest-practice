import pytest

from pytdemo import pytdemo


# This is an example of a fixture.
# The variable "crt_mock" will be available to all tests as an argument
# and contains a version of CrtSh with a patched base_url.
@pytest.fixture(scope="module")
def crt_mock():
    """Create an object with an invalid custom URL to make sure no request passes to crt.sh."""
    c = pytdemo.CrtSh()
    c.base_url = "https://test.local/"
    return c
