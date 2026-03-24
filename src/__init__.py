try:
    from _version import version
    VERSION = version
except FileExistsError:
    VERSION = "0.0.1-nightly"
