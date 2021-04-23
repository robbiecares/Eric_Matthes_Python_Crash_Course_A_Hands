import die

dice = [die.Die(size) for size in [6, 12, 20]]

for die in dice:
    results = []
    for i in range(10):
        result = die.roll_die()
        results.append(result)
    print(results)





