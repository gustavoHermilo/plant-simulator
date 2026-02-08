import random
# Plant Simulator - Version 0.4

day= 1
health= 100
water = 50
nutrients= 50

while health>0:
    print("\n-----------------------------------")
    print("Day",day)

    weather= random.choice(["sun","snow","hail"])
    print("Weather today:",weather)

    if weather== "sun":
        water -= 10
        print("The sun dries the soil.Water -10")
    elif weather == "snow":
        health -= 15
        print("Snow damages the plant! Health -15")
    elif weather == "hail":
        health -= 25
        print("Hail is very harmful! Health -25")

    if water<0:
        water=0
    if nutrients<0:
        nutrients=0
    if health<0:
        health=0

    print("\n Current Plant Status")
    print("Health:",health)
    print("Water:",water)
    print("Nutrients:",nutrients)

    print("\nWhat do you want to do?")
    print("1.Water the plant (+20 water)")
    print("2.Add nutrients (+15 nutrients)")
    print("Do nothing")

    choice=input("Choose an option (1/2/3):")

    if choice=="1":
        water+=20
        print("You water the plant.Water +20")
    elif choice=="2":
        nutrients+=15
        print("You added nutrients.Nutrients +15")
    elif choice=="3":
        print("You did nothing today.")
    else: 
        print("Invalid choice.Nothing happened")
    
    day+=1
print("\n The plant has died")
print("You kept it alive for",day -1,"days.")
