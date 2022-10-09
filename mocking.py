import random

def mocking_case(s):
  '''
  Transforms a string such that it conveys a mocking tone.

  Keyword arguments:
    s -- The input string to be transformed

  Returns:
    The input string but with some letters in uppercase and some in lowercase
    (e.g. thIs Is An exAMpLe)
   '''
  return ''.join(random.choice([x.upper(), x.lower()]) for x in s)
