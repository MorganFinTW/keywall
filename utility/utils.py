import os
import pydoc


def get_client(options, *args, **kwargs):

    if options.save:
        kwargs['save'] = True

    class_ = pydoc.locate("client.%s.%s" % (options.source, options.source))
    _client = class_(*args, **kwargs)
    return _client


def save_text_to_file(path: str, file_name: str, text: str):
    file_path = "%s%s" % (path, file_name)

    if not os.path.isdir(path):
        os.mkdir(path)

    with open(file_path, "w") as f:
        f.write(text)
