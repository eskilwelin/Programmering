""""

import math is cheat

DONE:
- Konvertera till funktioner


TODO: 
- Fixa nästlade if satser med if not https://lawyerdev.medium.com/i-never-write-nested-ifs-e4e91a5440ee
- Fixa user input 
- Lägg till fler opperander / funktionalitet
- Snygga till all text / output 

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
        if inp.isnumeric() != True and inp.find("-") == -1:
            if inp == "":
                if len(inputs) < 2:
                    print("Skriv minst 2 siffror!")
                    continue
                else:
                    break
            print("Bara siffror tack!!!")
            continue
        inputs.append(int(inp))
    
    return inputs


while True:

    operator = str.lower(input("Välj en operator + - / * : "))

    if operator not in ["addition", "+", "subtraktion", "-", "gånger", "*", "division", "/"]:
        print("Felaktigt val, välj + - / *")
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

