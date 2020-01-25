import atoma
import requests
from requests.exceptions import RequestException

from client.base import Client
from utility.tokenize import tokenize, remove_htmltags, \
    remove_special_character


class GoogleRSS(Client):
    """
    Grep Google RSS content, and transform into tokens
    """

    def __init__(self, *args, **kwargs):
        super(GoogleRSS, self).__init__(*args, **kwargs)

    def run(self):
        raw = self.read_raw_from_file()
        self.raw = raw if raw else self.get_rss()

        if self.raw:
            feed = self.serializer(self.raw)
            if feed and feed.items:
                (self.content,
                 self.tokens) = self.get_desc_contents_n_tokens(feed.items)

        if self.is_save:
            self.save()

    def get_desc_contents_n_tokens(self, feed_items):
        content, tokens = "", ""
        count = 1
        for post in feed_items:
            self._logger.debug("post number: %s" % count)

            self._logger.debug("post summary: %s" % post.description)
            content += "%s\n" % post.description

            _plaintext, _tokens = self.get_tokens(post.description)
            self._logger.debug("text: %s" % _plaintext)
            self._logger.debug("tokens: %s" % _tokens)
            tokens += "%s\n" % _tokens

            count += 1

        return content, tokens

    @staticmethod
    def get_tokens(html: str) -> (str, list):
        text = remove_htmltags(html)  # strip http tags
        plaintext = remove_special_character(text)  # strip http tags
        return plaintext, tokenize(plaintext)

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
