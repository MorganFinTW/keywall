from __future__ import absolute_import

import logging
from optparse import OptionParser

from utility.logger import Logger
from utility.utils import get_client
import client

if __name__ == '__main__':
    optParser = OptionParser(usage="""
            this script grep articles from internet, and generate the tokens
            with TF-IDF vector.
            """)
    optParser.add_option("--source",
                         default='GoogleRSS',
                         dest="source",
                         help="the input articles rss source.")
    optParser.add_option("--output",
                         default='output.txt',
                         dest="output",
                         help="the output file name.")
    (options, args) = optParser.parse_args()

    logger = Logger('keywall.greper', level=logging.DEBUG)

    try:
        client = get_client(options, args)
        client.run()
    except KeyboardInterrupt:
        logger.info("keyboard interrupt main tread shutdown")
