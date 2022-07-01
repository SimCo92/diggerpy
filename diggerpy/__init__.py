"""Top level package for DiggerPy."""
from importlib.metadata import version
from os import getcwd
from os.path import dirname, realpath


__appname__ = 'DiggerPy'
__version__ = version(__name__)
__location__ = dirname(realpath(__file__))
