from blox.modules.module import module
from blox.exceptions import *
import urllib2,base64,logging
logger = logging.getLogger( 'blox.url' )

class url(module):
  def input(self, params):
    logger.debug('getting data from url: %s'%params['url'])
    request = urllib2.Request( params['url'] )

    if 'proxyname' in params:
      proxy = urllib2.ProxyHandler({'http': params['proxyname'] })
      opener = urllib2.build_opener( proxy )
      urllib2.install_opener( opener )

    if 'username' in params and 'password' in params:
      base64auth = base64.encodestring('%s:%s' % ( params['username'], params['password'] )).replace('\n','')
      request.add_header("Authorization", "Basic %s" % base64auth)
    try:
      result = urllib2.urlopen( request )
    except urllib2.URLError:
      raise ParseException( 'URL Error' )
    return result.read().strip()
