import random
# Plant Simulator - Version 0.3

day= 1
health= 100
water = 50
nutrients= 50

print("Welcome to the Plant Care Simulator")
print("-----------------------------------")
print("Day",day)

weather= random.choice(["sun","snow","hail"])
print("Weather today:",weather)

if weather== "sun":
    water -= 10
    print("The sun dries the soil.Water -10")
elif weather == "snow":
    health -= 15
    print("Hail is very harmful! Health -15")
elif weather == "hail":
    health -= 25
    print("Hail is very harmful! Health -25")

print("\n Plant Status at the end of the day")
print("Health:",health)
print("Water:",water)
print("Nutrients:",nutrients)
