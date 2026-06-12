""""

import math IS CHEAT

TODO: 
- Lägg till fler opperander / funktionalitet
- Alla funktioner för uträkningar är återanvänd kod, konvertera det till en funktion eller ett objekt 

"""
from calculator import calc

while True:

    print("Välj en operator + - / * : ")
    operator = input("> ")

    if operator not in ["+", "-", "*", "/"]:
        print("Felaktigt val, välj + - / * ")
        continue
    
    users_numbers = calc.user_num()

    calc_output = calc.calculation(users_numbers, operator)

    match operator:
        case "+":
            result = calc.add(users_numbers)
        case "-":
            result = calc.sub(users_numbers)
        case "*":
            result = calc.mult(users_numbers)
        case _:
            result = calc.div(users_numbers)

    if result == "ERROR! Ingen division med 0!":
        print(result)
    else:
        print(f"{calc_output} = {result}")

    run_again = str.lower(input('Om du vill köra programmet igen säg "Ja": '))
   
    if not run_again == "ja" and not run_again == "j":
        print("Tack och hej!")
        break

