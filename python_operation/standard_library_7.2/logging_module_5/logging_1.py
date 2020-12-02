"""The logging module offers a full featured and flexible logging system.
--log messages are sent to a file or to sys.stderr.
--Other output options include routing messages through email, datagrams, sockets, or to an HTTP Server.
"""

import logging
logging.debug('Debugging information~')
logging.info('Informational message ~')
logging.warning('Warning: config file %s not found','server.conf')
logging.error('Error occurred~')
logging.critical('Critical error --shutting down')