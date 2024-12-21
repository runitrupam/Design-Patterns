"""
# 1. Factory Design Principle
The Factory Method is used to encapsulate the object creation process.
My goal is to create and return specific objects of Car, Bike, or Bycicle classes based on certain conditions.

Explanation
	1.	Encapsulation of Object Creation:
	b"	The VehicleFactory class contains the create_vehicle method, which encapsulates the logic for determining which object to create (Car, Bike, or Bycicle) based on the input parameters (no_of_wheels and has_engine).
	2.	Direct Return of Required Objects:
	b"	The factory method returns the correct class instance (Car, Bike, or Bycicle) without exposing the creation logic to the client code.
	3.	Benefits:
	b"	Encapsulation of object creation allows you to make changes to the creation logic without affecting client code.
"""
# 1. Factory Design Principle


class Bycicle:
    def __init__(self):
        self.wheels = 2
        self.has_engine = False

    def __str__(self):
        return "Bycicle: 2 wheels, no engine"


class Bike:
    def __init__(self):
        self.wheels = 2
        self.has_engine = True

    def __str__(self):
        return "Bike: 2 wheels, with engine"


class Car:
    def __init__(self):
        self.wheels = 4
        self.has_engine = True

    def __str__(self):
        return "Car: 4 wheels, with engine"


# Violates the Factory Design Principle
no_of_wheels = 4
has_engine = True
if no_of_wheels == 4 and has_engine == True:
    ob_car = Car()
else:
    ob_bike = Bike()


class VehicleFactory:
    @staticmethod  # used here as no class variable or instance is needed for the functionality.
    def create_vehicle(no_of_wheels, has_engine):
        if no_of_wheels == 4 and has_engine == True:
            return Car()
        elif no_of_wheels == 2 and has_engine == True:
            return Bike()
        elif no_of_wheels == 2 and has_engine == False:
            return Bycicle()
        else:
            raise ValueError("Invalid parameters for vehicle creation")


# Usage
vehicle1 = VehicleFactory.create_vehicle(4, True)
print(vehicle1)  # Output: Car: 4 wheels, with engine

vehicle2 = VehicleFactory.create_vehicle(2, False)
print(vehicle2)  # Output: Bycicle: 2 wheels, no engine

vehicle3 = VehicleFactory.create_vehicle(2, True)
print(vehicle3)  # Output: Bike: 2 wheels, with engine


"""
Conclusion
	b"	Use staticmethod if no subclassing or class-level data is involved.
	b"	Use classmethod if you anticipate extending the factory in the future or need class-level access.
	
	
class VehicleFactory:
    @staticmethod
    def create_vehicle(no_of_wheels, has_engine):
        if no_of_wheels == 4 and has_engine == True:
            return Car()
        elif no_of_wheels == 2 and has_engine == True:
            return Bike()
        elif no_of_wheels == 2 and has_engine == False:
            return Bycicle()
        else:
            raise ValueError("Invalid parameters for vehicle creation")
            
class AdvancedVehicleFactory(VehicleFactory):
    @classmethod
    def create_vehicle(cls, no_of_wheels, has_engine, color=None):
        # Add custom creation logic
        vehicle = super().create_vehicle(no_of_wheels, has_engine)
        if color:
            vehicle.color = color
        return vehicle            

You cannot use super() with a staticmethod because it is not bound to the class or the instance. 
Instead, you would need to explicitly call the parent classbs staticmethod:

"""


#####################

"""
#2. Builder Class :- for chaining the objects
like :- url builder , wardrobe build
"""


class UrlBuilder:
    

    def __init__(self):
        self.ip = None
        self.url = None
        self.header = None
        self.method = None
        pass

    def __str__(self):
        #(self.ip, self.url, self.header, self.method)
        return f'self.ip = {self.ip}, self.url = {self.url}, self.header = {self.header}, self.method = {self.method}'

    def add_ip(self, ip):
        self.ip = ip
        return self

    def add_url(self, url):
        self.url = url
        return self

    def add_header(self, header):
        self.header = header
        return self

    def add_method(self, method):
        self.method = method
        return self


ob1 = UrlBuilder()
# print(ob)
ob1.add_method('get').add_url('http://www.google.com')
print(ob1)


ob2 = UrlBuilder()
ob2.add_method('get').add_ip('192.11.1.1').add_url('http://www.google.com')
print(ob2)
print('\n\n')



"""
#3. Singleton Class :- for only 1 object
like :- db connection
"""
# METHOD 1:- Using a classmethod , _instance varible
class Singleton:
    _instance = None 
    
    def __init__(self):
        # Prevent multiple initialization if the instance already exists
        if Singleton._instance is not None:    
            raise Exception("Use get_instance method to create object")
        
        
    @classmethod
    def get_instance(cls):
        
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
# s3 = Singleton() # causes issues

s1 = Singleton.get_instance()
s2 = Singleton.get_instance()
# print(s3)

print(s1,'s1 is s2',s1 is s2)
print('\n\n')

# METHOD 2:- Using __new__ , _instance varible


class Singleton:
    _instance = None 
    
    def __new__(cls, *args, **kwargs):
        print('called 1st')
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
        
    
    def __init__(self,*args, **kwargs):
        print('called 2nd')
        pass
        

s1 = Singleton()
s2 = Singleton()
print(s1,'s1 is s2',s1 is s2)
print('\n\n')


s1 = 'abc'
s2 = 'abc'
print(f'{s1} == {s2}',s1 == s2)
print(f'{s1} is {s2}',s1 is s2)

print('\n\n')


s1 = [1,2,3]
s2 = [1,2,3]
print(f'{s1} == {s2}',s1 == s2)
print(f'{s1} is {s2}',s1 is s2)

print('\n\n')


'''
#4. Observer Design Pattern
To establish a one-to-many relationship between objects so that when one object (the “subject”) changes state, 
all its dependents (the “observers”) are notified automatically.
'''
    
class Subscriber:
    def __init__(self, name):
        self.name = name 
    
    def update(self, state):
        self.state = state
        print(f"The subject = {self.name} is updated with the state = {self.state}")
        
class NewsPublisher:
    def __init__(self):
        self.__subscribers = set() # __private , _protected, public 
        
    def attach(self, observer):
        self.__subscribers.add(observer)

    def detach(self, observer):
        self.__subscribers.remove(observer)
    
    def notify(self, state):
        # print(self.__subscribers)
        for obs in self.__subscribers:
            obs.update(state)


if __name__ == "__main__":
    news_ob = NewsPublisher() 
    ob1 = Subscriber('Hindustan')
    ob2 = Subscriber('TOI')

    news_ob.attach(ob1)
    news_ob.attach(ob2)
    news_ob.notify('State1')
    print('')
    news_ob.detach(ob1)
    news_ob.notify('State2')



print('\n\n')

'''
#5. The Adapter Design Pattern
The Adapter Design Pattern is used to bridge the gap between two incompatible interfaces, 
making them work together. It acts as a translator between a client and a service.
'''
  
class PlugInDevice:
    def __init__(self, name):
        self.name = name
        self.state = 'unplugged'
    
    def plug_in(self, power):
        self.state = 'plugged'
        print(f"Device = {self.name} is plugged in the power = {power}V")
        
    def plug_out(self, power = None):
        self.state = 'unplugged'
        print(f"Device = {self.name} is unplugged out of the power = {power}V")
    

from abc import ABC, abstractmethod

#Interface
class Socket(ABC):
    @abstractmethod
    def provide_power(self, power):
        pass
    
  
class SocketIndia(Socket):
    def __init__(self, name):
        self.name = name
        self.power = 110
    
    def provide_power(self):
        return self.power
    
    
class SocketAdapter():
    def __init__(self, us_socket):
        self.us_socket = us_socket

    def provide_power_to_india_socket(self):
        power = self.us_socket.provide_power()
        # Convert the power = 110V to 220V
        return power*2

if __name__ == "__main__":
    # US socket
    us_socket = SocketIndia('3-Pin Socket')
    
    #Adapter 
    adapter = SocketAdapter(us_socket)

    # India device
    tv_ob = PlugInDevice('Televison')

    tv_ob.plug_in(adapter.provide_power_to_india_socket())

'''

Output:-

Car: 4 wheels, with engine
Bycicle: 2 wheels, no engine
Bike: 2 wheels, with engine
self.ip = None, self.url = http://www.google.com, self.header = None, self.method = get
self.ip = 192.11.1.1, self.url = http://www.google.com, self.header = None, self.method = get



<__main__.Singleton object at 0x7bc95f20f6d0> s1 is s2 True



called 1st
called 2nd
called 1st
called 2nd
<__main__.Singleton object at 0x7bc95f20f640> s1 is s2 True



abc == abc True
abc is abc True



[1, 2, 3] == [1, 2, 3] True
[1, 2, 3] is [1, 2, 3] False



The subject = Hindustan is updated with the state = State1
The subject = TOI is updated with the state = State1

The subject = TOI is updated with the state = State2



Device = Televison is plugged in the power = 220V

'''
