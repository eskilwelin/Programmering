""""

import math IS CHEAT

TODO: 
- Lägg till fler opperander / funktionalitet
- Alla funktioner för uträkningar är återanvänd kod, konvertera det till en funktion eller ett objekt 

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

# Det går att dividera 0 men inte att dividera med 0
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
    print("Ange ett tal åt gången, skicka en tom rad efter sista talet.")
    while True:
        user_input = input("> ")
        if user_input == "":
            if len(num_list) < 2:
                print("Ange minst 2 siffror!")
                continue
            else:
                break
        try:
            converted_input = int(user_input)
        except ValueError:
            print("Bara siffror tack!")
            continue
        num_list.append(converted_input)
    
    return num_list

def calculation(num_list, operator):
    output = ""
    for num in num_list[:-1]:
        output += str(num) + " " + operator + " "
    output += str(num_list[-1])
    return output

while True:

    print("Välj en operator + - / * : ")
    operator = input("> ")

    if operator not in ["+", "-", "*", "/"]:
        print("Felaktigt val, välj + - / * ")
        continue
    
    users_numbers = user_num()

    calc_output = calculation(users_numbers, operator)

    match operator:
        case "+":
            result = add(users_numbers)
        case "-":
            result = sub(users_numbers)
        case "*":
            result = mult(users_numbers)
        case _:
            result = div(users_numbers)

    if result == "ERROR! Ingen division med 0!":
        print(result)
    else:
        print(f"{calc_output} = {result}")

    run_again = str.lower(input('Om du vill köra programmet igen säg "Ja": '))
   
    if not run_again == "ja" and not run_again == "j":
        print("Tack och hej!")
        break

