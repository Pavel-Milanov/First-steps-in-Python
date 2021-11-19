import math
import re

print("Chose 2, 16, 8, 5, 10")
chosen = input()

regex = r"([\d]+)([\d]+)?"

test_str = ("673\n"
            "1659412\n"
            "asdg6412gh\n"
            "awsdge641649"
            "466413\n"
            "000011111\n"
            "1695632\n\n")
matches = re.finditer(regex, test_str, re.MULTILINE)

nums = []

for matchNum, match in enumerate(matches, start=1):
    nums.append(match.group())

if chosen == "2":
    for num in nums:
        print(bin(int(num)))


elif chosen == "16":
    for num in nums:
        print(hex(int(num)))


elif chosen == "8":
    for num in nums:
        print(oct(int(num)))


elif chosen == "5":
    for num in nums:
        s = ""
        number = int(num)
        while number > 1:
            current = number % 5
            s = str(math.trunc(current % 10)) + s
            number /= 5
        print(s)


elif chosen == "10":
    for number in nums:
        print(number)
