import random

def RandomizedMotifSearch(Dna, k, t, N):
    BestMotifs = ["" for _ in range(t)]
    for i in range(t):
        start = random.randint(0, len(Dna[i]) - k)
        BestMotifs[i] = Dna[i][start:start + k]

    for _ in range(N):
        i = random.randint(0, t - 1)
        profile = ProfileWithPseudocounts([motif for idx, motif in enumerate(BestMotifs) if idx != i])
        BestMotifs[i] = ProfileMostProbableKmer(Dna[i], k, profile)

        if Score(BestMotifs) < Score(BestMotifs, [motif for idx, motif in enumerate(BestMotifs) if idx != i]):
            BestMotifs[i] = Dna[i]

    return BestMotifs

def ProfileWithPseudocounts(motifs):
    k = len(motifs[0])
    profile = {"A": [1] * k, "C": [1] * k, "G": [1] * k, "T": [1] * k}
    for motif in motifs:
        for j in range(k):
            profile[motif[j]][j] += 1
    for nucleotide in "ACGT":
        for j in range(k):
            profile[nucleotide][j] /= (len(motifs) + 4)  # Adding 4 for pseudocounts
    return profile

def ProfileMostProbableKmer(text, k, profile):
    max_prob = -1
    most_probable = text[:k]
    for i in range(len(text) - k + 1):
        kmer = text[i:i + k]
        prob = 1
        for j in range(k):
            prob *= profile[kmer[j]][j]
        if prob > max_prob:
            max_prob = prob
            most_probable = kmer
    return most_probable

def Score(motifs, motifs_to_ignore=None):
    if motifs_to_ignore is not None:
        motifs = motifs_to_ignore
    k = len(motifs[0])
    score = 0
    for j in range(k):
        counts = {"A": 0, "C": 0, "G": 0, "T": 0}
        for motif in motifs:
            counts[motif[j]] += 1
        max_count = max(counts.values())
        score += len(motifs) - max_count
    return score

def GibbsSampler(Dna, k, t, N):
    BestMotifs = RandomizedMotifSearch(Dna, k, t, N)
    for _ in range(19):
        motifs = RandomizedMotifSearch(Dna, k, t, N)
        if Score(motifs) < Score(BestMotifs):
            BestMotifs = motifs
    return BestMotifs


with open('GibbsSampler_dataset.txt','r') as file:
    lines = file.readlines()
ktN = lines[0].split()
k = int(ktN[0])
t = int(ktN[1])
N = int(ktN[2])
Dna = [lines[i].replace('\n','') for i in range(1,21)]

BestMotifs = GibbsSampler(Dna, k, t, N)

OutputString = ""

for motif in BestMotifs:
    OutputString += motif+'\n'

with open('output.txt', 'w') as file:
# Write the string to the file
    file.write(OutputString)