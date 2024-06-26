import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import numpy as np

def histogram(data):
    # initialize figure
    plt.style.use(data.style)
    fig, ax = plt.subplots(dpi=360)
    title = data.plot_title
    error_msg = ["Error!"]
    try:
        paraXs = data.para_data.get('datas')
        missing_msg = data.para_data.get('message')
    except IndexError:
        error_msg.append("You input an invalid parameter!")
        return {'figure': fig, 'message': error_msg}

    ax.hist(paraXs[0], bins=data.bin, edgecolor='black', label=data.para[0])
    
    # Set the title and labels
    ax.set_title(title, fontsize=data.plot_title_font)
    ax.set_xlabel(data.x_title, fontsize=data.x_font)
    ax.set_ylabel(data.y_title, fontsize=data.y_font)
    
    if data.legend == 1:
        ax.legend()
        
    # pack result information
    result = {'figure': fig, 'message': missing_msg}
    return result


def bihistogram(data):
    # initialize figure
    plt.style.use(data.style)
    fig, ax = plt.subplots(dpi=360)
    title = data.plot_title
    error_msg = ["Error!"]
    try:
        paraXs = data.para_data.get('datas')
        missing_msg = data.para_data.get('message')
    except IndexError:
        error_msg.append("You input an invalid parameter!")
        return {'figure': fig, 'message': error_msg}

    
    ax.hist(paraXs[0], bins=data.bin, edgecolor='black', label=data.para[0])
    ax.hist(paraXs[1], weights=-np.ones_like(paraXs[0]), bins=data.bin, edgecolor='black', label=data.para[1])
    # Set the title and labels
    ax.set_title(title, fontsize=data.plot_title_font)
    ax.set_xlabel(data.x_title, fontsize=data.x_font)
    ax.set_ylabel(data.y_title, fontsize=data.y_font)
    
    if data.legend == 1:
        ax.legend()

    # pack result information
    result = {'figure': fig, 'message': missing_msg}
    return result

