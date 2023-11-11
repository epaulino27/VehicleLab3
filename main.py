class Vehicle:
    def __init__(self,make,model,year,weight): #assign attributes
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
    def __str__(self,make,model,year,weight): #displays info.
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Weight: {self.weight}")
    def __repr__(self):
        return print(f"Vehicle({self.make!r}, {self.model!r}, {self.year!r}, {self.weight!r})")
    def honk(self):#print a honk sound
        return "Beep!Beep!"
    def display_vin(self):
        print("VIN: 1234567889")

class Car(Vehicle): #make class Vehicles
    def __init__(self, make, model, year, weight, num_doors):
        super().__init__(make,model,year,weight)
        self.num_doors = num_doors
    def __str__(self):#print out vehicles details neatly
        super().__str__(self.make, self.model, self.year, self.weight)
        return print(f"Number of Doors: {self.num_doors}")

    def __repr__(self):
        return print(f"Car({self.make!r}, {self.model!r}, {self.year!r}, {self.weight!r}, {self.num_doors!r})")
    def honk(self):#print a honk sound
        return "Beep!Beep!"

class Boat(Vehicle):
    def __init__(self,make,model,year,weight,boat_type): #assign attributes
        super().__init__(make, model, year, weight)
        self.boat_type = boat_type
    def __str__(self):#print out vehicles details neatly
        super().__str__(self.make, self.model, self.year, self.weight)
        return print(f"Boat Type: {self.boat_type}")

    def __repr__(self):
        return print(f"Boat({self.make!r}, {self.model!r}, {self.year!r}, {self.weight!r}, {self.boat_type!r})")
    def honk(self):#print a honk sound
        return "BWORRRRRRNK"

class Truck(Vehicle): #make class Vehicles
    def __init__(self,make,model,year,weight,num_doors,payload_capacity): #assign attributes
        super().__init__(make, model, year, weight)
        self.num_doors = num_doors
        self.payload_capacity = payload_capacity
    def __str__(self):#print out vehicles details neatly
        super().__str__(self.make, self.model, self.year, self.weight)
        return print(f"Make: {self.make}"), print(f"Model: {self.model}"), print(f"Year: {self.year}"), print(f"Weight: {self.weight}"), print(f"Number of Doors: {self.num_doors}"), print(f"Payload Capacity: {self.payload_capacity}")

    def __repr__(self):
        return print(f"Truck({self.make!r}, {self.model!r}, {self.year!r}, {self.weight!r}, {self.num_doors!r})")
    def honk(self):#print a honk sound
        return "Hoonk!"
    def dump_load(self):#print a dumping sound
        print("Clunk!Boom!")

# Test driver code
def main():
    # Create instances of Car
    # Create instances of Vehicle, Car, Truck, and Boat
    vehicle = Vehicle("Generic", "Transport", 2020, 1000)
    car = Car("Ford", "Mustang", 1964, 1500, 2)
    truck = Truck("Dodge", "Ram", 2010, 5000, 2000,250)  # Payload capacity in pounds
    boat = Boat("Yamaha", "242 Limited S", 2018, 3600, 24)  # Length in feet

    #vehicle.__str__()
    print("Car String Representation:")
    car.__str__()
    print()
    print("Truck String Representation:")
    truck.__str__()
    print()
    print("Boat String Representation:")
    boat.__str__()
    print()

    print("\nUnambiguous Representations:")
    # Print the __repr__ representation
    car.__repr__()
    truck.__repr__()
    boat.__repr__()
    print()

    # Demonstrating the honk method
    print("\nVehicle Sounds:")
    #print(f"{vehicle.make} Vehicle: {vehicle.honk()}")
    print(f"The {car.make}(Car) makes a {car.honk()} sound.")
    print(f"The {truck.make}(Truck) makes a {truck.honk()} sound.")
    print(f"The {boat.make}(Boat) makes a {boat.honk()} sound.")

if __name__ == "__main__":
    main()