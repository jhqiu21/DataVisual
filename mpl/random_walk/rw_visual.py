# Generate and save 'random walk' figures 

import matplotlib.pyplot as plt
from mpl.random_walk.random_walk import RandomWalk

total_number = int(input("Enter the number of figures you want to generate: "))
count = 1

# Keep random  walk if the program is running
while count <= total_number: 
    rw = RandomWalk(50_000)
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize = (9, 6))
    # use color to show the order of each nodes
    point_number = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c = point_number, 
               cmap = plt.cm.Blues, edgecolors = 'none', s = 3)
    
    # hide x,y-axis
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # plt.show()
    # save the figure with name '#.png'
    fig_name = "random_walk" + str(count) + ".png"
    plt.savefig(fig_name, bbox_inches = 'tight')
    count += 1
    # enter y/n to tell the program whether to generate a new figure
    # keep_running = input("Make another walk? (y/n): ")
    