import pydoc


def get_client(options, *args, **kwargs):
    class_ = pydoc.locate("client.%s.%s" % (options.source, options.source))
    _client = class_(*args, **kwargs)
    return _client
