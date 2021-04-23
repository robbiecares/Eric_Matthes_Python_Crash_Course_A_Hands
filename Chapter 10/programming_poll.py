filename = "text_files/poll_responses.txt"
active = True

while active:
    response = input("Tell me why you like programming: ")
    print(f"thank you for your response")
    with open(filename,"a") as file_object:
        file_object.write(f"{response}\n")

    moreresponses = input("Would someone else like to participate in the poll? ")
    if moreresponses == "y":
        continue
    else:
        active = False
