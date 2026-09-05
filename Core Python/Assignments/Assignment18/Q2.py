# Create a class Distance with data members as km,m and cm and add following
# methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator

class Distance:
    def __init__(self, km=0, m=0, cm=0):
        self.km = km
        self.m = m
        self.cm = cm
        self._normalize()
        print(f"Constructor: Created distance {self.km}km {self.m}m {self.cm}cm")

    def __del__(self):
        print(f"Destructor: Destroyed distance {self.km}km {self.m}m {self.cm}cm")

    def _normalize(self):
        if self.cm >= 100:
            self.m += self.cm // 100
            self.cm %= 100
        if self.m >= 1000:
            self.km += self.m // 1000
            self.m %= 1000

    # Convert everything to total centimeters for easy subtraction/math
    def _to_cm(self):
        return (self.km * 100000) + (self.m * 100) + self.cm

    @staticmethod
    def _from_cm(total_cm):
        # Handle negative distances by setting them to 0 or keeping them representationally
        sign = 1 if total_cm >= 0 else -1
        total_cm = abs(total_cm)
        
        km = total_cm // 100000
        total_cm %= 100000
        m = total_cm // 100
        cm = total_cm % 100
        return Distance(sign * km, sign * m, sign * cm)

    # Overloading the + operator
    def __add__(self, other):
        total_cm = self._to_cm() + other._to_cm()
        return Distance._from_cm(total_cm)

    # Overloading the - operator
    def __sub__(self, other):
        total_cm = self._to_cm() - other._to_cm()
        return Distance._from_cm(total_cm)

    # Helper method to print the object nicely
    def __str__(self):
        return f"{self.km}km {self.m}m {self.cm}cm"

print("--- Testing Distance Class ---")
d1 = Distance(2, 800, 70)
d2 = Distance(1, 400, 50)
    
d_add = d1 + d2
print(f"Result of Addition: {d_add}")
    
d_sub = d1 - d2
print(f"Result of Subtraction: {d_sub}\n")
    
print("--- Cleaning up objects (Triggering Destructors) ---")
