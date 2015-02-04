from blox.modules.module import module
from blox.exceptions import *
import logging
logger = logging.getLogger( 'blox.echo' )

class echo(module):
  def input(self, params):
    return params['value']
