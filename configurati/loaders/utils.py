import code
import re
import sys


def isstring(s):
  """Version of isinstance() that should work with python 2.6/2.7 and python 3+"""
  if sys.version_info[0] < 3:
    return isinstance(s, basestring)
  else:
    return isinstance(s, str)


def substitute(s):
  """Contents of `...` evaluated in Python"""
  if isstring(s) and s.count("`") == 2:
    match = re.search("""^`([^`]+)`$""", s)
    contents, rest = match.group(1), s[match.end():]
    return evaluate(contents)
  else:
    return s


def evaluate(line):
  """Evaluate a line and return its final output"""
  # XXX this isn't smart enough to know about semicolons/newlines in strings,
  # or code where the final result relies on indentation
  line = re.split(";|\n", line)
  line[-1] = "OUTPUT = " + line[-1]
  line = ";".join(line)

  interpreter = code.InteractiveConsole()
  interpreter.push(line)
  return interpreter.locals["OUTPUT"]
