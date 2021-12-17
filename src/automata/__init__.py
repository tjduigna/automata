from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("automata")
except PackageNotFoundError:
    __version__ = None
