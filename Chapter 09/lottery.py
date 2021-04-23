import random

def lotto_drawing():
    nums = (0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E")
    winners = tuple(random.choices(nums,k=4))
    winnums = ""
    for char in winners:
        winnums += f"{str(char)} "
    fwinnums = winnums[:-1]
    #print(f"Any ticket matching '{fwinnums}' exactly wins a prize!")
    return winners

myTicket = (1,1,3,4)
winners = lotto_drawing()
drawingNum = 1
while myTicket != winners:
    winners = lotto_drawing()
    drawingNum += 1

print(f"It took {drawingNum} draws for you to win the lottery!")


