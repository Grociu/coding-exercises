# Defines a dictionary of codon - protein pair.
code ={
    ":---" : ":---",
    "AUG" : "Methionine",
    "UUU" : "Phenylalanine",
    "UUC" : "Phenylalanine",
    "UUA" : "Leucine",
    "UUG" : "Leucine",
    "UCU" : "Serine",
    "UCC" : "Serine",
    "UCA" : "Serine",
    "UCG" : "Serine",
    "UAU" : "Tyrosine",
    "UAC" : "Tyrosine",
    "UGU" : "Cysteine",
    "UGC" : "Cysteine",
    "UGG" : "Tryptophan",
    "UAA" : "STOP",
    "UAG" : "STOP",
    "UGA" : "STOP"
}

def proteins(strand):
    """ Returns a list of unique proteins in a RNA strand."""
    protein_list = []
    # Divides the string into a list with three lettes
    codons = [strand[i: i+3] for i in range(len(strand))[::3]]
    for i in codons:
        # Append the list of proteins with unique protein codon value 
        # until stop is hit
        if code[i] != "STOP":
            if code[i] not in protein_list:
                protein_list.append(code[i])
        else:
            return protein_list
    return protein_list