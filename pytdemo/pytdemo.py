"""This demo module for crt.sh is the base for introcuding test best practices.

It is intentionally a bit too verbose and has multiple methods to show some common use cases.
"""
import logging
import requests
from typing import Any, Dict, List

from pytdemo import util


class CrtSh():
    """A class to interact with crt.sh that returns results in JSON format."""
    def __init__(self):
        self.base_url = "https://crt.sh/"
        self.logger = logging.getLogger("pytest_practice.CrtSh")

    def _call(self, identity: str, **kwargs) -> List[Dict[str, Any]]:
        """Internal function that puts out the actual request to crt.sh."""
        response = requests.get(self.base_url, params={"Identity": identity, "output": "json", **kwargs})
        rjson = response.json()
        return rjson


    def get_all(self, identity: str) -> List[Dict[str, Any]]:
        """Request all certificates for a given identity (i.e. "host.com") known to crt.sh."""
        response = self._call(identity)
        if len(response) >= 1:
            self.logger.debug("Got results. Example: %s", util.partly_pretty_format(response[0]))
        else:
            self.logger.info("No results returned. Maybe check the provided identity?")
        return response

    def get_wo_expired(self, identity: str) -> List[Dict[str, Any]]:
        """Request only certficates for a given identity (i.e. "host.com") that are still valid."""
        return self._call(identity, exclude="expired")

    def get_wo_duplicates(self, identity: str) -> List[Dict[str, Any]]:
        """Request all certificates for a given identity (i.e. "host.com"), deduplicated by certificate."""
        return self._call(identity, deduplicate="Y")

    def get_wo_expired_and_duplicates(self, identity: str) -> List[Dict[str, Any]]:
        """Request all certificates for a given identity (i.e. "host.com") that are still valid, deduplicated by certificate."""
        return self._call(identity, exclude="expired", deduplicate="Y")
