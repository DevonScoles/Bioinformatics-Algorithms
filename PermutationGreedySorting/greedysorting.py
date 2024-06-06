
def read_in(file_name):
    with open(file_name, 'r+') as file:
        line = file.readline().strip()

    line = line[1:len(line)-1].split()
    permutation = []
    for item in line:
        permutation.append(item)
    return permutation

def rev_subseq(start, end, str):
    seq = str[:start]
    seq += str[start:end][::-1]
    seq += str[end:]
    for i in range(start, end):
        if "+" in seq[i]:
            seq[i] = seq[i].replace("+", "-")
        else:
            seq[i] = seq[i].replace("-", "+")
    return seq

def format(permutation):
    result = " ".join(permutation)
    result = "(" + result + ")"
    return result

def greedy_sort_rev(permutation):
    result = []
    for i in range(1, len(permutation)+1):
        for j in range(i-1, len(permutation)):
            if str(i) == permutation[j][1:]:
                permutation = rev_subseq(i-1, j+1, permutation)
                result.append(format(permutation))
                if "-" in permutation[i-1]:
                    permutation[i-1] = permutation[i-1].replace("-", "+")
                    result.append(format(permutation))
                break
    return result

def write_to_file(file_name, permutation):
    with open(file_name, 'w') as file:
        for i in range(len(permutation)):
            file.writelines(permutation[i]+"\n")

if __name__ == "__main__":
    input = read_in("PermutationGreedySorting/test_input.txt")
    result = greedy_sort_rev(input)
    write_to_file("PermutationGreedySorting/output.txt", result)
