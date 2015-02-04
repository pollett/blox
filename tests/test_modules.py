from nose.tools import *
from blox.modules.url import url
from blox.modules.xmlparse import xmlparse
import xml.dom.minidom

def test_url():
  mod = url()
  params = {}
  params['url'] = 'http://www.google.com'
  ret = mod.input(params)
  assert( 'google' in ret )

def test_xml():
  mod = xmlparse()
  input = '<xml><test /></xml>'
  ret = mod.output( input, {} )
  assert( isinstance(ret, xml.dom.minidom.Document) )
