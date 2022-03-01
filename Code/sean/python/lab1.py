# 1 
'''
user = int(input("what is the distance in feet? "))
answer = user * 0.3048
print(f"{user} ft is {round(answer, 4)} m")
'''

#2
'''
unit = {"feet": 0.3048,
        "miles": 1609.34,
        "meters": 1,
        "kilometers": 1000}

question_1 = int(input("what is the distance? "))

question_2 = input("what are the units? feet, miles, meters or kilometers? ")


answer = unit[question_2] * question_1
answer = int(answer)

print(f"{question_1} {question_2} is {answer} m.")
'''

#3

unit = {"feet": 0.3048,
        "miles": 1609.34,
        "meters": 1,
        "kilometers": 1000,
        "yards": 0.9144, }

question_1 = int(input("what is the distance? "))

question_2 = input("what are the units? feet, miles, meters or kilometers? ")


answer = unit[question_2] * question_1
answer = int(answer)

print(f"{question_1} {question_2} is {answer} m.")