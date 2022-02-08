print("welcome to Unit converter")

"""
user = int(input("what is the distance in ft? "))
answer = user * 0.3048
print(f" {user}ft is {round(answer, 4)}m ")
"""


unit = {"feet": 0.3048,
        "miles": 1609.34,
        "meters": 1,
        "kilometers": 1000,
        "yards": 0.9144,
        "inch:": 0.0254
        }


ask1 = input("what units would you like to use? feet, miles, meters, or kilometers ")

ask2 = float(input("what is the distance? "))

total = unit[ask1] * ask2
print(f"{ask2}{ask1} is {total} meters. ")
