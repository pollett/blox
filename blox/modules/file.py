import sys, logging
from blox.modules.module import module
logger = logging.getLogger( 'blox.file' )

class file(module):
  def input(self, params):
    logger.debug('Waiting for file input')
    return "".join(sys.stdin.readlines())
  def output(self, input, params):
    logger.debug('Writing to file: %s'%params['file'])
    f = open( params['file'], 'w' )
    f.write( input )
    f.close()
    return params['file']
