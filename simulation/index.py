import simulation.stock


class Index:

	def __init__(self, name, maxstocks):
		self.name = name
		self.maxstocks = maxstocks
		self.contains = []
		self.halted = False
		self.last_price = 0.0

	def add_stock(self, stock):
		if type(stock) != simulation.stock.Stock:
			return None
		if len(self.contains) == self.maxstocks:
			return False
		else:
			self.contains.append(stock)
			return True

	def remove_stock(self, stock):
		for i in self.contains:
			if i == stock:
				self.contains.remove(i)
				return True
		else:
			return False

	def change_index(self, old, new):
		self.halted = True
		for i in self.contains:
			if i == old:
				self.contains.remove(i)
				returned = self.add_stock(new)
				if returned is None or False:
					self.add_stock(i)
					self.halted = False
					return False
				return True
		else:
			return False

	def get_index_price(self):
		summe = 0
		for s in self.contains:
			summe += s.last_price * s.count / 1_000
		return summe

	def update(self):
		self.last_price = self.get_index_price()

	def __str__(self) -> str:
		string = f'{self.name}: {self.last_price}'
		for s in self.contains:
			string = f'{string}\n{s}'
		return string



