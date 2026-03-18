class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel_level = 100

    def drive(self, distance):
        """Simulates driving and consuming fuel/energy."""
        self.fuel_level -= distance * 0.1
        return f"The {self.model} drove {distance} miles."

    def refuel(self):
        """Resets fuel level."""
        self.fuel_level = 100
        return f"{self.model} is now fully fueled."

    def __str__(self):
        return f"{self.year} {self.brand} {self.model} ({self.fuel_level}% fuel)"


class ElectricCar(Vehicle):
    def __init__(self, brand, model, year, battery_kwh):
        # Use super() to inherit base attributes
        super().__init__(brand, model, year)
        self.battery_kwh = battery_kwh

    def charge(self):
        self.fuel_level = 100
        return f"{self.model} is now 100% charged."

    # Overriding the __str__ method (Polymorphism)
    def __str__(self):
        return f"{self.year} {self.brand} {self.model} [EV] - {self.battery_kwh}kWh"


class Truck(Vehicle):
    def __init__(self, brand, model, year, max_payload):
        super().__init__(brand, model, year)
        self.max_payload = max_payload

    # Overriding the drive method (Polymorphism)
    def drive(self, distance):
        self.fuel_level -= distance * 0.3  # Trucks use more fuel!
        return f"The heavy-duty {self.model} hauled cargo for {distance} miles."

    def load_cargo(self):
        return f"Loading up to {self.max_payload} lbs into the {self.model}."