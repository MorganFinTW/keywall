import atoma
import requests
from requests.exceptions import RequestException

from client.base import Client


class GoogleRSS(Client):

    url = 'https://news.google.com/rss?hl=zh-TW&gl=TW&ceid=TW:zh-Hant'

    def __init__(self, *args, **kwargs):
        super(GoogleRSS, self).__init__(*args, **kwargs)

    def run(self):

        rss_resp = self.get_rss()
        if rss_resp:
            feed = self.serializer(rss_resp.content)
            for post in feed.items:
                self._logger.info("post summary: " + post.description)

    def serializer(self, content: bytes):
        feed = {}
        try:
            feed = atoma.parse_rss_bytes(content)
        except Exception:
            self._logger.error("can't parser RSS")

        return feed

    def get_rss(self):
        response = None
        try:
            response = requests.get(self.url)
        except RequestException as e:
            self._logger.error("requests fail: %s" % e)

        return response
