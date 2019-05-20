def distance(strand_a, strand_b):
    """Returns a hamming distance between two DNA strands."""
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands of unequal lenght.")
    # Forms a list of the nucleotides that are different, and returns lenght.
    return len([(a,b) for a,b in zip(strand_a, strand_b) if a != b])
