def inverse_bwt(transform):
    # Add a sentinel character to the end of the transform
    transform += '$'
    
    # Create a list of cyclic permutations
    cyclic_permutations = [transform]
    for i in range(1, len(transform)):
        cyclic_permutations.append(transform[-i:] + transform[:-i])
    
    # Sort the list lexicographically
    cyclic_permutations.sort()
    
    # The last column of the sorted list is the original string
    original_string = ''.join([s[-1] for s in cyclic_permutations])
    
    return original_string

# Sample input
transform = "GCTGCTATCAAAAAAAGGACCTAAATTTAAAGAAGCGGCTACAAGGCTCCCTCAAGAGTGGAGACCCGTGTTGCAGACGAGCTTGATCAGTATAGACTCCCCGTTACCCCGATGTGAATCCTTATTTGGACTACCGGGAGAGCAAATAAAAGTACTGAAGAACCAGAGGTAGCACGTACGTCCACCTACACTGATACCGTCCTAACAAACCCGTGCGAGTGCTTCGCGTTCGTAGTTAGCCGTTTCTATTCTGTGTTGATTCGGGAGCGGTCGTTCCTGCTCGTAGAATTCACGGTGCTGGTGGTGCAGATCAGCTTTTCCCCCCCCGCGGCGGCATTTGTCAAAATTACGCCCTCGCCGATCGTAAATGCTCTCTGATATTTCCCAATCGCATTCGAAGACCATTTCTGTCTACAAAGAAGGTCACGAGGAAGGAGGGTCGGATCGGCTGCATAATCTGACTCGTTGCACCATGTACCCGTGAACTATCGTCCGCTCGATCTATTGACATATTTCTTTATGCCTGTACTTTACAAGACAAAACCTATTGACCAAAGACATATACAATGAGTTAAGACCAACCTCGCCTCCTAAGGCAT$GCAGCCGCACGGAGAGACAGAGAAGAGAATATGATTTGTCGGATAGCGCCCTAGCTCCCGCATCATGAGGAAGGTCGAGAACGCATACAATCGATAAAACCTGAGGTCTTCGTTGAAGTCCCACATGACAGGATTGCCGTGGCCACTCGAATTAATTGTACACAGATCACTCTTCGCGCTCGGGCAGCTGCACACCCCTCCAGATAGTTTCGTCGGAATTAAGCATTGCGTGTCACCGCCCGG"

# Reconstruct the original string
original_text = inverse_bwt(transform)

# Print the result
print(original_text)