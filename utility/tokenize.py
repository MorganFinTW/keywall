from bs4 import BeautifulSoup
from nltk import word_tokenize, re
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer

Stemmer = None


def init_stemmer(options, *args, **kwargs):
    global Stemmer

    if options.stemmer == "porter":
        Stemmer = PorterStemmer()
    elif options.stemmer == "snowball":
        Stemmer = SnowballStemmer("english")


def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed


def tokenize(text: str):
    global Stemmer
    tokens = word_tokenize(text)

    # stem wording
    if Stemmer:
        tokens = stem_tokens(tokens, Stemmer)
    return tokens


def remove_htmltags(html: str) -> str:
    """
    replace html tags with space from content
    :param html:
    :return:
    """
    soup = BeautifulSoup(html, "html5lib")
    return ' '.join(soup.findAll(text=True))


def remove_special_character(text: str) -> str:
    """
    replace some special character with space from text
    :param text:
    :return:
    """
    # https://www.compart.com/en/unicode/
    # remove some non-chinese special symbols
    # https://unicode-table.com/en/blocks/basic-latin/
    # !"#$%'()*+,;<=>[\]^`{|}~
    # https://unicode-table.com/en/blocks/box-drawing/
    # 2500—257F
    # https://unicode-table.com/en/blocks/cjk-symbols-and-punctuation/
    # 3000—303F
    # https://unicode-table.com/en/blocks/cjk-compatibility-forms/
    # FE30—FE4F
    # https://unicode-table.com/en/blocks/halfwidth-and-fullwidth-forms/
    # FF00—FFEF
    return re.sub(r'['
                  r'!"#$%\'()*+,;<=>[\\\]^`{|}~'
                  r'\u2500—\u257F'
                  r'\u3000-\u303F'
                  r'\uFE30-\uFE4F'
                  r'\uFF00-\uFFEF'
                  r']+', ' ', text)
