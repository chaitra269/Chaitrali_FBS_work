# 2. Create class television that has members to hold the model number ,screen size
# and price. Take a member function to take input from user, If more than 4 digits
# are entered for model number, if screen size is smaller than 12 inches or greater
# than 70 inches or if the price is negative or greater than 5000 Rs, then throw an
# exception.
# Write a main() that instantiates an object and allows the user to enter and display
# data. If exception is caught, replace all data member values with zero

class TelevisionException(Exception):
    pass

class Television:
    def __init__(self):
        self.model_number = 0
        self.screen_size = 0
        self.price = 0

    def take_input(self):
        try:
            # Collect data from user
            model_str = input("Enter model number (max 4 digits): ").strip()
            size = float(input("Enter screen size (12 to 70 inches): "))
            price = float(input("Enter price (0 to 5000 Rs): "))

            # Validation 1: Model number length
            if not model_str.isdigit() or len(model_str) > 4:
                raise TelevisionException("Model number must be a valid integer up to 4 digits.")
            
            # Validation 2: Screen size
            if size < 12 or size > 70:
                raise TelevisionException("Screen size must be between 12 and 70 inches.")
            
            # Validation 3: Price
            if price < 0 or price > 5000:
                raise TelevisionException("Price must be between 0 and 5000 Rs.")

            # If all validations pass, assign values
            self.model_number = int(model_str)
            self.screen_size = size
            self.price = price

        except ValueError:
            # Handles non-numeric inputs for size and price during inputs
            raise TelevisionException("Invalid data type entered. Expected numeric values.")

    def display(self):
        print("\n--- Television Details ---")
        print(f"Model Number: {self.model_number}")
        print(f"Screen Size : {self.screen_size} inches")
        print(f"Price       : {self.price} Rs")


def main():
    tv = Television()
    try:
        tv.take_input()
    except TelevisionException as e:
        print(f"\n[Exception Caught]: {e}")
        print("Resetting all television data members to 0.")
        # Resetting values due to exception
        tv.model_number = 0
        tv.screen_size = 0
        tv.price = 0
    finally:
        # Always display the final state of the object
        tv.display()

if __name__ == "__main__":
    main()
