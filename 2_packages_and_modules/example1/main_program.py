# main_program.py

from my_module import square, cube
from my_package import module1, module2

if __name__ == "__main__":

    print("Square:", square(4))
    print("Cube:", cube(3))

    print("Addition:", module1.add(5, 3))
    print("Subtraction:", module1.subtract(8, 2))
    print("Multiplication:", module2.multiply(4, 6))
    print("Division:", module2.divide(9, 3))
