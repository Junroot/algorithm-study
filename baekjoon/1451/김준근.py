expression = input()
met_minus = False
result = 0
number = 0


def calculate_number():
    global result, number
    if met_minus:
        result -= number
    else:
        result += number
    number = 0


for character in expression:
    if character == "-":
        calculate_number()
        met_minus = True
    elif character == "+":
        calculate_number()
    else:
        number = number * 10 + int(character)

calculate_number()
print(result)


