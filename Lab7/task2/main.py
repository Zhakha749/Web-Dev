from models import Vehicle, ElectricCar, Truck

def main():
    # Instantiate objects
    my_car = Vehicle("Toyota", "Camry", 2022)
    my_tesla = ElectricCar("Tesla", "Model 3", 2024, 75)
    my_ford = Truck("Ford", "F-150", 2023, 2000)

    # Store objects in a list
    fleet = [my_car, my_tesla, my_ford]

    print("--- Current Fleet Status ---")
    for vehicle in fleet:
        print(vehicle)

    print("\n--- Testing Polymorphism & Methods ---")
    for vehicle in fleet:
        # Every vehicle has a drive method, but they behave differently!
        print(vehicle.drive(50))
        
    print(f"\nSpecific Method: {my_tesla.charge()}")
    print(f"Specific Method: {my_ford.load_cargo()}")

if __name__ == "__main__":
    main()