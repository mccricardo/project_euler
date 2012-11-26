from functools import reduce
from operator import mul

class Grid:
	def __init__(self, filename, size):
		with open(filename, 'r') as f:
			self.data = [[int(x) for x in line.split()] for line in f]
		f.closed
		self.rows = len(self.data)
		self.columns = len(self.data)
		self.diagonal_size = size

	def gen_tuples(self, x):
		four = list(range(self.diagonal_size))
		for i in range(self.diagonal_size*self.diagonal_size):
			for j in range(self.diagonal_size*self.diagonal_size):
				yield (x[i][j+k] for k in four)
				yield (x[i+k][j] for k in four)
				yield (x[i+k][j+k] for k in four)
				yield (x[i+3-k][j+k] for k in four)
	
	def max(self):
		print(max(reduce(mul, t) for t in self.gen_tuples(self.data)))

grid = Grid("number_grid.txt", 4)

grid.max()



