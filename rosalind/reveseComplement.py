import sys
 
def reverseComplement(dna):
    dna_match = {
        'A' : 'T',
        'T' : 'A',
        'C' : 'G',
        'G' : 'C'
    }

    result = ""
    for c in reversed(dna):
        if c in dna_match:
            result += dna_match[c]
    
    return result


# dna = "AAAACCCGGT"
dna = "GAATGCCGTTATACCCGGCGCGAGTTAAGCAACCGCATATATAACGCGCCCGTGGATAGTCTGGTGCTGTGTCTGCGATACGCAGCCCAAGTTACCCAAACCATTGAATCAATCACCCAGCTCAAAAGTTGGTATCGCCCCTTCGAGCTGCTCAAGACGGGTTCACTTGCCAGACATCCAAGAGACACCTGTGAATGGTACGCCCTAGTGACCAATCAGATTCAAATGAGATAGAATTCCGGCTGCTTTGACGCTAGGAGTCTAAGGCGAACATTGTTCTGACGGATCACCCTCGTGACGTGCGGCACATGTTGCGGACGGATTTACAGGCGGTACGTAAGGCCCTATTTCAGTAATAGGTCGAGCACTACAGCCCTTGCGCCGGGCCACTCACACTGCTGATGGCCGATTGCCTCTTTCCGTTAGCCGTAGGTCGCGTTCGGGTCACTAGGGGAACAGACCTTGTACGCCTGGTTTAATCCCTTGATATGTTTGTTTATCTGATTAGGATGTTATCCAACAACAGACATGCGAAGCCTTCTTCACCTATAAAGTCTTTGGGAACGGTGACTCGGACGGTGTCGTGTAAAAGAATGAGTCTTGTCCTGCACTTTCTCATTAATCGGACTAGTAATGAGCCTGATTTGAAACCTTCGCATGCCTATACCTAGTTACTACTGAAGAAGAGCGCATAAACCGACATTGCACTTGTAAATGAGCAGTGATTGTGGAGAAGTGTCCTGGGCGAGGCGCCTTTCACACCAACCGGGTCCAGTTAGCGATGCAGGGCTAGCAGAGTTCCGGTTGAAGGTGCCTAAGCATGTATTAGTACGGCTTGCGTGAAAGGTAAAAAGCATCGGCTAAGCTATCTCGCACCGGATAATAAAAACGCACTACGTCGC"
print(reverseComplement(dna))
