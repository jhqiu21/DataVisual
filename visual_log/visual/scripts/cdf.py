import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd



def cumulative_distributions(data):
    # initialize figure
    plt.style.use(data.style)
    fig, ax = plt.subplots(dpi=360)
    title = data.plot_title
    error_msg = ["Error!"]
    data_set = data.para_data.get('datas')
    missing_msg = data.para_data.get('message')

    for idx, datas in  enumerate(data_set):
        try:
            datas = [eval(i) for i in data_set[idx]]
        except IndexError:
            error_msg.append("You input an invalid parameter!")
            return {'figure': fig, 'message': error_msg}
        
        ax.ecdf(datas, label="CDF")
        ax.hist(datas, data.bin, density=True, histtype="step",
                cumulative=True, label="Cumulative histogram")
    

    # Set the title and labels
    ax.grid(True)
    ax.legend()
    ax.label_outer()
    ax.set_title(title, fontsize=data.plot_title_font)
    ax.set_xlabel(data.x_title, fontsize=data.x_font)
    ax.set_ylabel(data.y_title, fontsize=data.y_font)

    result = {'figure': fig, 'message': missing_msg}
    return result


