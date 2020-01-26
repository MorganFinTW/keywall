import atoma
import requests
from requests.exceptions import RequestException

from client.base import Client
from utility.tokenize import tfidf_vector


class GoogleRSS(Client):
    """
    Grep Google RSS content, and transform into tokens
    """

    def __init__(self, *args, **kwargs):
        super(GoogleRSS, self).__init__(*args, **kwargs)

        self.filename_raw = 'news.rss'
        self.filename_content = 'description.txt'
        self.filename_output = 'output.txt'

    def run(self):
        self.raw = self.get_raw()

        if self.raw:
            feed = self.serializer(self.raw)
            if feed and feed.items:
                (self.content,
                 self.tokens) = self.get_desc_contents_n_tokens(feed.items)

            self.vector = tfidf_vector(self.tokens)

        if self.is_save:
            self.save()

    def get_desc_contents_n_tokens(self, feed_items):
        content, tokens = "", []
        count = 1
        for post in feed_items:
            self._logger.debug("post number: %s" % count)

            self._logger.debug("post content: %s" % post.description)
            content += "%s\n" % post.description

            _plaintext, _tokens = self.get_tokens(post.description)
            self._logger.debug("plaintext: %s" % _plaintext)
            self._logger.debug("tokens: %s" % _tokens)
            tokens.append("%s" % " ".join(_tokens))

            count += 1

        return content, tokens

    def serializer(self, content: bytes):
        feed = None
        try:
            feed = atoma.parse_rss_bytes(content)
        except Exception:
            self._logger.error("can't parser RSS")

        return feed

    def get_raw(self):
        raw = None
        if not self.force_update:
            raw = self.read_raw_from_file()
        return raw if raw else self.get_rss()

    def get_rss(self) -> bytes:
        response = None
        try:
            response = requests.get(self.url)
        except RequestException as e:
            self._logger.error("requests fail: %s" % e)

        return response.content
