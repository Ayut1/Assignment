traffic_light = "Green"
speed= 60

class Vehicle:
    def start_engine(self):
        message = "Engine started"
        print(message)

class Car(Vehicle):
    def __init__(self, make):
        self.make = make  

    def start_engine(self):
        message = "Car engine started" 
        print(message)

class Bike(Vehicle):
    def __init__(self, bike_type):
        self.type = bike_type 

    def start_engine(self):
        message = "Bike engine started"
        print(message)
if __name__ == "__main__":
    print(f"Global variable traffic_light: {traffic_light}")
    print(f"Module-level variable speed: {speed}")

    
    my_car = Car("Toyota")
    my_bike = Bike("Mountain")

    
    my_car.start_engine()
    my_bike.start_engine()

    
    print(f"Car make: {my_car.make}")
    print(f"Bike type: {my_bike.type}")

