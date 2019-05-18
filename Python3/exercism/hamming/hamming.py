def distance(strand_a, strand_b):
    """Returns a hamming distance between two DNA strands."""
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands of unequal lenght.")
    count = 0
    for i in range(len(strand_a)):
            if strand_a[i] != strand_b[i]:
                count += 1
    return count
