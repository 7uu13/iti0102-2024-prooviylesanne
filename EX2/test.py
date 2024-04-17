import pytest

from dna_solution import get_nucleotides_by_occurrences

def test_empty_input():
    assert get_nucleotides_by_occurrences("") == {}

def test_normal_input_1():
    assert get_nucleotides_by_occurrences("AACCGT") == {2: ['A', 'C'], 1: ['G', 'T']}

def test_normal_input_2():
    assert get_nucleotides_by_occurrences("AAAACCCGGTTT") == {4: ['A'], 3: ['C', 'T'], 2: ['G']}
    
if __name__ == "__main__":
    pytest.main()