import pydoc


def get_client(options, args):
    class_ = pydoc.locate("client.%s.%s" % (options.source, options.source))
    _client = class_(options, args)
    return _client
