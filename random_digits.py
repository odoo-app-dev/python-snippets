from random import choice
from string import digits
my_random_digits = "".join(choice(digits) for i in range(9))
