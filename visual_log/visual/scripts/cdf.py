import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

def cumulative_distributions(data):
    reader = data.getFileReader()
    title = data.plot_title
    # 'next()' gets a reader object and returns the next line of the file
    header_row = next(reader)
    error_msg = ""
    ages = []
    for row in reader:
        type = str(row[-1])
        id = str(row[1])
        try: 
            age = int(row[3])
        except ValueError:
            error_msg += f"Missing data for {id} - {type}" + '<br>'
        else:     
            ages.append(age)
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots(dpi=360)

    ax.ecdf(ages, label="CDF")
    n, bins, patches = ax.hist(ages, 25, density=True, histtype="step",
                               cumulative=True, label="Cumulative histogram")
    
    # Set the title and labels
    ax.set_title(title, fontsize=24)
    ax.set_xlabel("Age", fontsize=14)
    ax.set_ylabel("Number of Patients", fontsize=14)

    result = {'figure': fig, 'message': error_msg}
    return result