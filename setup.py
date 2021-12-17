import os
import json
from setuptools import setup

pkg_file = os.path.join(os.path.dirname(__file__), "package.json")
with open(pkg_file, "r") as f:
    pkg = json.loads(f.read())

setup(version=pkg["version"])
