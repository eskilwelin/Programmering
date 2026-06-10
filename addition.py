"""
Två input tal
val = Input addition eller subtraktion

"""

while True:

    val = str.lower(input("Välj 'addition', 'subtraktion', 'gånger' eller 'division': "))

    if val not in ["addition", "+", "subtraktion", "-", "gånger", "*", "division", "/"]:
        print("Felaktigt val, välj addition, gånger, division eller subtraktion")
        continue


    tal1 = int(input("Välj tal ett: "))
    tal2 = int(input("Välj tal två: "))

    if val == "division" or "/" and tal2 == 0:
        print("Dividera inte med 0 tack.")
        continue
        
    if val == "addition" or val == "+":
        addition = tal1 + tal2
        print(f"Resultatet blir: {addition}")
    elif val == "subtraktion" or val == "-":
        subtraktion = tal1 - tal2
        print(f"Resultatet blir: {subtraktion}")
    elif val == "gånger" or val == "*":
        multiplikation = tal1 * tal2
        print(f"Resultatet blir: {multiplikation}")
    else:
        division = tal1 / tal2
        print(f"Resultatet blir: {division}")

    again = str.lower(input("Vill du testa ett till tal? Ja / Nej "))
   
    if again != "ja":
        exit()