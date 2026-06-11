""""
import math is cheat

"""

def add(n):
    result = 0
    for number in n:
        result += number
    return result

def sub(n):
    result = n[0]
    n.pop(0)
    for number in n:
        result -= number
    return result

def mult(n):
    result = n[0]
    n.pop(0)
    for number in n:
        result *= number
    return result

def div(n):
    result = n[0]
    n.pop(0)
    if 0 in n:
        return "ERROR! Dividera inte med noll!"
    for number in n:
        result /= number
    return result


def user_tal():
    inputs = []
    while True:
        inp = input("Skriv siffror, skicka en tom rad efter sista siffran: ")
        if inp == "":
            if len(inputs) < 2:
                print("Skriv minst 2 siffror!")
                continue
            else:
                break
        inputs.append(int(inp))
    
    return inputs


while True:

    operator = str.lower(input("Välj 'addition', 'subtraktion', 'gånger' eller 'division': "))

    if operator not in ["addition", "+", "subtraktion", "-", "gånger", "*", "division", "/"]:
        print("Felaktigt val, välj addition, gånger, division eller subtraktion")
        continue


    if operator == "addition" or operator == "+":
        result = add(user_tal())
        print(f"Resultatet blir: {result}")
    elif operator == "subtraktion" or operator == "-":
        result = sub(user_tal())
        print(f"Resultatet blir: {result}")
    elif operator == "gånger" or operator == "*":
        result = mult(user_tal())
        print(f"Resultatet blir: {result}")
    else:
        result = div(user_tal())
        print(f"Resultatet blir: {result}")

    again = str.lower(input("Vill du köra programmet en gång till? Ja / Nej "))
   
    if again != "ja" and again != "j":
        print("Tack och hej!")
        break

