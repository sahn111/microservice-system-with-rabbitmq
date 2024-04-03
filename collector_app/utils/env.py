import os

def env(key, default):
    return os.getenv(key, default)
