import random
# Plant Simulator - Version 0.5
class Plant:
    def __init__(self):
        self.health=100
        self.water=50
        self.nutrients=50
        self.protected=False  #greenhouse / cover active
    def status(self):
        print("\n Current Plant Status")
        print("Health:",self.health)
        print("Water:",self.water)
        print("Nutrients:",self.nutrients)
        print("Protected:",self.protected)
plant=Plant()
day= 1

while plant.health>0:
    print("\n-----------------------------------")
    print("Day",day)

    weather= random.choice(["sun","snow","hail"])
    print("Weather today:",weather)

    #Weather effects
    if weather== "sun":
        plant.water -= 10
        print("The sun dries the soil.Water -10")
    elif weather == "snow":
        if plant.protected:
            plant.health -= 5
            print("Snow is blocked by protection.Health -5")
        else:
            plant.health-= 5
            print("Snow damages the plant. Health -15")
    elif weather == "hail":
        if plant.protected:
            plant.health-=10
            print("Hail blocked by protection.Health -10")
        else:
            plant.health -= 25
            print("Hail is very harmful! Health -25")

    if plant.water<0:
        plant.water=0
    if plant.nutrients<0:
        plant.nutrients=0
    if plant.health<0:
        plant.health=0
    plant.status()

    print("\nWhat do you want to do?")
    print("1.Water plant (+20 water)")
    print("2.Add nutrients (+15 nutrients)")
    print("3.Activate protection(greehouse)")
    print("4.Do nothing")

    choice=input("Choose an option (1/2/3/4):")

    if choice=="1":
        plant.water+=20
        print("You watered the plant.Water +20")
    elif choice=="2":
        plant.nutrients+=15
        print("You added nutrients.Nutrients +15")
    elif choice=="3":
        plant.protected=True
        print("Protection activated.")
    elif choice=="4":
        print("You did nothing today.")
    else: 
        print("Invalid choice.")

    #Protection Lasts one day only 
    plant.protected=False 
    
    day+=1
print("\n The plant has died")
print("You kept it alive for",day -1,"days.")
