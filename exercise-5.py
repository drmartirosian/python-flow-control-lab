# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.
# Hint: The next number is found by adding the two numbers before it


#f(c) = f(c-1) + f(c-2)
num_terms = int(input("How many terms? "))
a = 0
b = 1
count = 0
if num_terms == 1:
   print(f"term: {count} / number: {a}")
else:
   while count < num_terms:
       print(f"term: {count+1} / number: {a}")
       c = a + b
       a = b
       b = c
       count += 1