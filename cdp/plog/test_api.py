from api import Plog
# Test file

def test_file_on_init():
    f = open('file')
    plog = Plog(f)
    assert plog.get_file() == f
    assert plog.get_data() == f

def test_add_file():
    f = open('file')
    plog = Plog()
    plog.set_file(f)
    assert plog.get_file() == f
    assert plog.get_data() == f

def test_add_string():
    CDP_DATA = '''
    Device ID: SEP001F9EAB59F1
    Entry address(es): 
      IP address: 10.243.14.48
    Platform: Cisco IP Phone 7941,  Capabilities: Host Phone 
    Interface: FastEthernet0/15,  Port ID (outgoing port): Port 1
    Holdtime : 124 sec
    '''    
    plog = Plog(CDP_DATA)
    assert plog.get_file()
