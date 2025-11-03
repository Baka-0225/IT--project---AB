def low(income):
     tax = int(income) * 0
     print("Tax: ",tax,"$")
def mod(income):
     tax = int(income) * 15/100
     print("Tax: ",tax,"$")
def high(income):
     tax = int(income) * 20/100
     print("Tax: ",tax,"$")
def very_high(income):
     tax = int(income) * 35/100
     print("Tax: ",tax,"$")
def over(income):
     tax = int(income) * 30/100
     print("Tax: ",tax,"$")
def over_over(income):
     tax = int(income) * 35/100
     print("Tax: ",tax,"$")
income = input("How much do you earn: ")

if int(income) <= 2000:
     low(income)
elif int(income) > 2000 and int(income) <= 4000:
     mod(income)
elif int(income) > 4000 and int(income) <= 7000:
     high(income)
elif int(income) > 7000 and int(income) <= 10000:
     very_high(income)
elif int(income) > 10000 and int(income) <= 14000:
     over(income)
elif int(income) > 14000:
     over_over(income)

     