'''
MOBILE DATA ENTRY PROJECT USING __INIT__ CONSTRUCTOR
'''

'''
class mobiles():
    def __init__(self,mobile_name , mobile_ram,mobile_battery,mobile_price):
        self.a=mobile_name
        self.b=mobile_ram
        self.c=mobile_battery
        self.d=mobile_price
    def mobile_data(self):
        print("mobile name:",self.a)
        print("mobile ram:",self.b)
        print("mobile battery:",self.c)
        print("mobile price:",self.d)
mobile_obj=mobiles("apple","8gb","5000mah","30000")
mobile_obj.mobile_data()        
#OUTPUT IS
# mobile name: apple
# mobile ram: 8gb
# mobile battery: 5000mah
# mobile price: 30000
'''


#USING INPUT FUNCTION
class mobiles():
    def __init__(self,mobile_name , mobile_ram,mobile_battery,mobile_price):
        self.a=mobile_name
        self.b=mobile_ram
        self.c=mobile_battery
        self.d=mobile_price
        
    def mobile_data(self):
        print("mobile name:",self.a)
        print("mobile ram:",self.b)
        print("mobile battery:",self.c)
        print("mobile price:",self.d)
        
while True:
    name=input("enter the mobile name:")
    ram=input("enter the mobile ram:")     
    bat=input("enter the mobile battery:") 
    Price=float(input("enter the mobile price:"))
        
    mobile_obj=mobiles(name,ram,bat,Price)
    mobile_obj.mobile_data()               
     
           
                