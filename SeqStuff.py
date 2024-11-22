#!/software/Anaconda3-2023.03/bin/python3
bases = 'tcag'.upper()
codons = [a + b + c for a in bases for b in bases for c in bases]
amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
codon_table = dict(zip(codons, amino_acids))
class Sequence:
	def __init__(self,id,seq):
		self._id = id
		self._seq = seq.upper()
	def __str__(self):
		return ('Seq object ID: {}\tSeq: {}'.format(self.id, self.seq))
	@property
	def id(self):
		return self._id
	@property
	def seq(self):
		return self._seq
	def fasta_form(self):
		output = ('>{}\n{}\n'.format(self.id, self.seq))
		return output
class DNASequence(Sequence):
	def calc_gc_content(self):
		g_count = self.seq.count('G')
		c_count = self.seq.count('C')
		gc_content = ((c_count + g_count) / len(self.seq) ) * 100
		gc_content = round(gc_content, 2)
		return (gc_content)
	def translator(self):
		aas = []
		for split in range(0, len(self.seq), 3):
			codon = self.seq[split:split+3]
			try:
				aa = codon_table[codon]
				aas.append(aa)
			except:      #this removes any of the last ones that dont pop in becayse they arent 3 bases long
				continue
		aas = ''.join(aas)
		return(aas)
	def get_protein_len(self):
		return int(len(self.seq) / 3)
class ProteinSeq(Sequence):
	def __init__(self, id, seq, description=None):
		super().__init__(id, seq)
		self._description = description
	@property
	def description(self):
		return self._description
	def hydro_calc(self):
		hydro_aa = ['A', 'I', 'L', 'M', 'F', 'W', 'Y', 'V']
		count = 0
		for value in self.seq:
			if value in hydro_aa:
				count = count + 1
			else:
				continue
		percent = (count / len(self.seq) ) * 100
		percent = round(percent, 2)
		return percent
	def get_protein_len(self):
		return len(self.seq)
