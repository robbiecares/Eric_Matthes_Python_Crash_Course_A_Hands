import json
import verify_int_input as vint

def requestFavNum():
    message = "Enter your favorite number & I'll remember it: "
    favNum = vint.ver_num(input(message))
    return favNum


def retrieveFavNum(filename):
    try:
        with open(filename) as f:
            favNum = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return favNum


def storeFavNum(favNum,filename):
    try:
        with open(filename,"w") as f:
            json.dump(favNum,f)
    except FileNotFoundError:
        print("the file for saving your favorite number cannot be found!")
        return None
    else:
        message = (f"I've stored '{favNum}' as your favorite number!")
        print(message)


root = "text_files/"
filename = "fav_nums.txt"
fullfilename = root + filename

favNum = retrieveFavNum(fullfilename)
if favNum:
    print(f"Your favorite number is {favNum}!")
else:
    favNum = requestFavNum()
    storeFavNum(favNum,fullfilename)
