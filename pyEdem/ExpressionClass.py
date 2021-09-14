import re

'''This class is used for all forms of validation check using regular expression'''

def kojo(name:str) ->str:
    '''
        Kojo is a function that takes one args.
        the args is compare to see if it"s a valid name
    '''
    pattern = re.compile('[a-zA-Z]+')
    pat = re.compile(r'[0-9_.)&;,<>@?/^~(\\-]')
    matches = re.finditer(pattern,name)
    for i in matches:
        if re.search(pat,name):
          return None
        else:
            return i.group(0)

def ama(email:str) ->str:
    '''
        ama is a function that takes email as an args and check if
        it is a valid email address.
    '''
    pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    matches = re.finditer(pattern, email)
    for i in matches:
        return i.group(0)
