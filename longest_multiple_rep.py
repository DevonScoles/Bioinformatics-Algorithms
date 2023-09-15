#read in text file
with open ('rosalind_lrep.txt','r') as file:
    lines = file.readlines()

sequence = ""
targ_len = 0
node_str = ""
node_lst = []


#Process each line
for i, line in enumerate(lines):
    if i == 0:
        sequence = line
    if i == 1:
        targ_len = line

#takes remaining lines of text file and assigns
# nodes to a string then into a 2D array
node_str = "".join(lines[2:-1])

node_lines = node_str.strip().split('\n')
for line in node_lines:
    elements = line.split()
    node_lst.append(elements)

with open("output.txt",'w') as file:
    file.write(str(node_lst))

def longest_multiple_repeat(s, k, edges):
    lines = edges.split('\n')
    edges = [line.split() for line in lines]
