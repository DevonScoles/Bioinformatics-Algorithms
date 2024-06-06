def read_in(file_name):
    with open(file_name, 'r') as file:
        line = file.readline().strip().split()

    length = len(line)
    line[0] = line[0].replace("(", "")
    line[length-1] = line[length-1].replace(")", "")
    for i in range(len(line)):
        line[i] = int(line[i])

    line = [0] + line + [length+1]
    return line

def br_points(permutation):
    breakpoints = 0
    length = len(permutation)
    for i in range(length-1):
        if permutation[i] == permutation[i+1] - 1:
            continue
        else:
            breakpoints += 1

    print(breakpoints)

if __name__ == "__main__":
    permutation = read_in("ComputeBreakpoints/test_input.txt")
    br_points(permutation)
