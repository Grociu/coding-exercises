# this creates a dictionary that is a translation table 
# for the maketrans() function
code = {
    "G" : "C",
    "C" : "G", 
    "T" : "A", 
    "A" : "U"
    }

def to_rna(dna_strand):
    """This function translates DNA to RNA.
    
    This is using the given dna code and using maketrans() and
    translate() functionality.
    """
    translation = dna_strand.maketrans(code)
    return dna_strand.translate(translation)
    