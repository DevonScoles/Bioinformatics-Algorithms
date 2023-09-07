def min_skew_positions(genome):
    min_skew = float('inf')  # Initialize minimum skew to positive infinity
    skew = 0                # Initialize current skew to 0
    min_positions = []      # List to store positions where skew is minimized
    skew_lst = []

    for i in range(len(genome)):
        if genome[i] == 'G':
            skew += 1
        elif genome[i] == 'C':
            skew -= 1
        skew_lst.append(skew)

        if skew < min_skew:
            min_skew = skew
            min_positions = [i + 1]
        elif skew == min_skew:
            min_positions.append(i + 1)
        print(min_positions)

    return min_positions, skew_lst

# Example usage:
genome = "CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG"
result = min_skew_positions(genome)
print(" ".join(map(str, result[0])))