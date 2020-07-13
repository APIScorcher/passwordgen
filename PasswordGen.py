import random
chars = ("abcdefghijklmnopqrstuvwxyz1234566780$$762$#!?!!0127ABCDEFGHIJKLMNOPQRSTUVWXYZ$@#")

number = input("Input the number of passwords: ")
number = int(number)

length = input("Input the length of the password: ")
length = int(length)

for p in range(number):
	password = ""
	for c in range(length):
		password += random.choice(chars)
	print(password)
		