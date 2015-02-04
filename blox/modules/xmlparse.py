import logging
from blox.modules.module import module
from blox.exceptions import *
from xml.dom.minidom import parseString
logger = logging.getLogger( 'blox' )

class xmlparse(module):
  def output(self, input, params):
    logger.debug('processing xml')
    if not input:
      raise ParseException( 'Invalid input' )
    xml = parseString( input )
    if not xml:
      raise ParseException( 'Invalid xml' )
    return xml
