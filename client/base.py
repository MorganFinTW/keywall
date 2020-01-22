from utility.utils import save_text_to_file, read_text_from_file
from utility.config import init_config

Settings = init_config()
output_setting = Settings.get('OUTPUT')


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
        # the data item should include three information.
        # data_item = (`file_path`, `file_name`, `file_content`)
        data_list = [
            (
                output_setting.get('q1_path', '.'),
                'news.rss',
                self.raw.decode()
            ),
            (
                output_setting.get('q1_path', '.'),
                'description.txt',
                self.content
            ),
            (
                output_setting.get('q1_path', '.'),
                'output.txt',
                self.tokens
            )
        ]

        for p, n, c in data_list:
            if c:
                save_text_to_file(p, n, c)

    @staticmethod
    def read_raw_from_file():
        return read_text_from_file(
            output_setting.get('q1_path', '.'),
            output_setting.get('q1_rss', 'news.rss')
        )
