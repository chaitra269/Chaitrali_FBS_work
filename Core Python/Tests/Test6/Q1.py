# Write a program which calculates toll calculation on some location following is data provided:
# Many vehicles goes through the toll every vehicle has to pay the basic toll + extra charges if any.
# two wheelers have to pay basic toll Rs 20 three wheelers have to pay 30 and four wheelers have to pay 40
# heavy veheicles i.e. Vehicles having wheels more than four, have to pay 60 Rs as basic toll
# extra charges :for two wheelers if no. of persons are more than two extra charge
# =10/person for three wheelers if no. of persons are more than 3 extra charge
# =20/person for four wheelers if no. of persons are more than 4 extra charge
# =40/person for heavy vehicle if no. of person are more than 6 extra charges
# =100/person.Show polymorphic behaviour in main. Main module should be
# designed in such way that toll should easily operate it through interactive menu driven program .
# Object of vehicle class should not be possible.

from abc import ABC, abstractmethod

class Vehicle(ABC):
    """Abstract Base Class for all vehicles. Direct object creation is disabled."""
    
    def __init__(self, vehicle_id, extra_passengers=0):
        self.vehicle_id = vehicle_id
        self.extra_passengers = max(0, extra_passengers)

    @abstractmethod
    def calculate_toll(self):
        """Polymorphic method to calculate toll."""
        pass

class TwoWheeler(Vehicle):
    def __init__(self, vehicle_id, persons):
        # Base capacity is 2 persons
        extra = persons - 2
        super().__init__(vehicle_id, extra)
        self.basic_toll = 20
        self.extra_rate = 10

    def calculate_toll(self):
        return self.basic_toll + (self.extra_passengers * self.extra_rate)

class ThreeWheeler(Vehicle):
    def __init__(self, vehicle_id, persons):
        # Base capacity is 3 persons
        extra = persons - 3
        super().__init__(vehicle_id, extra)
        self.basic_toll = 30
        self.extra_rate = 20

    def calculate_toll(self):
        return self.basic_toll + (self.extra_passengers * self.extra_rate)

class FourWheeler(Vehicle):
    def __init__(self, vehicle_id, persons):
        # Base capacity is 4 persons
        extra = persons - 4
        super().__init__(vehicle_id, extra)
        self.basic_toll = 40
        self.extra_rate = 40

    def calculate_toll(self):
        return self.basic_toll + (self.extra_passengers * self.extra_rate)

class HeavyVehicle(Vehicle):
    def __init__(self, vehicle_id, persons):
        # Base capacity is 6 persons
        extra = persons - 6
        super().__init__(vehicle_id, extra)
        self.basic_toll = 60
        self.extra_rate = 100

    def calculate_toll(self):
        return self.basic_toll + (self.extra_passengers * self.extra_rate)


def main():
    vehicles_processed = []

    while True:
        print("\n--- TOLL OPERATOR MENU ---")
        print("1. Process Two Wheeler")
        print("2. Process Three Wheeler")
        print("3. Process Four Wheeler")
        print("4. Process Heavy Vehicle")
        print("5. View Summary & Exit")
        
        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if choice == 5:
            print("\n=== Daily Toll Summary ===")
            if not vehicles_processed:
                print("No vehicles processed today.")
            else:
                total_collection = 0
                for v in vehicles_processed:
                    # Polymorphic behavior: Call to calculate_toll resolves at runtime
                    toll = v.calculate_toll()
                    total_collection += toll
                    print(f"Vehicle Type: {v.__class__.__name__:<15} | ID: {v.vehicle_id:<10} | Toll: Rs {toll}")
                print("-" * 50)
                print(f"Total Grand Collection: Rs {total_collection}")
            print("Exiting Toll System. Goodbye!")
            break

        # Fixed the missing list here
        if choice in[]:
            v_id = input("Enter Vehicle Registration Number: ").strip().upper()
            try:
                persons = int(input("Enter total number of persons inside the vehicle: "))
                if persons <= 0:
                    print("Number of persons must be greater than 0.")
                    continue
            except ValueError:
                print("Invalid input for persons. Please enter a valid integer.")
                continue

            vehicle_obj = None

            # Creating specific subclass objects based on selection
            if choice == 1:
                vehicle_obj = TwoWheeler(v_id, persons)
            elif choice == 2:
                vehicle_obj = ThreeWheeler(v_id, persons)
            elif choice == 3:
                vehicle_obj = FourWheeler(v_id, persons)
            elif choice == 4:
                vehicle_obj = HeavyVehicle(v_id, persons)

            if vehicle_obj:
                vehicles_processed.append(vehicle_obj)
                print(f"Success: Toll calculated for {v_id} -> Rs {vehicle_obj.calculate_toll()}")
        else:
            print("Invalid choice. Please select from options 1 to 5.")

if __name__ == "__main__":
    main()
