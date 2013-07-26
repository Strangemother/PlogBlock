'''
The api reads through the given
file, provided starters, terminators
and key value pair definitions, output it parsed
and applied to an object - later passed through the 
api into the django model
'''


import cStringIO

class Plog(object):

    EMPTY_LINE = '\r\n'

    # Set the whitespace character
    whitespace = ' '
    
    # A file is read as each line
    # But many commands can be passed
    # into a line.
    terminator = ';'

    def __init__(self, *args, **kwargs):
        ''' initial file can be given '''
        self._file = None
        self._data = None
        if len(args) > 0:
            ''' could be file or string'''
            self.set_data(args[0])
            

    def set_file(self, log_file):
        ''' Add a file to the class to parse 
        This will return a StringIO if a string
        was passed as data.'''
        self.set_data(log_file)

    def set_data(self, data):
        ''' wrapper for applying the file content
        to the class'''
        if type(data) == str:
            output = cStringIO.StringIO(data)
            self._data = output
        else:
            self._data = data

    def get_data(self):
        return self._data

    def get_file(self):
        ''' return the internal file,
        This will return a StringIO if a string
        was passed as data
        '''
        return self.get_data()

class PlogBlock(object):
    '''
    A block of definable content, containing
    a list of Plog lines.

    When a PlogBlock is used when commanded for use
    during the parsing of a file - all lines
    after are passed into the block as lines 
    associated with it's context. This will 
    occur until a PlockBlock terminator line 
    is parsed of PlogBlock().drop()
    is called whist context is open.


    '''
    def __init__(self, header_line=None, \
        footer_line=None, ref=None):
        '''
        Pass the PlogLine used to 
        validate a header of a given block.

        The footer_line is optional but would 
        automatically terminate upon a new block.
        '''
        self.ref = ref
        self.header_line(header_line, footer_line)

    def header_line(plog_line):
        ''' The header line of the block
        to validate a start object.'''
        self._header_line = plog_line

    def get_header_line(self):
        return self._header_line

    def lines(self):
        '''
        Return a list of lines applied to the
        block when the block has received some
        content. 
        '''
# Device ID: AH1CMSW07
# Entry address(es): 
#   IP address: 10.240.14.3
# Power request id: 23025, Power management id: 3

class PlogLine(object):
    # Define a line to match based upon it's value
    '''Define a single line to match'''
    def __init__(self, format=None):
        self.format = format



# work in a similar fashion to Django
# with an attribute loader for filtering a string,
# passed into a regexing lib
# Eg:
#   P(header__istartswith='Device')
class PlogPattern():
    '''
    Define a pattern to match within a plog line
    '''
    def __init__(*args, **kwargs):
        '''
        defined to be a set of attributes to 
        filter the object definition
        '''