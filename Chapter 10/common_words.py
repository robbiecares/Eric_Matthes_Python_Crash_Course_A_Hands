import re

files = ["The-Art-of-War.txt","The-Island-of-Doctor-Moreau.txt","White-Fang.txt","A-Brief-History-of-the-Internet.txt","Adventures-of-Pinocchio.txt"]

message = "Enter the word you would like to search: "
searchWord = input(message)

for filename in files:
    try:
        with open(f'text_files/{filename}') as f:
            try:
                contents = f.read()
            except UnicodeDecodeError:
                contents = None
                count = "decoding error"
    except FileNotFoundError:
        message = f"'{filename}' is not in the same directory as this program"
        print(message)

    if contents != None:
        wordcheckregex = re.compile(rf'(\b{searchWord}\b)', re.IGNORECASE)
        count = len(wordcheckregex.findall(contents))

    print(f"{filename}: {count}")






