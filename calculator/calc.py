
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
