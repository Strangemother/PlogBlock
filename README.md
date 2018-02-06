# Plogblock

Plogblock converts old fashioned log files into funky objects using a python class structure.

Create a `PlogBlock` to match a slice of your text and render clean python `dict` types without heavy lifting. You can capture any string struture allowing you to produce a suite of text conversion tools.


## 20 lines - text to python

Produce line matching for your text information and press go. Ignore the ugly file:

```py
from plogblock import Plog, PlogLine, PlogBlock

# Capture something
block = PlogBlock('Device ID:', ref='Device')
block.header.ref='device_id'
block.footer = PlogLine('----------', ref='footer').anything()

# new parser
f = open('cisco_discovery_protocol_report.txt', 'r')
plog = Plog(f, whitespace='|')

# run it
plog.add_block(block)
blocks = plog.run()

for block in blocks:
    if block.valid():
        print block.as_dict()
```

## Quick Start - More Lines

In this case we're using a Cisco Discovery Protocol file, but any repeating log file will work. Here is an ugly file:

    term|len|0
    AH1CMSW06>
    !
    AH1CMSW06>
    show|cdp|nei|detail
    -------------------------
    Device|ID:|SEP0021550326F6
    Entry|address(es):|
    ||IP|address:|10.243.14.32
    Platform:|Cisco|IP|Phone|7911,||Capabilities:|Host|Phone|
    Interface:|FastEthernet0/7,||Port|ID|(outgoing|port):|Port|1
    Holdtime|:|151|sec

    Version|:
    SCCP11.8-2-1S

    advertisement|version:|2
    Duplex:|full
    Power|drawn:|5.000|Watts
    Power|request|id:|9974,|Power|management|id:|3
    Power|request|levels|are:5000|0|0|0|0|
    Management|address(es):|

    -------------------------
    Device|ID:|SEP001B54527043
    Entry|address(es):|
    ||IP|address:|10.243.14.39

    # .. snip 18 items .. #


We can assume this file is long. Next we create a `PlogBlock` to capture one _object_ from the list

```py
block = PlogBlock('Device ID:', ref='Device')
block.header.ref='device_id'

block.footer = PlogLine('----------', ref='footer').anything()
```

We can see a `PlogBlock` starts at "Device ID:" and ends on a bunch of dashes "------" etc... Anything between is our _block_ of data. We want to extract a single device as a python object. Finally the pipes `|` within the data are whitespace. We can take care of when loading the `Plog` parser:

```python
stream = open('test_data2.txt', 'r')
# new parser
plog = Plog(stream, whitespace='|')
# run it
plog.add_block(block)
blocks = plog.run()
```

The finished blocks are `PlockBlocks` with information of the captured data. The `blocks` from the `run()` method, also exist within `plug.data_blocks`. To retrieve the information in neat manner:

```py
for block in blocks:
    if block.valid():
        print block.as_dict()
```

The result (from our example data) will yield objects with the captured values:

    {'device_id': 'SEP0021550326F6'}
    {'device_id': 'SEP001B54527043'}
    {'device_id': 'SEP001EF7C32410'}
    {'device_id': 'SEP001E7AC45310'}
    {'device_id': 'SEP001F9EAB59F1'}
    {'device_id': 'AH1CMSW07'}
    {'device_id': 'AH1CMSW05'}
    {'device_id': 'SEP001F9EAB5A33'}
    {'device_id': 'SEP001F9EAB3EFC'}
    // snip.


## Smarter with `PlogLine`

A `PlogBlock` defines a sector the text to start and stop scanning. In this case because we start with `Device ID`, we accidentally capture it. The parser knows to close a block with the `block.footer` line.

```
block = PlogBlock('Device ID:', ref='Device')
block.header.ref='device_id'

block.footer = PlogLine('----------', ref='footer').anything()
```

As a block needs a "header" and "footer" (or start and stop) of some text - we apply an alternative to the default _newline/return_ detection. We can target more data within the scope of our `PlogBlock`.

To recap on extra content we can extract from the scoped text:


      show|cdp|nei|detail
      -------------------------
    * Device|ID:|SEP0021550326F6
      Entry|address(es):|
      ||IP|address:|10.243.14.32
      Platform:|Cisco|IP|Phone|7911,||Capabilities:|Host|Phone|
      Interface:|FastEthernet0/11,||Port|ID|(outgoing|port):|Port|1
      Holdtime|:|136|sec

      Version|:
      SCCP41.8-2-1S

      advertisement|version:|2
      Duplex:|full
    //.. snip - ignored


The `block` we created starts at line 3 (noted `*`) due to the "Device ID" detection. It will end on the next line found with repeating dashes - our footer.

Anything within the header and footer can be parsed as another `PlogLine` for our result `dict`. We can add the next line to detect and add to the block:

```py
ip_address = PlogLine('IP address:')
block.add_lines(ip=ip_address)
```

You can add many lines using the `add_lines` method - sequence isn't particularly important. I like to make it slightly easier to by matching the data-pattern. Using the above example text, as a whole it can look something like this:

```py
block = PlogBlock('Device ID:', ref='Device')
block.header.ref='device_id'

block.footer = PlogLine('----------', ref='footer').anything()

lines = {}
lines['entry_address'] = PlogLine('IP address:')
lines['platform'] = PlogLine('Platform:')
lines['interface'] = PlogLine('Interface:')
lines['hold_time'] = PlogLine('Holdtime').maybe(' ').then(':')
lines['version'] = PlogLine('Version').maybe(' ').then(':').multiline()
lines['ad_version'] = PlogLine('advertisement version:')

block.add_lines(**lines)
```

Any content within the scope is a viable `PlogLine`. We expect the line to start with a given string. And end on a newline. Pressing go will yield results - here are two examples:

```py
{'ad_version': '2',
 'device_id': 'AH1CMSW07',
 'entry_address': '10.240.14.3',
 'hold_time': '154 sec',
 'interface': 'GigabitEthernet0/1,  Port ID (outgoing port): GigabitEthernet0/1',
 'platform': 'cisco WS-C3560-24PS,  Capabilities: Switch IGMP',
 'version': 'Cisco IOS Software, C3560 Software (C3560-IPBASEK9-M), Version 12.2(44)SE2, RELEASE SOFTWARE (fc2)\nCopyright (c) 1986-2008 by Cisco Systems, Inc.\nCompiled Thu 01-May-08 15:28 by antonino'}

{'ad_version': '2',
 'device_id': 'SEP001F9EAB59F1',
 'entry_address': '10.243.14.48',
 'hold_time': '124 sec',
 'interface': 'FastEthernet0/15,  Port ID (outgoing port): Port 1',
 'platform': 'Cisco IP Phone 7941,  Capabilities: Host Phone',
 'version': 'SCCP41.8-2-1S'}
```

We can see the first object has screwed up. the `interface`, `version` and `platform` properties have a bunch of other unwanted content. This is due a quirk in the data. a Cisco file uses a comma `,` as a line terminator _sometimes_. As a quick method to victory, you can add addtional file terminators to the parser:

```python
f = open('my_file.txt', 'r')
plog = Plog(f, whitespace='|', terminator=',')
plog.add_block(block)
plog.run()
```

Both _newline/return_ and the `terminator` as comma `,` will correct the line spliting whilst parsing.

## Quick Example

Let's complete the device `PlogBlock`. Defining all everything:

```python
from api import Plog
from patterns import PlogLine as Line, PlogBlock as Block


block = Block('Device ID:', ref='Device')
block.header.ref='device_id'

block.add_lines(
    entry_address=Line('IP address:'),
    platform=Line('Platform:'),
    interface=Line('Interface:'),
    hold_time=Line('Holdtime').maybe(' ').then(':'),
    version=Line('Version').maybe(' ').then(':').multiline(),
    ad_version=Line('advertisement version:'),
    duplex=Line('Duplex:'),
    power_drawn=Line('Power drawn:'),
    power_request_id=Line('Power request id:'),
    power_management_id=Line('Power management id:'),
    power_request_levels=Line('Power request levels are:'),
)

block.footer = Line('----------', ref='footer').anything()
```

That's everything for our example data. A single device entry from the log file. Running this


```py
# new parser
f = open('mylog_file.txt', 'r')
plog = Plog(f, whitespace='|', terminator=',')

# run it
plog.add_block(block)
blocks = plog.run()
```

You'll receive a list of dictionaries for each entry within the log file. Here's a couple from the the example data:

```
{'ad_version': '2',
 'device_id': 'SEP00141C3160E6',
 'entry_address': '10.243.14.37',
 'hold_time': '177 sec',
 'interface': 'FastEthernet0/22',
 'platform': 'Cisco IP Phone 7912',
 'power_drawn': '6.300 Watts',
 'version': 'CP7912-v8-00-2-060817A'}

{'ad_version': '2',
 'device_id': 'SEP001F9EAB5AA3',
 'duplex': 'full',
 'entry_address': '10.243.14.96',
 'hold_time': '138 sec',
 'interface': 'FastEthernet0/3',
 'platform': 'Cisco IP Phone 7941',
 'power_drawn': '6.300 Watts',
 'power_management_id': '3',
 'power_request_id': '23203',
 'power_request_levels': '6300 0 0 0 0',
 'version': 'SCCP41.8-2-1S'}

```


[![Requirements Status](https://requires.io/github/Strangemother/PlogBlock-CDP/requirements.svg?branch=master)](https://requires.io/github/Strangemother/PlogBlock-CDP/requirements/?branch=master)

PlogBlock-for-CDP-files
=======================

PlogBlock is a library designed to extract predictable data from text.

Plogblock for CDP: Convert Cisco Discovery Protocol output to python data.

## Usage:

1. Get your CDP log file (Piping it out from your terminal print)
2. Upload it to the interface
3. Download the CSV conversion


