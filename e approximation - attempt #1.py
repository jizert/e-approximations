# This is the first script I have made completely by myself, without a tutorial, and from an original idea.

import math


accuracy  = int(input("What level of accuracy would you like your approximation?: "))
e = math.e 

def sum_e_accuracy(n):
    return sum(1 / math.factorial(i) for i in range(n+1))
    
approximation = sum_e_accuracy(accuracy)
margin_of_error = e - approximation
print("The margin of error is: " + str(margin_of_error))
