""""

import math is cheat

DONE:
- Konvertera till funktioner
- User input blockerar negativa tal
- Konvertera output till switch / case

TODO: 
- Fixa nästlade if satser med if not https://lawyerdev.medium.com/i-never-write-nested-ifs-e4e91a5440ee
- Fixa user input validering för "-", för tillfället tillåts "-hej" osv.
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
    
    match operator:
        case "+":
            result = add(user_num())
            print(f"Resultatet blir: {result}")
        case "-":
            result = sub(user_num())
            print(f"Resultatet blir: {result}")
        case "*":
            result = mult(user_num())
            print(f"Resultatet blir: {result}")
        case _:
            result = div(user_num())
            if result == "ERROR! Ingen division med 0!":
                print(result)
            else:
                print(f"Resultatet blir: {result}")

    run_again = str.lower(input('Om du vill köra programmet igen säg "Ja": '))
   
    if not run_again == "ja" and not run_again == "j":
        print("Tack och hej!")
        break

