# iti0102-2024-prooviylesanne 

## EX1 - network_connections

### Rebranded version of a problem that was given to us in the first KT. (KT1 - iti0102-2023)
    You're given a log of network connection chains between devices. 

    Each connection chain consists of one device connecting to another, which then connects to yet another device, forming a sequence. 
    Your task is to parse this log and extract the network connection patterns among these devices.

    Write a function parse_network_connections that takes in a string representing the network connection log and returns a dictionary 
    where each key is a device's name and the corresponding value is a list of devices it has connected to.

    Each device name should appear only once in the list, and the order of devices in the lists or keys in the dictionary is not important.

    parse_network_connections("") => {}
    parse_network_connections("router1:router2,router2:switch1") => {"router1": ["router2"], "router2": ["switch1"]}

## EX2 - get_nucleotides_by_occurrences

### Came up with this one.

    Implement a function that categorizes each symbol in the DNA sequence based on its number of occurrences
    and returns a dictionary where each key is the number of occurrences, 
    and the value is a list of symbols (nucleotides) that appear with that frequency. 

    get_nucleotides_by_occurrences("AACCGT") => {2: ['A', 'C'], 1: ['G', 'T']}
    get_nucleotides_by_occurrences("AAAACCCGGTTT") => {4: ['A'], 3: ['C', 'T'], 2: ['G']}
    get_nucleotides_by_occurrences("") => {}