import matplotlib.pyplot as plt

input = []
output = []
 
x_value = range(1, 1001)
y_value = [x ** 2 for x in x_value]


plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots()
ax.plot(input, output, linewidth = 3)


# set the title and x,y-axis of the figure
ax.set_title("Title", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("y-axis", fontsize = 14)

# set the fontsize of x,y-label of the figure
ax.tick_params(axis = 'both', which = 'major',labelsize = 14)

plt.show()

