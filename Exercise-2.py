def toc(given):
     C = (int(given)-32)*5/9
     print("Temperature in celsius: ",C,"°C")
     	
def tofe(given):
     F = int(given)*3.28084
     print("Length in feet: ",F," feet")
def tof(given):
     F = (int(given) * 9/5) + 32
     print("Temperature in fahrenheit: ",F,"°F")
def tom(given):
     M = float(given) / 3.28084
     print("Lenght in meter: ",M," meters")

given = input("Enter a magnitude to convert: ")
ins = input("Enter instructions: ")
print("1 to convert celsius to fahrenheit")
print("2 to convert fahrenheit to celsius" )
print("3 to convert from meter to feet")
print("4 to convert from feet to meter ")

if int(ins) == 1:
     tof(given)
elif int(ins) == 2:
     toc(given)
elif int(ins) == 3:
     tofe(given)
elif int(ins) == 4:
     tom(given)
    
     





