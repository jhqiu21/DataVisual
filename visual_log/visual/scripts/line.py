import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

def line_chart(data):
    # initialize figure
    plt.style.use(data.style)
    fig, ax = plt.subplots(dpi=360)
    title = data.plot_title
    error_msg = ["Error!"]
    try:
        paraXs = data.para_data.get('paraX_datas')
        paraYs = data.para_data.get('paraY_datas')
        missing_msg = data.para_data.get('message')
    except IndexError:
        error_msg.append("You input an invalid parameter!")
        return {'figure': fig, 'message': error_msg}

    ax.plot(paraXs[0], paraYs[0], linewidth=2)
    
    # Set the title and labels
    ax.set_title(title, fontsize=data.plot_title_font)
    ax.set_xlabel(data.x_title, fontsize=data.x_font)
    ax.set_ylabel(data.y_title, fontsize=data.y_font)

    # pack result information
    result = {'figure': fig, 'message': missing_msg}
    return result


