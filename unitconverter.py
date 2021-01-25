import os
from length import Len
def menu():
#	os.system('clear')
	print('''Welcome To Unit Converter
	[1]Length
	[2]Area
	[3]Weigth
	[4]Temperture
	[5]Exit
Enter Your Choice: ''')
	try:
		user_menu=int(input())
		if(user_menu>5 or user_menu<1):
			raise Exception
	except Exception:
		print('Enter Valid Value')
		menu()
	if user_menu==1:
		user_menu_1()
	elif user_menu==5:
		quit()
def user_menu_1():
	while True:
		os.system('clear')
		print("Length Conversion :") 
		len_menu={1:'Decimeter',2:'Milimeter',3:'Centimeter',4:'Meter',5:'Kilometer'}
		for i in len_menu:
			print(f'[{i}]:{len_menu[i]}',end='\n')
		try :
			user_input=int(input('Enter The Unit Conversion From : ')) 
			user_length=int(input(f'{len_menu[user_input]}: '))
		except Exception:
			print("Enter Valid Number/Choice")
			user_menu_1()
		a=Len()
		meter=a.ans(len_menu[user_input],user_length)
		for i in len_menu:
			print(f'{i}:{len_menu[i]}',end='\n')
		user_input=int(input('Enter The Unit Conversion To : '))
		to_len_menu={1:'meter_to_dm',2:'meter_to_mm',3:'meter_to_cm',4:'meter_to_m',5:'meter_to_km'}
		answer=a.ans(to_len_menu[user_input],meter)
		print(f'{len_menu[user_input]}:{answer}')
		print('Press Any Key To Back To Menu Or',end='\n')
		user_input=input('Press Y For Unitconversion : ')
		if user_input!='y' and user_input!='Y':
			menu()






menu()

