from pathlib import Path
from setuptools import setup, find_packages


def get_req_file() -> list[str]:

    base_dir = Path(__file__).parents[2]
    with open(f"{base_dir}/requirements.txt", "r") as f:
        return [x.strip("\n") for x in f.readlines()]


setup(
    name='RevoDiscord',
    version='1.0',
    author='Felix Schmidt',
    author_email='Felix-schmidt2@outlook.de',
    description='Team Revolution discord bot',
    packages=find_packages()
)
