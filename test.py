import numpy

print("Welcome to Python Pizza Deliveries!")

def ask_for_topping(topping : str) -> str | None:

    user_topping = input(f"Do you want {topping} on your pizza? Y / N: ")
    if user_topping == "Y": return topping
    else: return None

size = input("What size pizza do you want? S, M or L: ")
type_of_pizza = input("What type of pizza do you want? pan or hand: ")

available_toppings = ["pepperoni", "extra cheese", "onion"]
toppings = [size, type_of_pizza]
toppings_price = {"S": 4, "M": 5, "L": 5, "pepperoni": 3, "extra cheese": 1, "onion": numpy.pi, "pan": 3, "hand": 4}

for topping in available_toppings:
    topping = ask_for_topping(topping)

    if topping is not None:
        toppings.append(topping)

bill = 0

for topping in toppings:
    bill += toppings_price[topping]


print(f"Your total bill is ${bill}")
print("Thank you for using Pizza Deliveries!")