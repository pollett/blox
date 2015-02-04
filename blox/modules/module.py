import inspect, sys

class module(object):
  def validateInput(self, input):
    return input
  def validateOutput(self, output):
    return output
  def input(self, params):
    raise NotImplemented("Input Interface",self)
  def output(self, input, params):
    raise NotImplemented("Output Interface",self)

class TextException(Exception):
  """Wrapper for an exception that takes text input"""
  def __init__(self, value, obj):
    self.value = value;
    self.obj = obj
  def __str__(self):
    comment = inspect.getcomments(self.obj) or "no comment"
    return repr(self.value + " : " + comment + " in " + self.obj.__module__ + "." + self.obj.__class__.__name__)

class NotImplemented(TextException):
  """Exception raised for unimplemented module call."""
  pass

class InvalidInputException(TextException):
  """Exception raised when module receives an incorrect input."""
  pass

class InvalidOutputException(TextException):
  """Exception raised when module sends an incorrect output."""
  pass
