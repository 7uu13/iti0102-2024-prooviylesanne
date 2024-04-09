import pytest

from network_connections_solution import parse_network_connections

def test_empty_input():
    assert parse_network_connections("") == {}

def test_single_connection_chain():
    assert parse_network_connections("router1:router2,router2:switch1") == {"router1": ["router2"], "router2": ["switch1"]}

def test_multiple_connection_chains():
    assert parse_network_connections("router1:router2:switch1,router1:switch1") == {"router1": ["router2", "switch1"], "router2": ["switch1"]}

def test_complex_network():
    assert parse_network_connections("router2:switch1,switch1:server1,router1:switch1") == {"router2": ["switch1"], "switch1": ["server1"], "router1": ["switch1"]}

def test_network_with_duplicates():
    assert parse_network_connections("router1:router2:switch1,server1:router1") == {"router1": ["router2"], "router2": ["switch1"], "server1": ["router1"]}

# not sure on what to expect from this one, i technically the input is a string not a dict.
def test_network_with_single_device():
    assert parse_network_connections("router1") == {}

if __name__ == "__main__":
    pytest.main()