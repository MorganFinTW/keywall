from bs4 import BeautifulSoup
from nltk import word_tokenize
from nltk.stem.porter import PorterStemmer
# todo:nltk setup issue
# >>> import nltk
# >>> nltk.download('punkt')

stemmer = PorterStemmer()


def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed


def tokenize(text: str):
    tokens = word_tokenize(text)
    # remove non alphabetic words
    filtered_tokens = [token for token in tokens if token.isalpha()]
    # stem wording
    stems = stem_tokens(filtered_tokens, stemmer)
    return stems


def remove_htmltags(html: str):
    soup = BeautifulSoup(html, "html5lib")
    return soup.get_text()
