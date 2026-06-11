"""
Två input tal
val = Input addition eller subtraktion

"""

def addition(i, j):
    return i + j

def subtraktion(i, j):
    return i - j

def multiplikation(i, j):
    return i * j

def division(i, j):
    if j == 0:
        return "ERROR! Dividera inte med noll!"
    else:
        return i / j



while True:

    val = str.lower(input("Välj 'addition', 'subtraktion', 'gånger' eller 'division': "))

    if val not in ["addition", "+", "subtraktion", "-", "gånger", "*", "division", "/"]:
        print("Felaktigt val, välj addition, gånger, division eller subtraktion")
        continue

    tal1 = int(input("Välj tal ett: "))
    tal2 = int(input("Välj tal två: "))

        
    if val == "addition" or val == "+":
        print(f"Resultatet blir: {addition(tal1, tal2)}")
    elif val == "subtraktion" or val == "-":
        print(f"Resultatet blir: {subtraktion(tal1, tal2)}")
    elif val == "gånger" or val == "*":
        print(f"Resultatet blir: {multiplikation(tal1, tal2)}")
    else:
        print(f"Resultatet blir: {division(tal1, tal2)}")

    again = str.lower(input("Vill du testa ett till tal? Ja / Nej "))
   
    if again != "ja" and again != "j":
        exit()