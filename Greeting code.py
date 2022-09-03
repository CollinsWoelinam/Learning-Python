import datetime
name = input("Enter your name")
now = datetime.datetime.now()
now.hour

if now.hour < 12:
    print("Good morning", name)
elif 12 <= now.hour < 16:
    print("Good afternoon", name)
else:
    print("Good evening", name)
