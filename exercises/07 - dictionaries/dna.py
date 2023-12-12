def main():
	dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

	nucleoMap = number_nucleotides(dna)

	for k,v in nucleoMap.items():
		print(f"{k} : {v}")

def number_nucleotides(strand):

	nucleo = {'A':0, 'G':0, 'C':0, 'T':0}

	# ADD CODE HERE

	return nucleo

main()