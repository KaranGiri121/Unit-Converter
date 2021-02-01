class Weigth:
    def ans(self,user_input,user_weigth):
        return getattr(self,user_input,lambda e : print("Enter Vaild Entry"))(user_weigth)
    def Gram(self,user_weigth):
        kg=user_weigth/1000
        return kg
    def Quintal(self,user_weigth):
        kg=user_weigth*100
        return kg
    def Carat(self,user_weigth):
        kg=user_weigth/5000
        return kg
    def Ton(self,user_weigth):
        kg=user_weigth*1000
        return kg
    def Miligram(self,user_weigth):
        kg=user_weigth/1000000
        return kg
    def Ounce(self,user_weigth):
        kg=user_weigth/35.2739619
        return kg
    def Pound(self,user_weigth):
        kg=user_weigth/2.2046226
        return kg
    def to_gram(self,user_weigth):
        answer=user_weigth*1000
        return answer
    def to_quintal(self,user_weigth):
        answer=user_weigth/100
        return answer
    def to_carat(self,user_weigth):
        answer=user_weigth*5000
        return answer
    def to_ton(self,user_weigth):
        answer=user_weigth/1000
        return answer
    def to_ounce(self,user_weigth):
        answer=user_weigth/0.028349523164848
        return answer
    def to_pound(self,user_weigth):
        answer=user_weigth/0.453592374495299
        return answer
    def Kilogram(self,user_weigth):
        return user_weigth
    def to_kilogram(self,user_weigth):
        return user_weigth
