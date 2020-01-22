from bs4 import BeautifulSoup
from nltk import word_tokenize, re
from nltk.stem.porter import PorterStemmer

# todo:nltk setup issue
# >>> import nltk
# >>> nltk.download('punkt')

Stemmer = PorterStemmer()


def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed


def tokenize(text: str):
    global Stemmer
    tokens = word_tokenize(text)

    # stem wording
    stems = stem_tokens(tokens, Stemmer)
    return stems


def remove_htmltags(html: str):
    soup = BeautifulSoup(html, "html5lib")
    return soup.get_text()


def remove_special_character(text: str):
    # remove non chinese symbols
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
