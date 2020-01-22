import logging
import logging.handlers


class Logger(object):
    """
    class handle logging stuff
    """
    log_name = 'keywall.log'

    def __init__(self, name, prefix='', level=logging.DEBUG, enable=True):
        self._logger = logging.getLogger(name)
        self.prefix = prefix

        # Do not propagate to parent
        self._logger.propagate = 0

        formatstring = ('[%(asctime)s][%(levelname)s][%(name)s]'
                        '[%(process)d %(processName)s]'
                        '[%(funcName)s (line %(lineno)d)]%(message)s')

        if enable:
            file_handler = logging.FileHandler("./%s.log" % self.log_name)
            formatter = logging.Formatter(formatstring)
            file_handler.setFormatter(formatter)
            self._logger.addHandler(file_handler)
        else:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(logging.Formatter(formatstring))
            self._logger.addHandler(console_handler)

        self._logger.setLevel(level)

    def sanitize(self, string: str):
        if self.prefix:
            string = " %s %s" % (self.prefix, string)
        return string

    def debug(self, message, *args, **kwargs):
        return self._logger.debug(self.sanitize(message), *args, **kwargs)

    def info(self, message, *args, **kwargs):
        return self._logger.info(self.sanitize(message), *args, **kwargs)

    def warning(self, message, *args, **kwargs):
        return self._logger.warning(self.sanitize(message), *args, **kwargs)

    def error(self, message, *args, **kwargs):
        return self._logger.error(self.sanitize(message), *args, **kwargs)

    def critical(self, message, *args, **kwargs):
        return self._logger.critical(self.sanitize(message), *args, **kwargs)

    def log(self, level, message, *args, **kwargs):
        return self._logger.log(level, self.sanitize(message), *args, **kwargs)