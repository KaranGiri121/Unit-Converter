class Area:
	def ans(self,user_input,user_area):
		dict={'Square Decimeter':'sqrtdecimeter','Square Milimeter':'sqrtmilimeter','Square Centimeter':'sqrtcentimeter','Square Kilometer':'sqrtkilometer','Square Meter':'sqrtmeter'}
		if user_input in dict:
			user_input=dict[user_input]
		return getattr(self,user_input,lambda e : print('Valid Entry'))(user_area)
	def sqrtdecimeter(self,user_area):
		sqrtmeter=user_area/100
#		print(sqrtmeter)
		return sqrtmeter
	def sqrtcentimeter(self,user_area):
		sqrtmeter=user_area/10000
		return sqrtmeter
	def sqrtkilometer(self,user_area):
		sqrtmeter=user_area*1000000
		return sqrtmeter
	def sqrtmilimeter(self,user_area):
		sqrtmeter=user_area/1000000
		return sqrtmeter
	def are(self,user_area):
		sqrtmeter=user_area*100
		return sqrtmeter
	def hectare(self,user_area):
		sqrtmeter=user_area*10000
		return sqrtmeter
	def to_sqrtdecimeter(self,user_area):
		answer=user_area*100
		print('Hello World')
		return answer
	def to_sqrtcentimeter(self,user_area):
		answer=user_area*10000
		return answer
	def to_sqrtkilometer(self,user_area):
		answer=user_area/1000000
		return answer
	def to_sqrtmilimeter(self,user_area):
		answer=user_area*1000000
		return answer
	def to_are(self,user_area):
		answer=user_area/100
		return answer
	def to_hectare(self,user_area):
		answer=user_area/10000
		return answer
	def sqrtmeter(self,user_area):
		answer=user_area
		return answer
	def to_sqrtmeter(self,user_area):
		return user_area



