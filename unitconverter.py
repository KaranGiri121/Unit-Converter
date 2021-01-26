import os
from length import Len
from area import Area
from weigth import Weigth
def menu():
	dict={1:Lenconversion,2:Areaconversion,3:Weigthconversion}
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
	dict.get(user_menu,default)()

def Lenconversion():
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
			print('Enter Valid Entry')
			Lenconversion()
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
def Areaconversion():
	while True:
		os.system('clear')
		print('Area Conversion')
		area_menu={1:'Square Decimeter',
			2:'Square Milimeter',
			3:'Square Centimeter',
			4:'Square Meter',
			5:'Square Kilometer',
			6:'Are',
			7:'Hectare'}
		for i in area_menu:
			print(f'{i}:{area_menu[i]}')
		try:
			user_input=int(input("Enter Unit Conversion From :"))
			user_area=int(input(f'{area_menu[user_input]}: '))
		except Exception:
			print("Enter Valid Entry")
			Areaconversion()
		a=Area()
		sqrtmeter=a.ans(area_menu[user_input],user_area)
		for i in area_menu:
			print(f'{i}:{area_menu[i]} ')
		user_input=int(input('Enter Unit Coversion To : '))
		to_area={1:'to_sqrtdecimeter',2:'to_sqrtmilimeter',3:'to_sqrtcentimeter',4:'to_sqrtmeter',
			5:'to_sqrtkilometer',6:'to_are',7:'to_hectare'}
		answer=a.ans(to_area[user_input],sqrtmeter)
		print(f'{area_menu[user_input]}:{answer}')
		print('Press Any Key To Back To Menu Or',end='\n')
		user_input=input('Press Y For Unitconversion : ')
		if user_input!='y' and user_input!='Y':
			menu()

def Weigthconversion():
	while True:
		os.system('clear')
		print('Weigth Conversion')
		weigth_menu={1:'Gram',
			2:'Quintal',
			3:'Carat',
			4:'Ton',
			5:'Kilogram',
			6:'Ounce',
			7:'Pound'}
		for i in weigth_menu:
			print(f'{i}:{weigth_menu[i]}')
		try:
			user_input=int(input("Enter Unit Conversion From :"))
			user_weigth=int(input(f'{weigth_menu[user_input]}: '))
		except Exception:
			print("Enter Valid Entry")
			Weigthconversion()
		a=Weigth()
		kilogram=a.ans(weigth_menu[user_input],user_weigth)
		for i in weigth_menu:
			print(f'{i}:{weigth_menu[i]} ')
		user_input=int(input('Enter Unit Coversion To : '))
		to_weigth={1:'to_gram',2:'to_quintal',3:'to_carat',4:'to_ton',
			5:'to_kilogram',6:'to_ounce',7:'to_pound'}
		answer=a.ans(to_weigth[user_input],kilogram)
		print(f'{weigth_menu[user_input]}: {answer}')
		print('Press Any Key To Back To Menu Or',end='\n')
		user_input=input('Press Y For Unitconversion : ')
		if user_input!='y' and user_input!='Y':
			menu()
def default():
	quit()





menu()

