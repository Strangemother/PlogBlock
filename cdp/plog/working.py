from api import Plog
from patterns import PlogBlock, PlogLine

'''
Entry address(es):
  IP address: 10.243.14.48
Platform: Cisco IP Phone 7941,  Capabilities: Host Phone
Interface: FastEthernet0/15,  Port ID (outgoing port): Port 1
Holdtime : 124 sec

Version :
SCCP41.8-2-1S

advertisement version: 2
Duplex: full
Power drawn: 6.300 Watts
Power request id: 23025, Power management id: 3
Power request levels are:6300 0 0 0 0
Management address(es):
'''
f = open('test_data2.txt', 'r')
plog = Plog(f, whitespace='|', terminator=',')
# Capture a device object.
device_block = PlogBlock('Device ID', ref='Device')

footer_line = PlogLine('----------').anything()
device_block.footer = footer_line

lines = {}

lines['ip_line']         = PlogLine('IP address:').anything()
lines['platform_line']   = PlogLine('Platform:').anything()
lines['interface_line']  = PlogLine('Interface:').anything()
lines['holdtime_line']   = PlogLine('Holdtime').maybe(' ').then(':').anything()
lines['version_line']    = PlogLine('Version').maybe(' ').then(':').anything()
lines['ad_version_line'] = PlogLine('advertisement version').anything()
lines['duplex_line']     = PlogLine('Duplex').anything()
lines['pdrawn_line']     = PlogLine('Power drawn').anything()
lines['prid_line']       = PlogLine('Power request id').anything()
lines['prmid_line']      = PlogLine('Power management id').anything()
lines['prl_line']        = PlogLine('Power request levels are').anything()

device_block.add_lines(**lines)

plog.add_blocks(device_block)

plog.run()

data = plog.data_blocks
bl = data[0]
pl = bl.data[0]

from pprint import pprint

print 'data',  len(data[0].data)

import pdb; pdb.set_trace()