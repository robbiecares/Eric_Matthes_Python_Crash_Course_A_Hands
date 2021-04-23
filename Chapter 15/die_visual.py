"""Use plotly to plot the results of dice rolls"""


from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die
import datetime

power = 2

while power < 8:

    current_time = datetime.datetime.now()
    min = current_time.minute
    second = current_time.second
    micro = current_time.microsecond

    # Create a number of D8's.
    dice_objs = []
    die_1 = Die(8)
    dice_objs.append(die_1)
    die_2 = Die(8)
    dice_objs.append(die_2)


    # Make some rolls, and store results in a list.
    num_of_rolls = 10 ** power
    results = [die_1.roll()*die_2.roll() for roll_num in range(num_of_rolls)]

    # Analyze the results.
    min_result = len(dice_objs)
    max_result = die_1.num_sides * die_2.num_sides
    frequencies = [results.count(value) for value in range(min_result,max_result+1)]

    # Visualize the results.
    x_values = list(range(min_result, max_result + 1))
    data = [Bar(x=x_values, y=frequencies)]

    x_axis_config = {'title': 'Result', 'dtick': 1}
    y_axis_config = {'title': 'Frequency of Result'}
    my_layout = Layout(title=f'Results of rolling {len(dice_objs)} D8 {num_of_rolls} times',
        xaxis=x_axis_config, yaxis=y_axis_config)
    offline.plot({'data': data, 'layout': my_layout}, filename=f'd8_{len(dice_objs)}_{min}_{second}_{micro}.html')

    power += 1
