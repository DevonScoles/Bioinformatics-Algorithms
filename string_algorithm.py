my_string = "GCAGCGAGGACGGATGCAGCGGACGTTCGCCATTTATTCAAAAGGGATAGGCCGTCAAGATCGATTATCAGGGAATAAGGCCTCCCGAACGCCGCGGACGGAAGCAAGGCCATCCAGAGATCAAAAAGGGTTCGCTTTTCGAGCTAAAAGCTGGACGAGGACTCACCACAGACTTGTGAGAAAATCTATGGTTCGCATCAAAGACGATGCGGTGTAGGTTCTCACTTGGCTCGACAGGTCCTATCCTTCGCACAAATGTGGAGGCTTTGATCATACGCTTGCGGCCCTACGGATTGTTGCGCGAAACTGAACGCAATCTCGCCACAGAGCACTCCTGATGTGACGAGGCCGAGCTATGCACGGTGCCCTGTGATCCTCTACATATTTAGGGAAAGGCTGTTCGGTGTTACCCAATCTATGGAGTCCACCGCCTAATTCTGCCTGTTTCGCGCTAGCAAAGGTCGCTCAACGTGATATCAGGCCCGCTCCCCTAAAGTCGCGTAGAAGGGAGACATACCATTCTGGTTCCCACGCGTGGAACCAATCCATTGCGAGCCGCACAGGCATCTGGAGCCTCACGCTGATATCACCGAGTAACGCGCTGGGAAGGAACCGCAGCACTACAACGTGTCGTTAACCCGACTTGCGGTCGGCTCTGCGCTTAGCGCACCAGTCCCCTTCCCACCGAGCTATTTACACGTATTATATGACGCGTCACGTTGTATACTAACGCCGATATCCAACTCAACTTTAAAAGATACTTGTTCGTTCAGGCTTGGAAAGACCTCTAAATGTCATGCCGATCTGGTTTTGTCCTTTCTTGGCAAACGCCACGCCTATTGATAAGTGATGACAAGTTCCAGGCGTGAAAGCTTGTTTCGTCAGGTGCGATGATTCCTGAGCCGACGGCCCCCCACAGAAACTTCGTCGCATAACCTATGGTGTTGGCGTATCCGATAACTTAGAAGAGAACCTGTAACTGCAAGCACTTC"
new_string = ""

for char in my_string:
    if char == 'A':
        new_string += 'T'
    if char == 'C':
        new_string += 'G'
    if char == 'T':
        new_string += 'A'
    if char == 'G':
        new_string += 'C'
    
print(new_string[::-1])