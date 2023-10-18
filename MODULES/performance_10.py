"""
write a program that that creates four functions; addition, subtraction, multiplication, and division.
create another file and import the functions, use the functions to run
arithmetic problems

inside the second file, use the time module to calculate the performance time of all the functions
individually and all together

"""

import time

from four_funcs_2 import addition, subtraction, multiplication, division

def measure_performance(func, a, b):
    start_time = time.time()
    result = func(a, b)
    end_time = time.time()

    execution_time = end_time - start_time

    return result, execution_time

a = 10
b = 5

result_addition, time_addition = measure_performance(addition, a, b)

result_subtraction, time_subtraction = measure_performance(subtraction, a, b)

result_multiplication, time_multiplication = measure_performance(multiplication, a, b)

result_division, time_division = measure_performance(division, a, b)

start_time_all = time.time()

result_all = (
    addition(a, b),
    subtraction(a, b),
    multiplication(a, b),
    division(a, b)
)

end_time_all = time.time()
time_all = end_time_all - start_time_all


print(f"Addition Result: {result_addition}, Time: {time_addition} seconds")

print(f"Subtraction Result: {result_subtraction}, Time: {time_subtraction} seconds")

print(f"Multiplication Result: {result_multiplication}, Time: {time_multiplication} seconds")

print(f"Division Result: {result_division}, Time: {time_division} seconds")


print(f"All Operations Together Result: {result_all}, Time: {time_all} seconds")