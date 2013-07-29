import re

class PatternBase(object):
    ''' Base mixin object of all Plog Mixins to inherit'''
    def __init__(self):
        pass

def re_escape(fn):
    def arg_escaped(this, *args):
        t = [isinstance(a, VerEx) and a.s or re.escape(str(a)) for a in args]
        return fn(this, *t)
    return arg_escaped


class VerEx(PatternBase):
    '''
    --- VerbalExpressions class ---
    the following methods behave different from the original js lib!

    - end_of_line
    - start_of_line
    - or
    when you say you want `$`, `^` and `|`, we just insert it right there.
    No other tricks.

    And any string you inserted will be automatically grouped
    excepte `tab` and `add`.
    '''
    def __init__(self):
        self.s = ''
        self.modifiers = {'I': 0, 'M': 0}

    def add(self, value):
        self.s += value
        return self

    def regex(self):
        ''' get a regular expression object. '''
        return re.compile(self.s, self.modifiers['I'] | self.modifiers['M'])

    def source(self):
        ''' return the raw string'''
        return self.s
    raw = value = source

    # ---------------------------------------------

    def anything(self):
        return self.add('(.*)')

    @re_escape
    def anything_but(self, value):
        return self.add('([^' + value + ']*)')

    def end_of_line(self):
        return self.add('$')

    @re_escape
    def maybe(self, value):
        return self.add("(" + value + ")?")

    def start_of_line(self):
        return self.add('^')

    @re_escape
    def find(self, value):
        return self.add('(' + value + ')')
    then = find

    # special characters and groups

    @re_escape
    def any(self, value):
        return self.add("([" + value + "])")
    any_of = any

    def line_break(self):
        return self.add("(\\n|(\\r\\n))")
    br = line_break

    @re_escape
    def range(self, *args):
        from_tos = [args[i:i+2] for i in range(0, len(args), 2)]
        return self.add("([" + ''.join(['-'.join(i) for i in from_tos]) + "])")

    def tab(self):
        return self.add('\\t')

    def word(self):
        return self.add("(\\w+)")

    def OR(self, value=None):
        ''' `or` is a python keyword so we use `OR` instead. '''
        self.add("|")
        return self.find(value) if value else self

    def replace(self, string, repl):
        return self.sub(repl, string)

    # --------------- modifiers ------------------------

    # no global option. It depends on which method
    # you called on the regex object.

    def with_any_case(self, value=False):
        self.modifiers['I'] = re.I if value else 0
        return self

    def search_one_line(self, value=False):
        self.modifiers['M'] = re.M if value else 0
        return self
        # work in a similar fashion to Django
# with an attribute loader for filtering a string,
# passed into a regexing lib
# Eg:
#   P(header__istartswith='Device')
class PlogPattern(VerEx):
    '''
    Define a pattern to match within a plog line
    '''
    def __init__(self, *args, **kwargs):
        '''
        defined to be a set of attributes to
        filter the object definition
        '''
        super(PlogPattern, self).__init__(*args, **kwargs)
        if len(args) > 0:
            self.__value = args[0]

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
        footer_line=None, ref=None, *args, **kwargs):
        '''
        Pass the PlogLine used to
        validate a header of a given block.

        The footer_line is optional but would
        automatically terminate upon a new block.
        '''
        super(PlogBlock, self).__init__(*args, **kwargs)

        self._header_line = None
        self._footer_line = None
        self.compiled = None
        self.pre_compile = kwargs.get('pre_compile', True)
        self.ref = ref

        self.header_line(header_line)
        self.footer_line(footer_line)

    def __repr__(self):
        s = self.header.format if self.ref is None else self.ref
        return '<PlogBlock: \'%s\'>' % s

    def __str__(self):
        s = self.header if self.ref is None else self.ref
        return '<PlogBlock: %s>' % s

    def compile(self):
        '''Compile the header object ready to match testing'''
        if self.pre_compile == True:
            if self.header:
                self.compiled = self.header.compile()
            else:
                self.compiled = None
        return self.compiled
                
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

    # method of pattern matching for the regex checking
    method = 'match' # 'search'

    def __init__(self, value=None, block=None, **kwargs):
        '''
        Pass block to define the parent block object of this
        line. This may be None
        '''
        
        # the value found on the last match() method call
        self.matched = None

        self.value = value
        self.block = block
        super(PlogPattern, self).__init__()

        # Assign kwargs correctly into the pattern style. 



    def startswith(self, value):

        self.start_of_line()
        return self.then(value)
        

    def compile(self):
        '''
        ready the matching re regex item for later use. this method considers
        the current regex start and fixes it accordingly.
        '''
        if self.value == '':
            self.compiled = None
        else:
            self.startswith(self.value)
            self.anything()
            self.compiled = self.regex()
        return self.compiled


    def match(self, line):
        '''
        recieve a plogline
        Return tuple of True/False if the value matches the value 
        and the matched object if one exists.
        '''
        matched = None
        if self.compiled:
            matcher = getattr(self.compiled, self.__class__.method)
            matched = matcher(line.value)

        if matched:
            groups = matched.group()
            self.matched = matched.string
            return (True, self.matched)
        else:
            v = line == self.get_value()
            return (v, None)

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def __str__(self):
        return 'PlogLine: \"%s\"' % (self.value)

    def __repr__(self):
        return '<%s>' % self.__str__()
    def __eq__(self, other):
        return self.value == other
