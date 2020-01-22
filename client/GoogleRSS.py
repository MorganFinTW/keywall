import atoma
import requests
from requests.exceptions import RequestException

from client.base import Client


class GoogleRSS(Client):
    """
    Grep Google RSS content, and transform into tokens
    """
    #
    url = 'https://news.google.com/rss?hl=zh-TW&gl=TW&ceid=TW:zh-Hant'

    def __init__(self, *args, **kwargs):
        super(GoogleRSS, self).__init__(*args, **kwargs)

    def run(self):

        self.raw = self.get_rss()

        if self.raw:
            feed = self.serializer(self.raw)
            if feed.items:
                (self.content, self.tokens) = self.get_description_content_and_tokens(
                    feed.items)

        if self.is_save:
            self.save()

    def get_description_content_and_tokens(self, feed_items):
        content, tokens = "", ""
        for post in feed_items:
            content += "%s\n" % post.description
            self._logger.debug("post summary: " + post.description)

            # TODO: need tokenize post.description
            tokens

        return content, tokens

    def serializer(self, content: bytes):
        feed = None
        try:
            feed = atoma.parse_rss_bytes(content)
        except Exception:
            self._logger.error("can't parser RSS")

        return feed

    def get_rss(self) -> bytes:
        response = None
        try:
            response = requests.get(self.url)
        except RequestException as e:
            self._logger.error("requests fail: %s" % e)

        return response.content
