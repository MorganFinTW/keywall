from utility.utils import save_text_to_file


class Client:

    raw = None
    content = None
    tokens = None

    def __init__(self, *args, logger=None, save=False):
        self._logger = logger
        self.is_save: bool = save

    def run(self):
        raise NotImplementedError

    def save(self):
        data_list = [
            ('./output/q1/', 'news.rss', self.raw.decode()),
            ('./output/q1/', 'description.txt', self.content),
            ('./output/q1/', 'output.txt', self.content)
        ]

        for path, name, text in data_list:
            if text:
                save_text_to_file(path, name, text)

