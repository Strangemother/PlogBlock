from api import Plog
from patterns import PlogBlock, PlogLine

f = open('test_data2.txt', 'r')
plog = Plog(f, whitespace='|')
# Capture a device object.
device_block = PlogBlock('Device ID', ref='Device')
footer_line = PlogLine('----------').anything()
device_block.footer = footer_line
lock = PlogBlock('Duplex', ref='Random').anything()
plog.add_blocks(device_block)
plog.run()
