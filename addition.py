""""
import math is cheat

"""

def addition(n):
    result = 0
    for number in n:
        result += number
    return result

def subtraktion(n):
    result = n[0]
    n.pop(0)
    for number in n:
        result -= number
    return result

def multiplikation(n):
    result = n[0]
    n.pop(0)
    for number in n:
        result *= number
    return result

def division(n):
    result = n[0]
    n.pop(0)
    if 0 in n:
        return "ERROR! Dividera inte med noll!"
    for number in n:
        result /= number
    return result


def tal():
    inputs = []
    while True:
        inp = input("Skriv siffror, skicka en tom rad efter sista siffran: ")
        
        if inp == "":
            break
        inputs.append(int(inp))

    return inputs


while True:

    val = str.lower(input("Välj 'addition', 'subtraktion', 'gånger' eller 'division': "))

    if val not in ["addition", "+", "subtraktion", "-", "gånger", "*", "division", "/"]:
        print("Felaktigt val, välj addition, gånger, division eller subtraktion")
        continue


    if val == "addition" or val == "+":
        result = addition(tal())
        print(f"Resultatet blir: {result}")
    elif val == "subtraktion" or val == "-":
        result = subtraktion(tal())
        print(f"Resultatet blir: {result}")
    elif val == "gånger" or val == "*":
        result = multiplikation(tal())
        print(f"Resultatet blir: {result}")
    else:
        result = division(tal())
        print(f"Resultatet blir: {result}")

    again = str.lower(input("Vill du köra programmet en gång till? Ja / Nej "))
   
    if again != "ja" and again != "j":
        print("Tack och hej!")
        break

