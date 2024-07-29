# This is the first script I have made completely by myself, without a tutorial, and from an original idea.

import math


accuracy  = int(input("What level of accuracy would you like your approximation?: "))
e = math.e 

def sum_e_accuracy(n):
    sum(i/math.factorial(n) for i in range(n))
    

margin_of_error = e - sum_e_accuracy(accuracy)
print("The margin of error is: " + str(margin_of_error))
