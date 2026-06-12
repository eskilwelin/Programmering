""""

import math IS CHEAT

TODO: 
- Lägg till fler operatorer / funktionalitet
- Alla funktioner för uträkningar är återanvänd kod, konvertera det till en funktion eller ett objekt 

"""
from math_at_home import op

while True:

    print("Välj en operator + - / * : ")
    operator = input("> ")

    if operator not in ["+", "-", "*", "/"]:
        print("Felaktigt val, välj + - / * ")
        continue
    
    users_numbers = op.user_num()

    calc_output = op.calculation(users_numbers, operator)

    match operator:
        case "+":
            result = op.add(users_numbers)
        case "-":
            result = op.sub(users_numbers)
        case "*":
            result = op.mult(users_numbers)
        case _:
            result = op.div(users_numbers)

    if result == "ERROR! Ingen division med 0!":
        print(result)
    else:
        print(f"{calc_output} = {result}")

    run_again = str.lower(input('Om du vill köra programmet igen säg "Ja": '))
   
    if not run_again == "ja" and not run_again == "j":
        print("Tack och hej!")
        break

