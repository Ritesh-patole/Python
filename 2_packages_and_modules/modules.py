'''
modules :

1. math and cmath
2. Decimal Module
3. Fractions Module
4. Satistics Module
5. Time Module
6. Datetime Module
7. Calender
8. sys module

'''

import math
import cmath
from decimal import Decimal
from fractions import Fraction
import statistics
import time
from datetime import datetime
import calendar
import sys

# 1. Math and cmath
print("Math and cmath:")
print(math.sqrt(25))  # Square root
print(math.sin(math.radians(30)))  # Sine of 30 degrees

complex_num = cmath.sqrt(-1)
print(complex_num)

# 2. Decimal Module
print("\nDecimal Module:")
decimal_num = Decimal('3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862')
print(decimal_num)

# 3. Fractions Module
print("\nFractions Module:")
fraction1 = Fraction(1, 3)
fraction2 = Fraction(2, 5)
result = fraction1 + fraction2
print(result)

# 4. Statistics Module
print("\nStatistics Module:")
data = [1, 2, 3, 4, 5]
mean_value = statistics.mean(data)
print(mean_value)

# 5. Time Module
print("\nTime Module:")
current_time = time.time()
print(current_time)

# 6. Datetime Module
print("\nDatetime Module:")
current_datetime = datetime.now()
print(current_datetime)

# 7. Calendar Module
print("\nCalendar Module:")
cal = calendar.month(2024, 2)
print(cal)

# 8. Sys Module
print("\nSys Module:")
print(sys.version)  # Python version
print(sys.platform)  # Operating system platform
