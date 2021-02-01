class Temperature:
    def ans(self,user_input,user_temp):
        return getattr(self,user_input,lambda e:print('Enter Valid Entry'))(user_temp)
    def Fahrenheit(self,user_temp):
        celsius=user_temp-32
        celsius*=5
        celsius/=9
        return celsius
    def Kelvin(self,user_temp):
        celsius=user_temp-273.15
        return celsius
    def to_f(self,user_temp):
        answer=user_temp*9
        answer/=5
        answer+=32
        return answer
    def to_kelvin(self,user_input):
        answer=user_input+273.15
        return answer
    def Celsius(self,user_temp):
        return user_temp
    def to_c(self,user_temp):
        return user_temp
