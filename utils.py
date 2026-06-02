# modul utilitas

def get_valid_float(pesan_input):
	while True:
		try:
			num = float(input(pesan_input))
			return num

		except ValueError:
			print("Input is not number!")
def get_valid_float_edit(pesan_input, old_value):
	while True:
		# tampilkan pesan beserta nilai lamannya di dalam kurung
		user_input = input(f"{pesan_input} ({old_value}) : ")

		# jika user hanya tekan enter (nilai input kosong)
		if user_input.strip() == "":
			return old_value # kembalikan nilai yang lama

		try:
			num = float(user_input)
			return num
		except ValueError:
			print("Input is not a valid number!")

def get_valid_option_menu(pesan_input, option_list):
	while True:
		option = input(pesan_input)
		if option in option_list:
			return option
		else:
			print("Option is not valid!!")
