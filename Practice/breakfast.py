name = input("Enter your name: ")
money = int(input("Enter your cash amount: "))
hungry = input("Are you hungry? (y/n): ")

if hungry == "y":
    if money > 30:
        print(f"{name} should go to eat breakfast.")
    else:
        print(f"{name} is hungry but might not have enough money to eat breakfast.")
elif hungry == "n":
    if money > 30:
        print(f"{name} has budget but doesn't want to eat breakfast.")
    else:
        print(f"{name} has no money but isn't hungry")
else:
    print("Please make sure that you enter either y or n")


lang = input("Which language do you want to learn: ")

# if lang == "php":
#     print("You will be a backend engineer.")
# elif lang == "JavaScript":
#     print("You will be a frontend engineer.")
# elif lang == "Python":
#     print("You will be a data scientist.")
# elif lang == "Kotlin":
#     print("You will be an Android engineer.")
# elif lang == "Swift":
#     print("You will be an iOS engineer.")
# else:
#     print("You will be a good software engineer.")


match lang:
    case "php":
        print("You will be a backend engineer.")
    case "JavaScript":
        print("You will be a frontend engineer.")
    case "Python":
        print("You will be a data scientist.")
    case "Kotlin":
        print("You will be an Android engineer.")
    case "Swift":
        print("You will be an iOS engineer.")
    case _:
        print("You will be a good software engineer.")

dest = input("Where do you wanna go: ")
match dest.split(" "):
    case ["Go", "home"]:
        print("I wanna go home.")
    case _:
        print("The system can't determine where do you want to go.")