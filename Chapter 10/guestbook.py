filename = "text_files/guestbooklog.txt"
active = True

while active:
    guest = input("Please enter your name in our guest book: ")
    print(f"Welcome, {guest}!")
    with open(filename,"a") as file_object:
        file_object.write(f"{guest}\n")

    moreguests = input("Would another guest like to sign-in? ")
    if moreguests == "y":
        continue
    else:
        active = False
        print("Enjoy your visit!")