Name = input("Enter your name ")
Age = int(input ("Enter your age "))
Year = 2022
def getYear():
    return Year - Age
print("Hello, " + Name + " your year of birth is ", getYear())
