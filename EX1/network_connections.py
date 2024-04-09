def parse_network_connections(connections: str) -> dict:
    """
    You're given a log of network connection chains between devices. 

    Each connection chain consists of one device connecting to another, which then connects to yet another device, forming a sequence. 
    Your task is to parse this log and extract the network connection patterns among these devices.

    Write a function parse_network_connections that takes in a string representing the network connection log and returns a dictionary 
    where each key is a device's name and the corresponding value is a list of devices it has connected to.

    Each device name should appear only once in the list, and the order of devices in the lists or keys in the dictionary is not important.

    Input:
    - consists of 0 or more "chains"
    - chains are separated by comma (,)
    - one chain consists of 2 or more device names
    - device name is 1 or more symbols long
    - there are no commas nor colons in the device name
    - device names are separated by colon (:)

    parse_network_connections("") => {}
    parse_network_connections("router1:router2,router2:switch1") => {"router1": ["router2"], "router2": ["switch1"]}
    parse_network_connections("router1:router2:switch1,router1:switch1") => {"router1": ["router2", "switch1"], "router2": ["switch1"]}
    parse_network_connections("router2:switch1,switch1:server1,router1:switch1") => {"router2": ["switch1"], "switch1": ["server1"], "router1": ["switch1"]}
    parse_network_connections("router1:router2:switch1,server1:router1") => {"router1": ["router2"], "router2": ["switch1"], "server1": ["router1"]}

    :param connection_chain: the whole log as a string
    :return: dictionary with connection information
    """
