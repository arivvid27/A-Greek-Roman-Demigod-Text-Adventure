import replit
from replit import db
import sys
from time import sleep

roman_money = 0
greek_money = 0

db["Aureus"] = roman_money
db["Drachma"] = greek_money

roman_gods = ['Jupiter', 'Neptune', 'Minerva', 'Mars', 'Venus', 'Apollo', 'Vulcan', 'Mercury', 'Ceres', 'Bacchus']

greek_gods = ['Zeus', 'Athena', 'Apollo', 'Poseidon', 'Ares', 'Demeter', 'Aphrodite', 'Dionysos', 'Hermes', 'Hephaestus']

def text_effect(text):
	'''
	Creates an effect of natural typing
	'''
	for char in text:
		sleep(0.045)              
		print(char, end="")
		sys.stdout.flush()

def clear():
	'''
	Clears the terminal
	'''
	replit.clear()

text_effect('Hello! Welcome to the game! You will be givin a prompt to choose if you want to be a Greek demigod or a Roman Demigod. Here you go!')

Roman_or_Greek = input('Would you like play as a Roman, or Greek? > ')

if Roman_or_Greek.lower() == 'roman':
	demigod_name = input('What do you want your Roman demigod\'s name to be? > ')
	demigod_godly_parent = input('What god do you want to have as a godly parent? > ')
	sleep('2')
	text_effect(f'Okay, {demigod_name}, child of {demigod_godly_parent}.')
	sleep(2)
	text_effect('STARTING GAME')
	sleep(2)
	clear()
	text_effect(f'You have {roman_money} Aureus')
	text_effect('**What do you want to do?**')
	text_effect('1. Go to the armory')
	text_effect('2. Practice dueling - Can get you some Aureus')
	text_effect('3. Go on a mission - Can get you some Aureus')
	text_effect('------------------------------------------------')
	todo_choice = input()
	if todo_choice == '1':
		clear()
		text_effect('Welcome to the armory!')
		text_effect('Here are your choices of weapon:')
		text_effect('1. Imperial Gold Coin - A coin that can transfrom to a sword, javalin and a bow on your will - 0 Aureus ')
		text_effect('2. Infinite Arrows Quiver - Can produce an infinite amount of arrows - 5 Aureus')
		text_effect('3. Boomerang Blade - A sword that can be thrown and controled by the user. Always comes back. - 20 Aureus')
		text_effect('--------------------------------------------------------------')
		weapon_choice = input()
		if weapon_choice == '1':
			clear()
			text_effect('You got the Imperial Gold Coin!')
			text_effect('Adding to your inventory...')
			sleep(2)
			try:
				db['weapon'] = 'Imperial Gold Coin'
				text_effect('Success!')
			except Exception:
				text_effect('Oops. The game has crashed. Please run this again.')
				exit(120)
			