import atoma
import requests
from requests.exceptions import RequestException

from client.base import Client
from utility.tokenize import tokenize, remove_htmltags


class GoogleRSS(Client):
    """
    Grep Google RSS content, and transform into tokens
    """

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
            self._logger.debug("post summary: %s" % post.description)
            content += "%s\n" % post.description

            # TODO: need tokenize post.description
            _tokens = self.get_tokens(post.description)
            self._logger.debug("tokens: %s" % _tokens)
            tokens += "%s\n" % _tokens

        return content, tokens

    def get_tokens(self, html: str):
        text = remove_htmltags(html)  # strip http tags
        return tokenize(text)

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
