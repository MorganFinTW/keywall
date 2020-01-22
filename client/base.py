from utility.utils import save_text_to_file, init_config


Settings = init_config()


class Client:

    raw = None
    content = None
    tokens = None
    url = None

    def __init__(self, *args, logger=None, save=False):
        global Settings
        self._logger = logger
        self.is_save: bool = save
        self.url = getattr(Settings, self.__class__.__name__)['url']

    def run(self):
        raise NotImplementedError

    def save(self):
        output_setting = Settings.get('OUTPUT')
        data_list = [
            (output_setting.get('q1_path', '.'),
             'news.rss', self.raw.decode()),
            (output_setting.get('q1_path', '.'),
             'description.txt', self.content),
            (output_setting.get('q1_path', '.'),
             'output.txt', self.tokens)
        ]

        for path, name, text in data_list:
            if text:
                save_text_to_file(path, name, text)
