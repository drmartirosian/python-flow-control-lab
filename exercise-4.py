# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a:
#      b:
#      c:
print("Enter the length of three sides of a triangle: ")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))


# 2. Write the code that determines if the triangle is:
#      equilateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length

if a == b and a == c:
    tri = ("EQUILATERAL")

elif a != b and a != c and b != c:
    tri = ("SCALENE")

else:
    tri = ("ISOSCELES")


# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

print(f"Triangle with {a}, {b}, {c} is a {tri}")