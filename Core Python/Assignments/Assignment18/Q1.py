# Create a class Complex Number with data members as real and imag and add
# following methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator

class ComplexNumber:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag
        print(f"Constructor: Created complex number {self.real} + {self.imag}i")

    def __del__(self):
        print(f"Destructor: Destroyed complex number {self.real} + {self.imag}i")

    # Overloading the + operator
    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    # Overloading the - operator
    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    # Helper method to print the object nicely
    def __str__(self):
        return f"{self.real} + {self.imag}i"

print("--- Testing Complex Number Class ---")
c1 = ComplexNumber(3, 5)
c2 = ComplexNumber(1, 2)
    
c_add = c1 + c2
print(f"Result of Addition: {c_add}")
    
c_sub = c1 - c2
print(f"Result of Subtraction: {c_sub}\n")