# work in a similar fashion to Django
# with an attribute loader for filtering a string,
# passed into a regexing lib
# Eg:
#   P(header__istartswith='Device')
class PlogPattern(object):
    '''
    Define a pattern to match within a plog line
    '''
    def __init__(*args, **kwargs):
        '''
        defined to be a set of attributes to
        filter the object definition
        '''

class PlogBlock(PlogPattern):
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
        self._header_line = None
        self._footer_line = None

        self.ref = ref

        self.header_line(header_line)
        self.footer_line(footer_line)

    def __repr__(self):
        s = self.header if self.ref is None else self.header.format
        return '<PlogBlock: \'%s\'>' % s

    def __str__(self):
        s = self.header if self.ref is None else self.header
        return '<PlogBlock: %s>' % s

    def header():
        doc = "The headerline for the PlogBlock"
        def fget(self):
            return self.get_header_line()
        def fset(self, value):
            self.set_header_line(value)
        def fdel(self):
            self.set_header_line(None)
        return locals()
    header = property(**header())

    def footer():
        doc = "The footerline for the PlogBlock"
        def fget(self):
            return self.get_footer_line()
        def fset(self, value):
            self.set_footer_line(value)
        def fdel(self):
            self.set_footer_line(None)
        return locals()
    footer = property(**footer())

    def header_line(self, plog_line):
        ''' The header line of the block
        to validate a start object.'''
        line = plog_line
        if type(plog_line) == str:
            line = PlogLine(plog_line)
        self._header_line = line

    def get_header_line(self):
        return self._header_line

    def footer_line(self, plog_line):
        ''' The footer line of the block
        to validate a start object.'''
        self._footer_line = plog_line

    def get_footer_line(self):
        return self._footer_line

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

class PlogLine(PlogPattern):
    # Define a line to match based upon it's value
    '''Define a single line to match'''
    def __init__(self, format=None, block=None):
        '''
        Pass block to define the parent block object of this
        line. This may be None
        '''
        self.format = format
        self.block = block

    def __str__(self):
        return 'PlogLine: %s' % (self.format)

    def __eq__(self, other):
        return self.format == other
