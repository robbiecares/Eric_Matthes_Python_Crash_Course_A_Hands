print("Let's add two numbers! (type 'q' at any time to quit)\n")


def request_num(message):
    num = input(message)
    return num


def ver_num(num):
    while type(num) != int:
        if num == "q":
            break
        try:
            num = int(num)
        except ValueError:
            message = "The number should consist only of digits from 0-9. Please try again!"
            print(message)
            num = request_num("Enter a number: ")
    return num


num1 = ver_num(request_num("Enter a number: "))
num2 = ver_num(request_num("Enter another number: "))

sum = num1 + num2
print(f"\n{num1} + {num2} = {sum}")
