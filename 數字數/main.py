import time
import os
while True:
	time.sleep(1)
	os.system("clear")
	text = ""
	with open("in.txt", 'r') as file:
		text = file.read()
	print(len(text))
	print('---')
	print(text)