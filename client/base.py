
class Client:

    def __init__(self, *args, logger=None, save=False):
        self._logger = logger
        self._save = save

    def run(self):
        raise NotImplementedError

