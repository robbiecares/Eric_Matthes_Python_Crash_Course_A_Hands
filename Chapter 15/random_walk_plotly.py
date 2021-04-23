#import plotly.express as px
from random_walk import RandomWalk
import plotly.graph_objects as go


while True:
    # Make a random walk.
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Plot the points in the walk.
    x = rw.x_values
    y = rw.y_values
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            mode='markers',
            x=rw.x_values,
            y=rw.y_values))

    # todo: Emphasize the first and last points.

    fig.add_trace(
        go.Scatter(
            mode='markers',
            x=[0],
            y=[0],
            color='green',
            size=12))

    # Remove the axes.

    # Show results
    fig.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

