import re

regex = r"((\-|\+)?(\d+)(\.\d{2})?)"

print("Enter currency from: BGN/EUR/GBP")
currencyFrom = input()

print("Enter value")
value = input()

print("Enter currency to: BGN/EUR/GBP")
currencyTo = input()

if currencyFrom == "BGN":
    if currencyTo == "EUR":
        print(float(value) * 0.51)
    elif currencyTo == "GBP":
        print(float(value) * 0.44)
elif currencyFrom == "EUR":
    if currencyTo == "BGN":
        print(float(value) * 1.96)
    elif currencyTo == "GBP":
        print(float(value) * 0.86)
elif currencyFrom == "GBP":
    if currencyTo == "BGN":
        print(float(value) * 2.28)
    elif currencyTo == "EUR":
        print(float(value) * 1.17)
