import os
import pydoc
import yaml


def get_client(options, *args, **kwargs):

    if options.save:
        kwargs['save'] = True

    class_ = pydoc.locate("client.%s.%s" % (options.source, options.source))
    _client = class_(*args, **kwargs)
    return _client


def save_text_to_file(path: str, file_name: str, text: str):
    path = os.path.abspath(path)
    file_path = "%s/%s" % (path, file_name)

    if not os.path.isdir(path):
        os.mkdir(path)

    with open(file_path, "w") as f:
        f.write(text)


class AttributeDict(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__


Settings = AttributeDict()


def read_config(path: str):
    config_file_path = os.path.abspath(path)
    if os.path.isfile(config_file_path):
        with open(config_file_path, 'r') as config_file:
            config = yaml.load(config_file)
    return config


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
