import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

def histogram(data):
    # 'next()' gets a reader object and returns the next line of the file
    reader = data.getFileReader()
    title = data.plot_title
    header_row = next(reader)
    error_msg = []
    # get TMAX in 5th row in the csv file
    ages = []
    for row in reader:
        type = str(row[-1])
        id = str(row[1])
        try: 
            age = int(row[3])
        except ValueError:
            error_msg.append(f"Missing data for {id} - {type}")
        else:     
            ages.append(age)
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots(dpi=360)
    ax.hist(ages, bins=10, edgecolor='black')
    # Set the title and labels
    ax.set_title(title, fontsize=24)
    ax.set_xlabel("Age", fontsize=14)
    ax.set_ylabel("Number of Patients", fontsize=14)

    result = {'figure': fig, 'message': error_msg}
    return result

