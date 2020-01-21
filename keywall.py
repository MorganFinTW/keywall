from __future__ import absolute_import

import logging
from optparse import OptionParser

from utility.logger import Logger

if __name__ == '__main__':
    optParser = OptionParser(usage="""
            this script grep articles from internet, and generate the tokens
            with TF-IDF vector.
            """)
    optParser.add_option("--source",
                         default='google',
                         dest="source",
                         help="the input articles rss source.")
    optParser.add_option("--output",
                         default='output.txt',
                         dest="output",
                         help="the output file name.")
    (options, args) = optParser.parse_args()

    logger = Logger('keywall.greper', level=logging.DEBUG)

    try:
        logger.info("keyboard interrupt main tread shutdown")
    except KeyboardInterrupt:
        logger.info("keyboard interrupt main tread shutdown")
