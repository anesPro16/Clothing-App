# models.py

from utils import get_valid_float, get_valid_float_edit

class Clothing:
	"""docstring for Clothing"""
	def __init__(self, code, name, price):
		self.code = code
		self.name = name
		self.price = price

class Shirt(Clothing):
	"""docstring for Shirt"""
	def __init__(self, code, name, price, size):
		super().__init__(code, name, price)
		self.size = size

	def display_info(self):
		print("\n---- Data Shirt ----")
		print("Code  : ", self.code)
		print("Name  : ", self.name)
		print("Price : ", self.price)
		print("Size  : ", self.size)
		print()

	def edit_info(self):
		print("\n---- Edit Shirt ----")
		print("(Press Enter to skip and keep old data)")

		# Edit name
		new_name = input(f"Name ({self.name}) : ")
		if new_name.strip() != "":
			self.name = new_name

		# Edit size
		new_size = input(f"Size ({self.size}) : ")
		if new_size.strip() != "":
			self.size = new_size

		#edit price
		self.price = get_valid_float_edit("Price", self.price)

		print("Clothing has changed")

	def format_for_txt(self):
		# format: Tipe|Code|Name|Price|Size\n
		return f"Shirt|{self.code}|{self.name}|{self.price}|{self.size}\n"
		
class Trousers(Clothing):
	"""docstring for Trousers"""
	def __init__(self, code, name, price, colour):
		super().__init__(code, name, price)
		self.colour = colour

	def display_info(self):
		print("\n---- Data Trousers ----")
		print("Code   : ", self.code)
		print("Name   : ", self.name)
		print("Price  : ", self.price)
		print("Colour : ", self.colour)
		print()

	def edit_info(self):
		print("\n---- Edit Trousers ----")
		print("(Press Enter to skip and keep old data)")

		# Edit name
		new_name = input(f"Name ({self.name}) : ")
		if new_name.strip() != "":
			self.name = new_name

		# Edit colour
		new_colour = input(f"Colour ({self.colour}) : ")
		if new_colour.strip() != "":
			self.colour = new_colour

		#edit price
		self.price = get_valid_float_edit("Price", self.price)

		print("Clothing has changed")

	def format_for_txt(self):
		# format: Tipe|Code|Name|Price|Colour\n
		return f"Trousers|{self.code}|{self.name}|{self.price}|{self.colour}\n"
