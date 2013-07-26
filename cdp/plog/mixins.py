import cStringIO
import patterns

class MixinBase(object):
    ''' Base mixin object of all Plog Mixins to inherit'''
    def __init__(self, *args, **kwargs):
        pass

class PlogFileMixin(MixinBase):
    '''
    A PlogFileMixin is designed to wrap a file object to
    represent correctly for enumeration. You can pass a string or
    a file object.
    Strings are converted to cStringIO.StringIO before use.
    Pass this to the class for easy get_file, set_file methods
    '''
    def __init__(self, *args, **kwargs):
        ''' initial file can be given '''
        self._file = None
        self._data = None

        if len(args) > 0:
            ''' could be file or string'''
            self.set_data(args[0])

        super(PlogFileMixin, self).__init__(*args, **kwargs)

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

class PlogBlockMixin(MixinBase):
    '''
    Methods to assist block design on on a class
    '''
    def __init__(self, *args, **kwargs):
        self._blocks = []
        super(PlogBlockMixin, self).__init__(*args, **kwargs)

    def blocks():
        doc = "The blocks property."
        def fget(self):
            return self._blocks
        def fset(self, value):
            self._blocks = value
        def fdel(self):
            del self._blocks
        return locals()
    blocks = property(**blocks())

    def add_blocks(self, *args):
        '''
        Add a list of blocks to append

            add_blocks(block1, block2, block3, ... )
            add_blocks(*blocks)
        '''
        for block in args:
            self.add_block(block)

    def add_block(self, block):
        '''
        Append a plog block to all valid blocks.
        '''
        _block = block
        if type(block) == str:
            _block = patterns.PlogBlock(block)
        self._blocks.append(_block)

    def get_blocks_with_header(self, *args):
        '''
        Pass on or many PlogLines and return all matching
        blocks with the headers of that type.
        '''
        header_line = args[0]
        # Loop blocks.
        _blocks = []
        for block in blocks:
            if block.header.match(header_line):
                _blocks.append(_block)

        return _blocks