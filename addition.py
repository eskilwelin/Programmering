""""

import math is cheat

DONE:
- Konvertera till funktioner
- User input blockerar negativa tal
- Konvertera output till switch / case
- Fixa user input validering för "-", för tillfället tillåts "-hej" osv.
- La till en funktion för att lista hela uträkningen i output

TODO: 
- Fixa nästlade if satser med if not https://lawyerdev.medium.com/i-never-write-nested-ifs-e4e91a5440ee
- Lägg till fler opperander / funktionalitet
- Snygga till all text / output 
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
    print("Ange en siffra åt gången, skicka en tom rad efter sista siffran.")
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

    print(f"{calc_output} = {result}")

    run_again = str.lower(input('Om du vill köra programmet igen säg "Ja": '))
   
    if not run_again == "ja" and not run_again == "j":
        print("Tack och hej!")
        break

