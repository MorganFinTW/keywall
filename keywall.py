from __future__ import absolute_import

import logging
from optparse import OptionParser

from utility.logger import Logger
from utility.tokenize import init_stemmer
from utility.utils import get_client
from utility.config import init_config

if __name__ == '__main__':
    optParser = OptionParser(usage="""
            this script grep articles from internet, and generate the tokens
            with TF-IDF vector.
            """)
    optParser.add_option("--source",
                         default='GoogleRSS',
                         dest="source",
                         help="choose the client resource.")
    optParser.add_option("--enable-save",
                         action="store_true",
                         dest="save",
                         help="enable store output files."
                              " default won't saving anything")
    optParser.add_option("--force-download",
                         action="store_true",
                         dest="force",
                         help="force to renew the source data"
                              " default won't saving anything")
    optParser.add_option("--log",
                         action="store_true",
                         dest="log",
                         help="enable logger to file."
                              " default show log at console only")
    optParser.add_option("--stemmer",
                         default=None,
                         dest="stemmer",
                         help="customize stemmer type, (porter, snowball)")
    (options, args) = optParser.parse_args()

    Settings = init_config()
    level = max(Settings.LogLevel, logging.NOTSET)
    logger = Logger('keywall.greper', level=level, enable=options.log)

    try:
        init_stemmer(options, *args, logger=logger)
        client = get_client(options, *args, logger=logger)
        client.run()
    except KeyboardInterrupt:
        logger.error("keyboard interrupt main tread shutdown")
