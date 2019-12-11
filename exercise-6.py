# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the season (Jan - Dec):
month = input("Enter the month of the season (Jan - Dec): ")


# 2. Then propts the user to enter the day of the month:
#      Enter the day of the month:
day = int(input("Enter the day of the month 1-31: "))


# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall

#WINTER
if month in ('Dec') and day >= 21 or month in ('Jan', 'Feb') or month in ('Mar') and day <= 19:
    season = 'Winter'
#SPRING
elif month in ('Mar') and day >= 20 or month in ('Apr', 'May') or month in ('Jun') and day <= 20:
    season = 'Spring'
#SUMMER
elif month in ('Jun') and day >= 21 or month in ('July', 'Aug') or month in ('Sep') and day <= 21:
    season = 'Summer'
#FALL
elif month in ('Sep') and day >= 22 or month in ('Oct', 'Nov') or month in ('Dec') and day <= 20:
    season = 'Fall'
else:
    print('INVALID INPUTS')



# 4. Print the result as follows:
#      <Mmm> <dd> is in <season>
print(f'{month} {day} is in {season}')

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.