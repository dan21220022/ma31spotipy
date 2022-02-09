import configparser
import os


def read_config(config_path, *args):
    config = configparser.ConfigParser()
    config.read(config_path)
    for arg in args:
        config = config[arg]
    return config
