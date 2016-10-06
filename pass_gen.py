import random
import os
import csv
import sys

lower_case_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_case_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numericals_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_char_list = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '{', '}']
lowercase_alphabet_dictionary = {}
uppercase_alphabet_dictionary = {}
lowercase_reader = csv.reader(open(os.path.join(sys.path[0], 'lower_words.csv')))
uppercase_reader = csv.reader(open(os.path.join(sys.path[0], 'upper_words.csv')))
for row in lowercase_reader:
    lowercase_alphabet_dictionary[row[0]]=row[1:]
for row in uppercase_reader:
    uppercase_alphabet_dictionary[row[0]]=row[1:]

special_char = []
numericals = []
upper_case = []
lower_case = []
simple_pass = []
complex_pass = []
extra_bit = []
temp = []
final_pass_generated = ""
remember_password_generated = []
remember_me = []

class password_generation:
	def __init__(self):
		return None
# Function to generate simple password - assuming that simple passwords cosists of just lower case and upper case characters
	def simple_password(self,pass_length):
		count = int(pass_length/2)
		for i in range(0 , count):
			simple_pass.append(random.choice(lower_case_list))		
			simple_pass.append(random.choice(upper_case_list))			
		mod = pass_length%2
		if mod > 0:
			temp =  self.extra_char(mod) + simple_pass
			random.shuffle(temp)
			simple_password = "".join(temp)
			return simple_password
		else:
			return "".join(simple_pass)
			
# Function to generate complex passwords - these consists of lower case, upper case, numerics as well as special characters
	def complex_password(self,pass_length):
		count = int(pass_length/4)
		for i in range(0 , count):
			complex_pass.append(random.choice(lower_case_list))		
			complex_pass.append(random.choice(upper_case_list))		
			complex_pass.append(random.choice(numericals_list))
			complex_pass.append(random.choice(special_char_list))
		mod = pass_length%4
		if mod > 0:
			temp =  self.extra_char(mod) + complex_pass
			random.shuffle(temp)
			complex_password = "".join(temp)
			return complex_password
		else:
			return "".join(complex_pass)

	def extra_char(self,mod_legth):
		i=1
		while i<=mod_legth:
			if i == 1:
				extra_bit.append(random.choice(lower_case_list))
			elif i == 2:
				extra_bit.append(random.choice(upper_case_list))
			elif i ==3:
				extra_bit.append(random.choice(numericals_list))
			i+=1
		return extra_bit

# Fuction to generate custom pasword based upon the user's requirement

	def custom_password_generation(self, remember = 'no'):
		pass_type = int(input("Which type of password you wish to have? \nPress 1 for Simple \nPress 2 for Complex\n> "))
		char_choice = int(input("\nPress 1 If you wish to specify the type and number of characters you want \nPress 2 If you wish the computer to do it for you\n> "))

		if char_choice == 2:
			pass_length = int(input("\nPlease specify the password length ( between 8-20)\n> "))
			if pass_type == 1 and pass_length in range (8,20):
				final_pass_generated =  self.simple_password(int(pass_length))
				
			elif pass_type == 2 and pass_length in range (8,20):
				final_pass_generated = self.complex_password(int(pass_length))

			else:
				print ("Wrong Input!!")

			if remember == 'yes':
				return (final_pass_generated + "\n" + self.remember_password(final_pass_generated))
			else:
				return final_pass_generated

		elif char_choice == 1 and pass_type == 1:
			user_lower = int(input("Please enter the number of lower case characters\n> "))
			user_upper = int(input("Please enter the number of upper case characters\n> "))
			for i in range (0, user_lower):
				lower_case.append(random.choice(lower_case_list))
			for i in range (0, user_upper):
				upper_case.append(random.choice(upper_case_list))

			temp = lower_case + upper_case
			random.shuffle(temp)
			simple_pass = "".join(temp)
			final_pass_generated = simple_pass

			if remember == 'yes':
				return (final_pass_generated + "\n" + self.remember_password(final_pass_generated))
			else:
				return final_pass_generated

		elif char_choice == 1 and pass_type == 2:
			user_lower = int(input("Please enter the number of lower case characters\n> "))
			user_upper = int(input("Please enter the number of upper case characters\n> "))
			user_numeric = int(input("Please enter the number of numeric characters\n> "))
			user_special_char = int(input("Please enter the number of special characters\n> "))
			for i in range (0, user_lower):
				lower_case.append(random.choice(lower_case_list))
			for i in range (0, user_upper):
				upper_case.append(random.choice(upper_case_list))
			for i in range (0, user_numeric):
				numericals.append(random.choice(numericals_list))
			for i in range (0, user_special_char):
				special_char.append(random.choice(special_char_list))

			temp = lower_case + upper_case + numericals + special_char
			random.shuffle(temp)
			complex_pass = "".join(temp)
			final_pass_generated = complex_pass

			if remember == 'yes':
				return (final_pass_generated + "\n" + self.remember_password(final_pass_generated))
			else:
				return final_pass_generated

# Automatically generate password for the user, takes three parameters: pass_type(can be either simple or complex), length and whether the user need help to remeber the password
	def automated_pass_generation(self,pass_type,length=8, remember='no'):
		
		if length < 8:
			length = 8
			print ("Minimum Length required is 8")
		if pass_type == "simple":
			final_pass_generated = self.simple_password(length)
			
		elif pass_type == "complex":
			final_pass_generated = self.complex_password(length)
			
		else:
			return "Wrong Input"

		if remember == 'yes':
			return (final_pass_generated + "\n" + self.remember_password(final_pass_generated))
		else:
			return final_pass_generated

# Functionality to help User, remember the generated password. 

	def remember_password(self, password):
		list_password = (list(password))

		for i in list_password:
			if i in lowercase_alphabet_dictionary:
				remember_password_generated.append(lowercase_alphabet_dictionary[i])

			elif i in uppercase_alphabet_dictionary:
				remember_password_generated.append(uppercase_alphabet_dictionary[i])

			else:
				remember_password_generated.append(i)


		for i in (remember_password_generated):
			remember_me.append(''.join(i))

		return (' '.join(remember_me))


passGen = password_generation()

print (passGen.custom_password_generation())