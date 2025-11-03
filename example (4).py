
def classify_person(ag):
     if ag < 13:
          print("Child")
     elif ag > 12 and ag <18:
          print("Teenager")
     elif ag > 17 and ag <65:
          print("Adult")
     elif ag >= 65:
          print("Senior") 
classify_person(int(input("How old are you ")))

hour = int(input("Enter an hour in 24 hours format: "))
min = int(input("Enter min: "))

if hour > 4 & hour < 12:
     print("Morning")
     print(hour,":",min)
elif hour > 11 and hour < 17:
     print("Afternooon")
     print(hour,":",min)
elif hour > 16 and hour <21:
     print("Evening")
     print(hour,":",min)
elif hour >21:
     print("Night")
     print(hour,":",min)
     
     
number = int(input("Enter a random number: "))

if number % 5 == 0:
     print("Divisible by 5.")
else:
     print("Not divisible by 5.")
     