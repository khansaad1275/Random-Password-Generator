import random
import os
import time
import sys
import clipboard


choice = 100
def typewriter(message,dealy):
			for char in message:
				sys.stdout.write(char)
				sys.stdout.flush()

				if char !="\n":
					time.sleep(dealy)
				else:
					time.sleep(0.5)

while(choice != 0 ):
	os.system('cls')
	print(' ')
	print('     ▄▀▀▀▄   RP Generator™         ')
	print('     █   █   Version 1.0           ')
	print('    ███████         ▄▀▀▄           ')
	print('   ░██─▀─██░░█▀█▀▀▀▀█░░█░          ')
	print('   ░███▄███░░▀░▀░░░░░▀▀░░          ')
	print("╔════════════════════════════════════════╗")                                                                         
	print("║ ♚ Project Name : RP Generator™         ║")
	print("║ ♚ Author : Khan Saad                   ║")
	print("║ ♚ Github : github.com/khansaad1275     ║")
	print("╠════════════════════════════════════════╝")
	print("║[1] Simple Random Passwords ") 
	print("║[2] Strong Rememberable Passwords ") #specify the size of password 
	print("║[3] Manual Digit Passwords ")
	print("║[4] Scribbeled passwords ") #aljksbfjiasni321@!E32r
	print("║[5] About Me ")
	print("║[0] Exit ")

	choice = int(input('>>>> Select an Option : ')) 

	symbols = ['@', '#', '$', '_',' @', '=', '?', '.', '/','*','@']
	i = 0


#1 RPG Memorable passwords
	if choice == 1:
		print(" ")
		amount = int(input("Enter The Number of Passwords you wanna Generate : "))
		while(i < amount):
			with open("noun.txt", "r") as f:
			    lines = f.readlines()
			    noun = (random.choice(lines))

			with open("adjectives.txt", "r") as f:
			    lines = f.readlines()
			    adjective = (random.choice(lines))

			rnumber = random.randrange(9999)
			rsymbol = random.choice(symbols)

			password = noun.strip() + adjective.strip() + rsymbol +str(rnumber)
			print(" ")
			i += 1
			print(" ")
			print(">>> ",end='')
			typewriter(password,0.03)
			time.sleep(0.5)
		print(" ")
		print(" ")
		input('>   Press Enter for main menu...  ')
		print(" ")	
		typewriter("Exiting this menu",0.05)
		os.system('cls')



#2 Strong remabarable passwords
	if choice == 2:
		print(" ")

		amount = int(input("Enter The Number of Passwords you wanna Generate : "))
		while(i < amount):
			with open("noun.txt", "r") as f:
			    lines = f.readlines()
			    noun = (random.choice(lines))

			with open("adjectives.txt", "r") as f:
			    lines = f.readlines()
			    adjective = (random.choice(lines))

			password = noun.strip() + adjective.strip()

			password = password.replace("i","1",1)
			password = password.replace("o","0",1)
			password = password.replace("L","7",1)
			password = password.replace("a","@",1)
			password = password.replace("s","$",1)

			i += 1
			print(" ")
			print(">>> ",end='')
			typewriter(password,0.03)
			time.sleep(0.5)
			print(" ")
		print(" ")
		typewriter('>>> Tip : The Above Passwords are Combinations of English words I have Just Replaced i with 1,o with 0,L with 7,a with @,s with $, so its still readable.',0.03)
		print(" ")
		print(" ")
		input('>   Press Enter for main menu...  ')
		print(" ")	
		typewriter("Exiting this menu",0.05)
		os.system('cls')




#3 Manual DIGIT RPG
	elif (choice == 3):
		size = int(input("Enter The Number of Digits your password should have (e.g: 13) : "))
		
		if (size < 7) :
			print(" ")
			typewriter('>!!  If you Want your password less then 7 digit then just use 123456 or qwerty or maybe 007007 as your password :) ',0.02)
			print(" ")
			print(" ")
			input('>   Press Enter for main menu...  ')
			os.system('cls')
		else:

			j = 0
			for j in range(3):
				b = True
				while(b == True):
					with open("noun.txt", "r") as f:
					    lines = f.readlines()
					    noun = (random.choice(lines))

					with open("adjectives.txt", "r") as f:
					    lines = f.readlines()
					    adjective = (random.choice(lines))

					rnumber = random.randrange(9999)
					rsymbol = random.choice(symbols)

					password = noun.strip() + adjective.strip() + rsymbol +str(rnumber)



					if (len(password) == size):
						print(" ")
						print(">>> ",end='')
						typewriter(password,0.1)
						i += 1
						b = False
						j += 1
						print(" ")		
			print(" ")
			print(" ")
			input('>   Press Enter for main menu...  ')
			print(" ")
			typewriter("Exiting this menu",0.05)
			os.system('cls')

#4 Skribbeled RPG
	elif (choice == 4):
		
		print(' ')
		size = int(input("> Enter The Number of Digits your password should have (Def: 13) : "))
		chars = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%&*_+ABCDEFGHIJKLMNOPQRSTUVWXYZ'


		passwordall = " "
		# here change the range to increase the number of RPGenerated
		for x in range(3):
			password = ''
			for c in range(size):
				password += random.choice(chars)
			print(" ")
			print(">>> ",end='')
			typewriter(password,0.05)
			print(" ")
			time.sleep(0.8)
			passwordall += password
		 

		print(" ")
		copychoice = int(input('>   Press 1 to copy the Passwords on your clipboard or Press 0 to Exit : '))
		if copychoice == 1:
			clipboard.copy(passwordall)  
			text = clipboard.paste() 
		else:
			print(" ")
			typewriter("Exiting this menu",0.05)
		os.system('cls')


#4 About Me
	elif (choice == 5):

		def typewriter(message):
			for char in message:
				sys.stdout.write(char)
				sys.stdout.flush()

				if char !="\n":
					time.sleep(0.05)
				else:
					time.sleep(0.5)

		typewriter("  ___  \n\
 |[_]| RP Generator™ \n\
 |+ ;| Version 1.0 \n\
 '---' Last-Update 19 June 21 \n\
 \n\
 \n\
 [ɴᴀᴍᴇ] = [Khan Saad Maqsood] \n\
 [ᴡᴇʙsɪᴛᴇ] = [www.#######.Tech] \n\
 [ɢɪᴛʜᴜʙ] = [https://github.com/khansaad1275] \n\
 [ɪɴsᴛᴀɢʀᴀᴍ] = [www.instagram.com/skhan_official/] \n\
 \n\
 ")

		
		print(" ")
		input('>   Press Enter for main menu...  ')
		os.system('cls')
	elif (choice == 0):
		typewriter("   ▄▄▄▄·  ▄· ▄▌▄▄▄ .      \n",0.01)
		typewriter("   ▐█ ▀█▪▐█▪██▌▀▄.▀·      \n",0.01)
		typewriter("   ▐█▀▀█▄▐█▌▐█▪▐▀▀▪▄      \n",0.01)
		typewriter("   ██▄▪▐█ ▐█▀·.▐█▄▄▌      \n",0.01)
		typewriter("   ·▀▀▀▀   ▀ •  ▀▀▀  ▀  ▀ \n",0.01)
	else:
		pass


