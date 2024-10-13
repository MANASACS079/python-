#Create a class Complex number with attributes real and complex. Define two methods- one to print the complex number in the form a+ib and the other method to find the conjugate of a complex number
class complex_num():
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary
    def print_complex(self):
        if self.imaginary >= 0:
            print(f"{self.real} + {self.imaginary}i")
        else:
            print(f"{self.real} - {-self.imaginary}i")
    def conjugate(self):
        return complex_num(self.real, -self.imaginary)
num = complex_num(6, 5)
num.print_complex()  
conjugate_num = num.conjugate()
conjugate_num.print_complex()  
    