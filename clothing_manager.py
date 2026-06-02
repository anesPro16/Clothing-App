# clothing_manager.py

import os
from models import Shirt, Trousers

class ClothingList:
	"""docstring for ClothingList"""
	def __init__(self):
		self.clothing_list = []
		self.file_name = "data_pakaian.txt"
	
	def create_clothing(self, cloth):
		self.clothing_list.append(cloth)

	def take_cloth(self, code):
		for cloth in self.clothing_list:
			if cloth.code == code:
				return cloth
		return None

	def delete_cloth(self, code):
		for i, cloth in enumerate(self.clothing_list):
			if cloth.code == code:
				del self.clothing_list[i]
				return True
		return False

	def search_cloth(self, keyword):
		''' cari berdasarkan code atau name '''
		result_searching = []
		keyword = keyword.lower()

		for cloth in self.clothing_list:
			# jika keyword ada di dalam code atau name
			if (keyword in cloth.code.lower()) or (keyword in cloth.name.lower()):
				result_searching.append(cloth)

		# kembalikan berupa list
		return result_searching

	def save_data(self):
		''' Menyimpan seluruh isi list ke dalam file txt'''
		with open(self.file_name, "w") as file:
			for cloth in self.clothing_list:
				# panggil method polymorphism dari langkah 1
				baris_teks = cloth.format_for_txt()
				file.write(baris_teks)

	def load_data(self):
		''' baca file txt dan merakitnya kembali menjadi Object'''
		if not os.path.exists(self.file_name):
			return

		with open(self.file_name, "r") as file:
			for line in file:
				data = line.strip().split("|")

				# pastikan format data valid
				if len(data) == 5:
					tipe = data[0]
					code = data[1]
					name = data[2]
					price = float(data[3]) # kembalikan dalam type data float
					spesifik = data[4] # bisa size atau colour

					# rakit kembali menjadi object berdasarkan tipenyua
					if tipe == "Shirt":
						kemeja = Shirt(code, name, price, spesifik)
						self.clothing_list.append(kemeja)
					elif tipe == "Trousers":
						celana = Trousers(code, name, price, spesifik)
						self.clothing_list.append(celana)
