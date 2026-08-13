from abc import ABC, abstractmethod


class Vehicle(ABC):
    """Base class representing a rental vehicle."""

    def __init__(self, vehicle_number, brand, rental_price_per_day):
        self.vehicle_number = vehicle_number
        self.brand = brand
        self.rental_price_per_day = rental_price_per_day

    @abstractmethod
    def calculate_rental_amount(self, days):
        """Calculate rental amount based on vehicle type."""
        pass

    @abstractmethod
    def display_details(self):
        """Display vehicle information."""
        pass


class Car(Vehicle):
    """Car implementation."""

    def __init__(self, vehicle_number, brand, rental_price_per_day, seats):
        super().__init__(vehicle_number, brand, rental_price_per_day)
        self.seats = seats

    def calculate_rental_amount(self, days):
        amount = self.rental_price_per_day * days

        # 10% discount for rentals of 7 or more days
        if days >= 7:
            amount *= 0.90

        return amount

    def display_details(self):
        print("Vehicle Type   : Car")
        print("Vehicle Number : {}".format(self.vehicle_number))
        print("Brand          : {}".format(self.brand))
        print("Seats          : {}".format(self.seats))
        print("Price/Day      : ₹{}".format(self.rental_price_per_day))


class Bike(Vehicle):
    """Bike implementation."""

    def __init__(self, vehicle_number, brand, rental_price_per_day,
                 engine_capacity):
        super().__init__(vehicle_number, brand, rental_price_per_day)
        self.engine_capacity = engine_capacity

    def calculate_rental_amount(self, days):
        amount = self.rental_price_per_day * days

        # Additional charge for bikes above 500 CC
        if self.engine_capacity > 500:
            amount += 200 * days

        return amount

    def display_details(self):
        print("Vehicle Type   : Bike")
        print("Vehicle Number : {}".format(self.vehicle_number))
        print("Brand          : {}".format(self.brand))
        print("Engine Capacity: {} CC".format(self.engine_capacity))
        print("Price/Day      : ₹{}".format(self.rental_price_per_day))


class VehicleRentalSystem:
    """Manages available vehicles."""

    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def display_vehicles(self):
        for vehicle in self.vehicles:
            vehicle.display_details()
            print("-" * 40)

    def calculate_rental(self, vehicle_number, days):
        for vehicle in self.vehicles:
            if vehicle.vehicle_number == vehicle_number:
                return vehicle.calculate_rental_amount(days)

        return None


def main():
    rental_system = VehicleRentalSystem()

    # Add different types of vehicles
    rental_system.add_vehicle(
        Car("KA01AB1234", "Toyota", 2500, 5)
    )

    rental_system.add_vehicle(
        Car("KA02CD5678", "Honda", 3000, 7)
    )

    rental_system.add_vehicle(
        Bike("KA03EF9012", "Royal Enfield", 1200, 350)
    )

    rental_system.add_vehicle(
        Bike("KA04GH3456", "Kawasaki", 1800, 650)
    )

    # Display all vehicles
    print("AVAILABLE VEHICLES")
    print("=" * 40)
    rental_system.display_vehicles()

    # Calculate rental amounts
    rental_days = 5

    print("\nRENTAL CALCULATION")
    print("=" * 40)

    for vehicle in rental_system.vehicles:
        amount = rental_system.calculate_rental(
            vehicle.vehicle_number,
            rental_days
        )

        print("{} - {} days: ₹{}".format(
            vehicle.vehicle_number,
            rental_days,
            amount
        ))


if __name__ == "__main__":
    main()