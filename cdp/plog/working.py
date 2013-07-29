from api import Plog
from patterns import PlogBlock, PlogLine
from exampledata import CDP_DATA
plog = Plog(CDP_DATA)
empty_block = PlogBlock('', ref='empty')

# Capture a device object.
device_block = PlogBlock('Device ID', ref='Device')
footer_line = PlogLine('----------').anything()
device_block.footer = footer_line
plog.add_blocks(device_block)
plog.run()
