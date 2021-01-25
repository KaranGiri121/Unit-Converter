class area:
    def ans(self,user_input,user_area):
        getattr(self,user_input,lambda e : print('Valid Entry'))()
    def sqrtdecimeter(self,user_area):
        sqrtmeter=sqrtdecimeter/100
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
        return user_area*100
    def to_sqrtcentimeter(self,user_area):
        return user_area*10000
    def to_sqrtkilometer(self,user_area):
        return user_area/1000000
    def to_sqrtmilimeter(self,user_area):
        return user_area*1000000
    def to_are(self,user_area):
        return user_area/100
    def to_hectare(self,user_area):
        return user_area/10000
    def sqrtmeter(self,user_area):
        return user_area



