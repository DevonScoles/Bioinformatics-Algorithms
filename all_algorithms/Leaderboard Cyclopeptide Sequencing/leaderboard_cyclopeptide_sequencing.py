class LeaderboardCyclopeptideSequencing:
    def __init__(self):
        self.read_in('Leaderboard Cyclopeptide Sequencing/test_input.txt')
        print(self.leaderboard_creation(self.spectrumDict, self.N))

    def read_in(self, fileName):
        file = open(fileName, 'r')
        data = [piece.strip() for piece in file]
        self.N = int(data[0])
        data = [int(s) for s in data[1].strip().split()]
        self.parentMass = max(data)
        self.spectrumDict = dict()
        for s in data:
            self.spectrumDict[s] = self.spectrumDict.get(s, 0) + 1
        return       

    def masses(self, version = 0):
        if 0 == version:
            mass = '57 71 87 97 99 101 103 113 114 115 128 129 131 137 147 156 163 186'
            return mass.split()
        if 1 == version:
            return [str(aa) for aa in range(57, 201)]
        
    def calc_mass(self, peptide):
        return sum([int(peps) for peps in peptide.split('-')])

    def expand(self, peptides, version = 0):
        mass = self.masses(version)
        longpep = set()
        for peptide in peptides:
            if '' == peptide:
                for m in mass:
                    longpep.add(m)
            else:
                for m in mass:
                    longpep.add(peptide + '-' + m)
        return longpep
    
    def t(self, leaderboard, spectrumDict, N):
        l = len(leaderboard) 
        linearSDict = dict()
        for peptide in leaderboard:
            linearSDict[peptide] = self.linearS(peptide, spectrumDict)
        lbScore = sorted(linearSDict.items(), key = lambda a:a[1], reverse = True)
        leaderboard = [p[0] for p in lbScore]
        linearSs = [p[1] for p in lbScore]
        for j in range(N, l):
            if linearSs[j] < linearSs[N-1]:
                return leaderboard[:j]
        return leaderboard
    
    def line_spec(self, a_lst):
        length = len(a_lst)
        pre = [0]
        for i in range(length):
            pre.append(pre[i] + a_lst[i])
        linear_spectrum = [0]
        for i in range(length):
            for j in range(i+1, length+1):
                linear_spectrum.append(pre[j] - pre[i])
        current_spectrum = dict()
        for spec in linear_spectrum:
            current_spectrum[spec] = current_spectrum.get(spec, 0) + 1
        return current_spectrum
    
    def cyclopep_spec(self, a_lst):
        n = len(a_lst)
        pre = [0]
        for i in range(n):
            pre.append(pre[i] + a_lst[i])
        pepmass = pre[n]
        cSpec = [0]
        for i in range(n):
            for j in range(i+1, n+1):
                cSpec.append(pre[j] - pre[i])
                if i > 0 and j < n:
                    cSpec.append(pepmass-(pre[j]-pre[i]))
        current_spectrum = dict()
        for s in cSpec:
            current_spectrum[s] = current_spectrum.get(s, 0) + 1
        return current_spectrum

    def linearS(self, peptide, spectrumDict):
        if 0 == len(peptide):
            return 0
        a_lst = [int(aa) for aa in peptide.split('-')]
        theoSpectrumDict = self.line_spec(a_lst)
        score = 0
        for s, v in theoSpectrumDict.items():
            v0 = spectrumDict.get(s, 0)
            if v0 >= v:
                score += v
            else:
                score += v0
        return score
    
    def cyclopeptide_S(self, peptide, spectrumDict):
        if 0 == len(peptide):
            return 0
        a_lst = [int(aa) for aa in peptide.split('-')]
        theoSpectrumDict = self.cyclopep_spec(a_lst)
        score = 0
        for s, v in theoSpectrumDict.items():
            v0 = spectrumDict.get(s, 0)
            if v0 >= v:
                score += v
            else:
                score += v0
        return score

    def leaderboard_creation(self, spectrumDict, N):
        lead_dict = {''}
        lead_peptide = ''
        bestScore = 0
        while len(lead_dict) > 0:
            lead_dict = self.expand(lead_dict)
            removed = []
            for peptide in lead_dict:
                if self.calc_mass(peptide) == self.parentMass:
                    currScore = self.cyclopeptide_S(peptide, spectrumDict)
                    if currScore > bestScore:
                        lead_peptide = peptide
                        bestScore = currScore
                elif self.calc_mass(peptide) > self.parentMass:
                    removed.append(peptide)
            for peptide in removed:
                lead_dict.remove(peptide)
            lead_dict = self.t(lead_dict, spectrumDict, N)
        return lead_peptide

if __name__ == "__main__":
    LeaderboardCyclopeptideSequencing()
