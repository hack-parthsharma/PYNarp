import os
# import sys


def has_permissions():
    return os.geteuid() == 0