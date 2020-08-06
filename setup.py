import sys
from os import path
from platform import python_version

from setuptools import setup

try:
    import RPi.GPIO
except Exception:
    import fake_rpi

    sys.modules["RPi"] = fake_rpi.RPi  # Fake RPi
    sys.modules["RPi.GPIO"] = fake_rpi.RPi.GPIO  # Fake GPIO
    sys.modules["smbus"] = fake_rpi.smbus  # Fake smbus (I2C)

from hc_sr04 import __version__

version = __version__
long_description = ""
test_requirements = []

this_directory = path.abspath(path.dirname(__file__))

if python_version().startswith("2.7"):
    try:
        with open(path.join(this_directory, "README.md")) as f:
            long_description = f.read()
        with open("test_requirements.txt") as f:
            test_requirements = f.read().splitlines()
    except IOError:
        pass
elif python_version().startswith("3."):
    try:
        with open(path.join(this_directory, "README.md")) as f:
            long_description = f.read()
        with open("test_requirements.txt") as f:
            test_requirements = f.read().splitlines()
    except FileNotFoundError:
        pass

setup(
    name="hc_sr04",
    version=version,
    description="package which delivers hc_sr04",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Jef Neefs",
    author_email="neefsj@gmail.com",
    url="https://github.com/studioj/hc-sr04",
    packages=["hc_sr04"],
    tests_require=test_requirements,
    license="GPL",
    platforms="Posix; MacOS X; Windows",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
