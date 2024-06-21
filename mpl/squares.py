import matplotlib.pyplot as plt

# input = [1, 2, 3, 4, 5]
# output = [1, 4, 9, 16, 25]
 
x_value = range(1, 1001)
y_value = [x ** 2 for x in x_value]


plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots()
# ax.plot(input, output, linewidth = 3)

# ax.scatter(input, output, s = 100)
# Use `c` to set color. We can also use RGB format i.e. c = (0, 0.8, 0)
ax.scatter(x_value, y_value, c = 'red', s = 5)
ax.axis([0, 1100, 0, 1100000])

# set the title and x,y-axis of the figure
ax.set_title("Title", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("y-axis", fontsize = 14)

# set the fontsize of x,y-label of the figure
ax.tick_params(axis = 'both', which = 'major',labelsize = 14)

# plt.show()

# save the figure
plt.savefig('square_plot.png', bbox_inches = 'tight')