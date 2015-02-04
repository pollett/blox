"""scp module"""
import sys, logging, paramiko
from blox.modules.module import module, InvalidInputException, InvalidOutputException
from os.path import basename
logger = logging.getLogger( 'blox.scp' )

class scp(module):
  """scp file to destination"""
  def validateInput(self,input):
    """Expect string as an input"""
    if isinstance( input, str ):
      return input
    raise InvalidInputException( "Expected str, got %s" % type(input), self )
  def validateOutput(self, output):
    """Expect string as return type"""
    if isinstance( output, str ):
      return output
    raise InvalidOutputException( "Expected str, got %s" % type(output), self )
  def output(self, input, params):
    self.validateInput(input)
    logger.debug('SCP file')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect( params['hostname'], username=params['username'], key_filename=params['key_file'])

    dest = input
    if 'dest' in params:
      dest = "%s/%s" % ( params['dest'], basename( input ) )

    sftp = ssh.open_sftp()
    sftp.put( input, dest )
    sftp.close()

    ssh.close()

    logger.debug('File sent to %s' % params['hostname'] )
    return self.validateOutput(input)
