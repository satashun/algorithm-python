class UnionFind():
	def __init__(self, n):
		self.n = n
		self.par = [-1] * n
		for i in range(0, n):
			self.par[i] = i
		self.rank = [0] * n

	def find(self, x):
		if self.par[x] < 0:
			return x
		else:
			self.par[x] = self.find(self.par[x])
			return self.par[x]

	def unite(self, x, y):
		x = self.find(x)
		y = self.find(y)

		if x == y:
			return 

			if self.rank[x] < self.rank[y]:
				x, y = y, x
		self.par[y] = x
		if self.rank[x] == self.rank[y]:
			self.rank[x] += 1

	def same(self, x, y):
		return self.find(x) == self.find(y)