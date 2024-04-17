def get_nucleotides_by_occurrences(dna_sequence: str) -> dict:
    """
    Implement a function that categorizes each symbol 
    in the DNA sequence based on its number of occurrences and returns a dictionary where each key is the number of occurrences, 
    and the value is a list of symbols (nucleotides) that appear with that frequency.

    Input: 
    A string representing a DNA sequence, only containing the characters 'A', 'C', 'G', and 'T'.

    Output:
    get_nucleotides_by_occurrences("AACCGT") => {2: ['A', 'C'], 1: ['G', 'T']}
    get_nucleotides_by_occurrences("AAAACCCGGTTT") => {4: ['A'], 3: ['C', 'T'], 2: ['G']}
    get_nucleotides_by_occurrences("") => {}
    """
    
    occurrence_count = {}

    for nucleotide in dna_sequence:
        if nucleotide in occurrence_count:
            occurrence_count[nucleotide] += 1
        else:
            occurrence_count[nucleotide] = 1

    print(occurrence_count)

    nucleotides_by_occurrences = {}

    for nucleotide, count in occurrence_count.items():
        if count in nucleotides_by_occurrences:
            nucleotides_by_occurrences[count].append(nucleotide)
        else:
            nucleotides_by_occurrences[count] = [nucleotide]

    return nucleotides_by_occurrences