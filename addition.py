""""

import math is cheat

DONE:
- Konvertera till funktioner
- User input blockerar negativa tal

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
        return "ERROR! Ingen division med 0!"
    for number in n:
        result /= number
    return result


def user_num():
    num_list = []
    while True:
        user_input = input("Ange en siffra åt gången, skicka en tom rad efter sista siffran: ")
        if not user_input.isnumeric() and user_input.find("-") == -1:
            if user_input == "":
                if len(num_list) < 2:
                    print("Ange minst 2 siffror!")
                    continue
                else:
                    break
            print("Ange enbart siffror.")
            continue
        num_list.append(int(user_input))
    
    return num_list


while True:

    operator = str.lower(input("Välj en operator + - / * : "))

    if operator not in ["+", "-", "*", "/"]:
        print("Felaktigt val, välj + - / * ")
        continue

    if operator == "+":
        result = add(user_num())
        print(f"Resultatet blir: {result}")
    elif operator == "-":
        result = sub(user_num())
        print(f"Resultatet blir: {result}")
    elif operator == "*":
        result = mult(user_num())
        print(f"Resultatet blir: {result}")
    else:
        result = div(user_num())
        if result == "ERROR! Ingen division med 0!":
            print(result)
        else:
            print(f"Resultatet blir: {result}")

    again = str.lower(input("Vill du köra programmet en gång till? Ja / Nej "))
   
    if again != "ja" and again != "j":
        print("Tack och hej!")
        break

