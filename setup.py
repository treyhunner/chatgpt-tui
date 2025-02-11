import pathlib

from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = ''

# This call to setup() does all the work
setup(
    name="ai",
    version="0.0.1",
    description="",
    long_description=README,
    long_description_content_type="text/markdown",
    url="",
    author="Ben Hammel",
    author_email="bdhammel@gmail.com",
    license="MIT",
    install_requires=["openai"],
    entry_points={
        'console_scripts': ['ai=ai.tui:main'],
    },
)
