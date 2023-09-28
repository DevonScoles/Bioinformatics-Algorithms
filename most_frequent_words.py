def frequent_words(text, k):
    # Initialize a dictionary to store k-mers and their counts
    kmer_counts = {}
    max_count = 0
    
    # Loop through the text in sliding windows of size k
    for i in range(len(text) - k + 1):
        kmer = text[i:i + k]
        
        # Check if the k-mer is already in the dictionary
        if kmer in kmer_counts:
            kmer_counts[kmer] += 1
        else:
            kmer_counts[kmer] = 1
        
        # Update the maximum count
        max_count = max(max_count, kmer_counts[kmer])

            # Collect k-mers with the maximum count
    most_frequent_kmers = [kmer for kmer, count in kmer_counts.items() if count == max_count]
    
    return most_frequent_kmers

# Example usage:
text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4
result = frequent_words(text, k)
print(" ".join(map(str,result)))