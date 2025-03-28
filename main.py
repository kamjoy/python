
print("Boudreaux's Barbershop")
print("Type the number for the action you wish to perform and " "\n then hit enter")
print("1. Add a new client")
print("2. Display a list of all current clients")
print("3. Search for a client")
print("4. Delete a client")
print("5. Quit")

print("What do you want to do?")
selection = input()

if selection < "1" or selection > "5":
    print("I'm sorry, that is not an allowed action")
elif selection == "1":
    name = input("Provide the client's name: ")
    phone = int(input("Provide the client's phone number: "))
    dob = int(input("Provide the client's D.O.B. in MMDDYYYY: "))
    print("You've added a new client!")
else:
    print("Quit")


prompt_one = "1"
prompt_two = "2"
prompt_three = "3"
prompt_four = "4"
prompt_five = "5"
