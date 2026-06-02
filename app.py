# app.py

from utils import get_valid_option_menu, get_valid_float
from models import Shirt, Trousers
from clothing_manager import  ClothingList

class ClothManageApp:
	"""docstring for ClothManageApp"""
	def __init__(self):
		self.clothing_list = ClothingList()

		# load data saat aplikasi dibuka
		self.clothing_list.load_data()

	def run(self):
		while True:
			print("\n === Simple Clothing APP ===")
			print("\n1. Create Clothing")
			print("2. Read Clothing List")
			print("3. Search Clothing")
			print("4. Exit")

			option = get_valid_option_menu("Choose Menu : ", ["1", "2", "3", "4"])

			if option == "1":
				self.run_create_clothing()
			elif option == "2":
				self.run_read_clothing_list()
			elif option == "3":
				self.run_search_clothing()
			elif option == "4":
				# save data saat aplikasi mau ditutup
				self.clothing_list.save_data()
				break

	def run_create_clothing(self):
		while True:
			print("\n--- Create Clothing ---")
			print("\n1. Create Shirt")
			print("2. Create Trousers")
			print("3. Back")

			option = get_valid_option_menu("Choose Menu : ", ["1", "2", "3"])

			if option == "1":
				self.run_create_shirt()
			elif option == "2":
				self.run_create_trousers()
			elif option == "3":
				break

	def _get_valid_new_code(self):
		''' cek validasi code  '''
		code = input("Code : ")
		if self.clothing_list.take_cloth(code) is not None:
			print(f"Error: Clothing with code '{code}' already exists!")
			return None
		return code


	def run_create_shirt(self):
		print("\nCreate Shirt")
		code = self._get_valid_new_code()
		if code is None: return # gagal jika code sudah ada

		name = input("Name : ")
		size = input("Size : ")
		price = get_valid_float("Price : ")

		data_shirt = Shirt(code, name, price, size)
		self.clothing_list.create_clothing(data_shirt)

	def run_create_trousers(self):
		print("\nCreate Trousers")
		code = self._get_valid_new_code()
		if code is None: return # gagal jika code sudah ada

		name = input("Name : ")
		colour = input("Colour : ")
		price = get_valid_float("Price : ")

		data_trousers = Trousers(code, name, price, colour)
		self.clothing_list.create_clothing(data_trousers)

	def run_read_clothing_list(self):

		# Cek, apakah data pakaian ada
		if not self.clothing_list.clothing_list:
			print("\n Clothing List is Empty!")
			return

		print("\n === All Clothing ===")
		for cloth in self.clothing_list.clothing_list:
			cloth.display_info()

		print("\nMenu")
		print("1. Edit Clothing")
		print("2. Delete Clothing")
		print("3. Back")

		option = get_valid_option_menu("Choose Menu : ", ["1", "2", "3"])

		if option == "1":
			self.run_edit_clothing()
		elif option == "2":
			self.run_delete_clothing()

	def run_search_clothing(self):
		keyword = input("\n Input Code or Name to search : ")

		# panggil fungsi search dari gudang
		result = self.clothing_list.search_cloth(keyword)

		if len(result) == 0:
			print(f"Clothing with keyword '{keyword}' not found!")
		else:
			print(f"\nFound {len(result)} item(s) : ")
			for cloth in result:
				cloth.display_info()

	def run_delete_clothing(self):
		code = input("Input Code to Delete : ")
		if self.clothing_list.delete_cloth(code):
			print("Clothing has been deleted! \n")
		else:
			print("Code is not found!! ", code)

	def run_edit_clothing(self):
		code = input("Input Code to Edit : ")
		cloth = self.clothing_list.take_cloth(code)

		if cloth is None:
			print("Clothing is not found!! ", code)
		else:
			# panggil method edit_info
			cloth.edit_info()