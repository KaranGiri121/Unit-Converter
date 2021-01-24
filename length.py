class Len:
	def ans(self,num,user_input):
		answer='Flase'
		return getattr(self,num,lambda:answer)(user_input)
	def Decimeter(self,user_input):
		meter=float(user_input)/10
		return meter
	def Milimeter(self,user_input):
		meter=float(user_input)/1000
		return meter
	def Centimeter(self,user_input):
		meter=float(user_input)/100
		return meter
	def Kilometer(self,user_input):
		meter=float(user_input)*1000
		return meter
	def Meter(self,user_input):
		return user_input
	def meter_to_dm(self,user_input):
		dm=float(user_input)*10
		return dm
	def meter_to_mm(self,user_imput):
		mm=float(user_input)*1000
		return mm
	def meter_to_km(self,user_input):
		km=float(user_input)/1000
		return km
	def meter_to_cm(self,user_input):
		cm=float(user_input)*100
		return cm
	def meter_to_m(self,user_input):
		return user_input
