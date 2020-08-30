from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="PytestPractice",
    version="0.1.0",
    author="Mat",
    author_email="me@sigpwr.de",
    description="Sample package to show off some Python testing best practices.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Maddosaurus/pytest-practice",
    packages=find_packages(),
    install_requires=["requests>=2"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
