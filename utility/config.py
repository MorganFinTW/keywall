import os
import yaml


def init_config():
    global Settings
    if not Settings:
        config = read_config('./config.yml')
        Settings.update({
            'LogLevel': config.get('LogLevel'),
            'GoogleRSS': config.get('GoogleRSS'),
            'OUTPUT': config.get('OUTPUT'),
        })
    return Settings


def read_config(path: str):
    config_file_path = os.path.abspath(path)
    if os.path.isfile(config_file_path):
        with open(config_file_path, 'r') as config_file:
            config = yaml.load(config_file)
    return config


class AttributeDict(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__


Settings = AttributeDict()
