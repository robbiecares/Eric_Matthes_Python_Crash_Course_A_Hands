import matplotlib.pyplot as plt
plt.style.available

#input_values = [1,2,3,4,5]
#squares = [1,4,9,16,25]

x_values = range(1,5001)
y_values = [x**3 for x in x_values]

plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

#ax.plot(input_values, squares, linewidth = 3)

#Set chart title & label axes
ax.set_title("Cubes", fontsize = 14)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Cube of value", fontsize = 14)

#Set size of tick labels
ax.tick_params(axis="both", which = "major", labelsize = 14)

#Set the range for each axis
ax.axis([0,(x_values[-1]),0,y_values[-1]])

plt.show()

#pg. 313