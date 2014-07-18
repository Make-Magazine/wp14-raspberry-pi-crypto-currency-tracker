class CryptocurrencyApiPuller(object):
	def __init__(self):
		self.last_price = 0
	def get_name(self):
		return ""
	def get_type(self):
		return ""
	def get_price(self, country):
		return 0
	def get_last_price(self):
		return self.last_price