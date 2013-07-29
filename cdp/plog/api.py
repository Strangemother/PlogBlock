'''
Plog.

The api reads through the given file, provided starters, terminators
and key value pair definitions, output it parsed
and applied to an object - later passed through the
api into the django model

Usage: 
    api.py 

Options:
    --pre-compile=False Optionally don't complile string patterns before use
'''
import docopt

import mixins
from patterns import PlogLine, PlogBlock


class Plog( mixins.PlogFileMixin,
            mixins.PlogBlockMixin):

    EMPTY_LINE = '\r\n'

    # Set the whitespace character
    whitespace = ' '

    # A file is read as each line
    # But many commands can be passed
    # into a line.
    terminator = ';'

    def __init__(self, *args, **kwargs):
        self.open_box = None
        self.hash_state = {}
        super(Plog, self).__init__(*args, **kwargs)

    def run(self, parser=None):
        '''
        Begin the process, working the passed
        file. Pass an enumerator method to
        call on each line detection
        '''

        if parser is None:
            parser = self.parse_line

        self.compile_blocks()

        _file = self.get_file()
        line_no = 0
        for line in _file:
            line_no += 1
            parser(line[:-1], line_no=line_no)

        self.close_blocks()
        self.print_status()

    def print_status(self):
        print 'PlogBlocks', self.blocks

    def parse_line(self, line, *args, **kwargs):
        '''
        method is passed to the run and receives
        a single line string to parse and apply PlogLine
        and PlogBlock
        '''
        # Make a plog line.
        pline = PlogLine(line, line_no=kwargs.get('line_no', -1))

        # Find header_line blocks matching this pline
        blocks = self.get_blocks_with_header(pline)
        # one or more blocks detected

        for block in blocks:
            if block.is_open:
                # if block is open, validate and
                # parse its lines only - 
                block.add_data(line)
                block.close()

            



        # Matched blocks with this as a header_line
        # blocks =

        # if in block.
            # line *should exist as a definition in block
            # line should be added to the block.
            # if header line
                # end current block
                # start block
                # add line to block as header line
            # if footer line
                # end current block
                # add line to block as footer line
        # Check against block headers for matches
            # if match
            #   start block
            #   add line to block as header line
        # Check against lines for matches.
            # if match
            # add line
            #


