#Task 1
import datetime

class Patient:
    class PatientError(Exception):
         pass
    def __init__(self, name:str, surname:str, age:int, gender:str):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender
        try:
            if isinstance(name, str):
                self.name = name
            else: raise self.PatientError("Name should be string.")

            if isinstance(surname, str):
                self.surname = surname
            else: raise self.PatientError("Surname should be string")  

            if isinstance(age, int):
                if self.age in range(18, 100):
                    self.age = age
                else: raise self.PatientError("Age should be between 18-100.")

            if isinstance(gender, str):
                if self.gender == "M" or self.gender == "F":
                    self.gender = gender
                else: raise self.PatientError("Gender should be Male or Female")

        except Exception as e:
            print(e)

    def __repr__(self):
        return f"Patient: {self.name}, {self.surname},  {self.age}, {self.gender}"
    
    def __ne__(self, other):
        if self.name == other.name and self.surname == other.surname and self.age == other.age and self.gender == other.gender:
            return True
        else: return False
    
a= Patient("John", "Smith", 19, "M")
b = Patient("Mary", "Jane", 12, "F")
print(a)
print(b)

class Doctor:
    def __init__(self, name:str, surname:str, schedule:dict):
        self.name = name
        self.surname = surname
        self.schedule = schedule

    def __repr__(self):
        return f" {self.name}, {self.surname},  {self.schedule}"
    

    def is_free(self, date, time):
        if date in self.schedule:
            start_time = 9
            end_time = start_time + 8
            for t in range(start_time, end_time, 30):
                if time == t and self.schedule[date].get(t) is not None:
                    return "This time is busy"
        return "This time is free"
    
    def is_registered(self, patient):
        for date in self.schedule:
            for time in self.schedule[date]:
                if self.schedule[date][time] == patient:
                    return f"{patient} is registered"
        return f"{patient} is not registered yet"
    
    def register_patient(self, date, time, patient):
            if self.is_registered(patient) == True:
                raise Exception("you are already registered")
            elif self.is_free(date, time):
                if date not in self.schedule:
                    self.schedule[date] = {}
                self.schedule[date][time] = patient
                return f" {patient} successfully registered at {datetime}"
            return f"Datetime {datetime} is already taken by another patient"
        
p1 = Patient("John", "Doe", 30, "M")
p2 = Patient("Jane", "Doe", 25, "F")
p3 = Patient("Bob", "Smith", 40, "M")
d1 = Doctor("Dr.", "Smith", {})
print(d1.is_free("2023-03-05", 8))
d1.register_patient("2023-03-05", 8, p1)
print(d1.is_registered(p1))
print(d1.is_registered(p2)) 
d1.register_patient("2023-12-05", 10, p2)
print(d1.is_registered(p2))



#Task 2

class Product:
    def __init__(self, price : int, id : int, quantity : int):
        self.price = price
        self.id = id
        self.quantity = quantity
    
    def __repr__(self):
        return f" {self.price}, {self.id},  {self.quantity}"
    
    
    def buy(self, quantity_to_buy):
        if self.quantity >= quantity_to_buy:
            self.quantity -= quantity_to_buy
            return "Purchase succesfully"
        else: raise Exception("Not enogh products")


class Inverntory(Product):
    def __init__ (self):
        self.list = []

    def __repr__(self):
        return f" {self.list}"
    
    def add_product(self, product):
        self.list.append(product)

    def sum_of_products(self):
        sum = 0
        for item in self.list:
            sum += item.quantity
            return sum   
        
    def get_by_id(self, product_id):
        for product in self.list:
            if product.id == product_id:
                return product
        return "This product is not in our list"
    

p1 = Product(100, 20, 10)
p2 = Product(500, 1245, 25 )
i1 = Inverntory()
i1.add_product(p1)
i1.add_product(p2)
print("The details of the product with this id is:", i1.get_by_id(20))
print(p1.buy(3))
print(p1.buy(2))

        
#Task 3   
class Passenger:
    def __init__(self,name, city, rooms):
        self.name = name
        self.city = city
        self.rooms = rooms

    def __repr__(self):
        return f" {self.name}, {self.city}, {self.rooms}"
    
    def get_name(self):
        return self.name
    
    def get_city(self):
        return self.city
    
    def get_rooms(self):
        return self.rooms
    
class Hotel:
    def __init__(self, city, rooms):
        self.city = city
        self.rooms = rooms

    def __repr__(self) -> str:
        return f"{self.city}, {self.rooms}"
    
    def get_city(self):
        return self.city
    
    def free_rooms_list(self):
        return [room for room, count in self.rooms.items() if count > 0]

    def reserve_rooms(self, room_type, count):
        if room_type in self.rooms and self.rooms[room_type] >= count:
            self.rooms[room_type] -= count
            return True
        return False
    
def book(hotel, passenger, room_type, count):
    result = hotel.reserve_rooms(room_type, count)
    if result:
        print("Reservation successful")
        passenger.rooms[room_type] = count
    else:
        print("Reservation failed: not enough rooms")

p = Passenger("John Doe", "New York", {"single": 2, "double": 1})
print("Passenger name:", p.name)
print("Passenger city:", p.city)
h = Hotel("New York", {"single": 5, "double": 2})
print("Hotel city:", h.get_city())
print("Free rooms:", h.free_rooms_list())
book(h,p, "double", 2)
book(h,p,"doble", 1)
book(h,p,"single", 4)
print(p.rooms)



    


        



        
    
