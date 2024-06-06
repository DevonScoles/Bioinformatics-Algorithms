def generate(s, edges, k):

	add_on = [index for index, item in enumerate(edges) if item[0] == s[-k+1:]]

	if len(add_on) == 0:
		return [s if edges == [] else []]
	else:
		return [generate(s+edges[i][1][-1], edges[:i]+edges[i+1:], k) for i in add_on]

def evacuate(lst):
	for element in lst:
		if isinstance(element, list):
			for subelement in evacuate(element):
				yield subelement		
		else:
			yield element

if __name__ == '__main__':

	with open('GenomeAssembly/test_input.txt') as input_data:
		k_mers = [line.strip() for line in input_data.readlines()]

	k = len(k_mers[0])
	edge = lambda elmt: [elmt[0:k-1],elmt[1:k]]
	DBG_edges = [edge(elmt) for elmt in k_mers[1:]]

	circular_strings = [circular[:len(k_mers)] for circular in set(evacuate(generate(k_mers[0], DBG_edges, k)))]

	print('\n'.join(circular_strings))
	with open('GenomeAssembly/output.txt', 'w') as output_data:
		output_data.write('\n'.join(circular_strings))
