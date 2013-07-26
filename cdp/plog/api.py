'''
The api reads through the given
file, provided starters, terminators
and key value pair definitions, output it parsed
and applied to an object - later passed through the
api into the django model
'''


import mixins

class Plog( mixins.PlogFileMixin,
            mixins.PlogBlockMixin):

    EMPTY_LINE = '\r\n'

    # Set the whitespace character
    whitespace = ' '

    # A file is read as each line
    # But many commands can be passed
    # into a line.
    terminator = ';'

    def run(self, parser=None):
        '''
        Begin the process, working the passed
        file. Pass an enumerator method to
        call on each line detection
        '''

        if parser is None:
            parser = self.parse_line

        _file = self.get_file()
        for line in _file:
            parser(line)

    def parse_line(self, line):
        '''
        method is passed to the run and receives
        a single line string to parse and apply PlogLine
        and PlogBlock
        '''

        # Make a plog line.
        pline = PlogLine(line)

        # Find header_line blocks matching this pline
        block = self.get_blocks_with_header(pline)

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


