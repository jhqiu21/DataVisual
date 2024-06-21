# simulate rolling a die in n times and analyze the distribution of the results
from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die


die = Die()
roll_nums = int(input("Enter the number of rolling: "))
results = []

for roll_num in range(roll_nums):
    result = die.roll()
    results.append(result)

# analyze the results
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# visualize the result
x_values = list(range(1, die.num_sides + 1))
data = [Bar(x = x_values, y = frequencies)]

x_axis_config = {'title': 'result'}
y_axis_config = {'title': 'frequency'}

# class Layoout return an object set the config of the figure
my_layout = Layout(title = '1d6 for ' + str(roll_nums) +' times', 
                   xaxis = x_axis_config, 
                   yaxis = y_axis_config)

# call offline to produce a html file to show the figure
filename = '1d6_' + str(roll_nums) + '.html'
offline.plot({'data': data, 'layout': my_layout}, filename = filename)
