# Pytest-Practice
Example repo containing Python testing best practices I've found for myself.  
It is a combination of `pytest`, `unittest.mock` and serves as a best practice collection and playground to test new things.  

Currently, the main base for tests is a module to interact with https://crt.sh.

## Dev Setup & Tests
To install all requirements, i.e. in a virtual environment, using pip:  
`python -m pip install -r requirements.txt`  
Additionally, to run the tests you'll need to install *pytest*:  
`python -m pip install pytest`  

Afterwards, unit tests can be run from the root directory by invoking *pytest*:  
`python -m pytest`

## Credits
A reasonable part of the organizational structure is based on the excellent ["Hitchhikers Guide To Python" by Kenneth Reitz & Tanja Schlusser](https://docs.python-guide.org/).
Most of the decisions for packaging and setup are taken from the ["Python Packaging User Guide"](https://packaging.python.org/).
For test setup, a mixture of the Hitchhikers Guide and the ["pytest documentation"](https://docs.pytest.org/en/stable) is used.
