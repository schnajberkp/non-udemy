import random
def nextNumber(val):
    random_number = random.randint(1,11)
    sum = random_number + val
    print(random_number)
    response = input("Prejete si pridat dalsi?")
    if response == "Y" or "y":
        print(sum)
        if sum == 21:
            print("Vyhral jsi")
            exit()
        elif sum > 21:
            print("Prohral jsi")
            exit()
        nextNumber(sum)

user_input = input("Zadej Y nebo N \n")
if user_input == "Y" or "y":
    nextNumber(val=0)
