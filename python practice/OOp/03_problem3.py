class TemperaturConverter:
    def farh(self,number):
        return number*33.8
    def celc(self,number):
        return number/33.8
temp=TemperaturConverter()
num=int(input("Enter a number:"))
print(f"the fahrenheit value of {num} is {temp.farh(num)}")
print(f"the celcius value of {num} is {temp.celc(num)}")