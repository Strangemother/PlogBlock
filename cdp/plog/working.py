from api import Plog
from patterns import PlogBlock

CDP_DATA = '''
Device ID: SEP001F9EAB59F1
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
Management address(es):'''

plog = Plog(CDP_DATA)
empty_block = PlogBlock('', ref='empty')
device_block = PlogBlock('Device ID', ref='Device')
plog.add_blocks(empty_block, device_block)

def runner(line):
    print '"%s"' % ( line )

# plog.run(runner)
plog.run()