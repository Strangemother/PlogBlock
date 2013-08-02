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
    def __init__(self, *args, **kwargs):
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
        '''
        Accept any value at this point

            >>> VerEx().anything()

        '''
        return self.add('(.*)')

    @re_escape
    def anything_but(self, value):
        '''
        Accept any value, except the value provided.

            >>> VerEx().anything_but('A-Z0-9')
        '''
        return self.add('([^' + value + ']*)')

    def end_of_line(self):
        '''
        this should be appended last of all your called methods if
        searching for a terminated value.
        Assert the end of a string at this given point

            >>> VerEx('foo').maybe('bar').end_of_line()
        '''
        return self.add('$')

    @re_escape
    def maybe(self, value):
        '''
        The value passed is potentially a match

            >>> VerEx('foo').maybe('bar')
        '''
        return self.add("(" + value + ")?")

    def start_of_line(self):
        '''
        this is used internally when required.
        '''
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
        self._ref = None

        if len(args) > 0:
            self.__value = args[0]

        self.set_ref( kwargs.get('ref', None) )

        super(PlogPattern, self).__init__(*args, **kwargs)

    def ref():
        doc = "The ref property."
        def fget(self):
            return self.get_ref()
        def fset(self, value):
            self.set_ref(value)
        return locals()

    ref = property(**ref())

    def set_ref(self, value):
        self._ref = value

    def get_ref(self):
        return self._ref


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

    def __init__(self, *args, **kwargs):
        '''
        Pass the PlogLine used to
        validate a header of a given block.

        The footer_line is optional but would
        automatically terminate upon a new block.
        '''
        self._ref=None
        self._lines = []
        self.is_open = False
        self._header_line = None
        self._footer_line = None
        self.compiled = None
        self.pre_compile = kwargs.get('pre_compile', True)
        self.data = []
        hl = args[0] if len(args) > 0 else None
        fl = args[1] if len(args) > 1 else None
        self.set_header_line(hl)
        self.set_footer_line(fl)
        super(PlogBlock, self).__init__(*args, **kwargs)

    def __repr__(self):
        s = self.header.format if self.ref is None else self.ref
        c = len(self.data)
        return '<%s: \'%s\'~%s>' % (self.__class__.__name__, s, c)

    def __str__(self):

        s = self.header if self.ref is None else self.ref
        c = len(self.data)
        return "<%s: %s~%s>" % (self.__class__.__name__, s, c)


    def add_data(self, data):
        self.data.append(data)

    def compile(self):
        '''Compile the header object ready to match testing'''

        if self.pre_compile == True:
            if self.header:
                self.header_compiled = self.header.compile()
            else:
                self.header_compiled = None

        if self.pre_compile == True:
            if self.footer:
                self.footer_compiled = self.footer.compile()
            else:
                self.footer_compiled = None

        return (self.header_compiled, self.footer_compiled)

    def add_lines(self, *args, **kwargs):
        '''
        Apply arguments for each line added to the validation routine
        '''
        for line in args:
            self.add_line(line)

        for ref in kwargs:
            line = kwargs[ref]
            if line.ref is None:
                line.ref = ref
            else:
                line._kwarg = ref
            self.add_line(line)

    def add_line(self, plog_line):
        '''
        Apply a PlogLine to the PlogBlock. If the line is a string,
        it'll be converted to a PlogLine
        '''
        line = plog_line
        if type(plog_line) == str:
            line = PlogLine(plog_line)
        self._lines.append(line)


    def lines():
        doc = "The lines property."
        def fget(self):
            return self._lines
        def fset(self, value):
            self._lines = value
        def fdel(self):
            del self._lines
        return locals()
    lines = property(**lines())

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

    def set_header_line(self, plog_line):
        ''' The header line of the block
        to validate a start object.'''

        line = plog_line
        if type(plog_line) == str:
            line = PlogLine(plog_line)
        self._header_line = line

    def get_header_line(self):
        return self._header_line

    def set_footer_line(self, plog_line):
        ''' The footer line of the block
        to validate a start object.'''
        line = plog_line
        if type(plog_line) == str:
            line = PlogLine(plog_line)
        self._footer_line = line

    def get_footer_line(self):
        return self._footer_line

    def open(self):
        ''' Open the block during file enumeration to
        begin recieve lines'''
        self.is_open = True

    def close(self):
        self.is_open = False


# Device ID: AH1CMSW07
# Entry address(es):
#   IP address: 10.240.14.3
# Power request id: 23025, Power management id: 3

class DjangoPlogBlock(PlogBlock):
    '''
    Wraps a PlogBlock into a django mode using ref's from
    field values.
    '''


class PlogLine(PlogPattern):
    # Define a line to match based upon it's value
    '''Define a single line to match'''

    # method of pattern matching for the regex checking
    method = 'match' # 'search'

    def __init__(self, value=None, block=None, *args, **kwargs):
        '''
        Pass block to define the parent block object of this
        line. This may be None
        '''

        self._ref=None
        # the value found on the last match() method call
        self.matched = None
        self.line_no = kwargs.get('line_no', -1)
        self.value = value
        self.block = block
        super(PlogPattern, self).__init__(*args, **kwargs)

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
            return (True, matched)
        else:
            v = line == self.get_value()
            return (v, None)

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def __str__(self):
        return 'PlogLine #%s: \"%s\"' % (self.line_no, self.value,)

    def __repr__(self):
        return '<%s>' % self.__str__()

    def __eq__(self, other):
        return self.value == other
