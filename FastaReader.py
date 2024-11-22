#!/software/Anaconda3-2023.03/bin/python3
class FastaSlayer:
	def __init__(self, file, type='DNA'):
		self._file = file
		self._type = type
	def read_fastafile(self):
		df = []
		with open(file) as fh:
			for data in fh:
				line = data.rstrip().split('\t')
				df.append(line)
		for value in range(0, len(df), 2):
			key = df[value]
			seq = df[value+1]
			key = ''.join(key)
			key = key[1:]
			seq = ''.join(seq)
			yield (key, seq)
