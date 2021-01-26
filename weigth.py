class Weigth:
    def ans(self,user_input,user_weigth):
        return getattr(self,user_input,lambda e : print("Enter Vaild Entry"))(user_weigth)
    def Gram(self,user_area):
        kg=user_area/1000
        return kg
    def Quintal(self,user_area):
        kg=user_area*100
        return kg
    def Carat(self,user_area):
        kg=user_area/5000
        return kg
    def Ton(self,user_area):
        kg=user_area*1000
        return kg
    def Miligram(self,user_area):
        kg=user_area/1000000
        return kg
    def Ounce(self,user_area):
        kg=user_area/35.2739619
        return kg
    def Pound(self,user_area):
        kg=user_area/2.2046226
        return kg
    def to_gram(self,user_area):
        answer=user_area*1000
        return answer
    def to_quintal(self,user_area):
        answer=user_area/100
        return answer
    def to_carat(self,user_area):
        answer=user_area*5000
        return answer
    def to_ton(self,user_area):
        answer=user_area/1000
        return answer
    def to_ounce(self,user_area):
        answer=user_area/0.028349523164848
        return answer
    def to_pound(self,user_area):
        answer=user_area/0.453592374495299
        return answer
    def Kilogram(self,user_area):
        return user_area
    def to_kilogram(self,user_area):
        return user_area
