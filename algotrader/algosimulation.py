import simulation.stock as simus
import simulation.index as simui
import simulation.szenario as simusz

class AlgoSimulation:

	def __init__(self):
		self.tickers = dict()
		self.indizes = dict()

	def add_ticker(self, ticker, symbol):
		self.tickers[symbol] = ticker

	def add_index(self, index, symbol):
		self.indizes[symbol] = index

	def update(self):
		for ticker in self.tickers:
			self.tickers[ticker].update(simusz.rand_szenario())
		for index in self.indizes:
			self.indizes[index].update()
