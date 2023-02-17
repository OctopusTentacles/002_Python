

# _*_coding:utf -8 _*_
#!/usr/bin/python3

import random

chars = '+*^%$#@!1234567890qwertyuiopasdfghjklzxcvbnm'
number = int(input('количество паролей'+ "\n"))
length = int(input('длина пароля?' + "\n"))
for n in range(number):
	password = ''
	for i in range(length):
		password += random.choice(chars)
	print(password)
