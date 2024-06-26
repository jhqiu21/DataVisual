import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.transforms import Affine2D
from matplotlib.patches import Ellipse
import pandas as pd
from datetime import datetime
import numpy as np


def confidence_ellipse_gram(data):
    # initialize figure
    plt.style.use(data.style)
    fig, ax_nstd = plt.subplots(figsize=(6, 6), dpi=360)
    title = data.plot_title
    error_msg = ["Error!"]
    try:
        paraXs = data.para_data.get('paraX_datas')
        paraYs = data.para_data.get('paraY_datas')
        missing_msg = data.para_data.get('message')
    except IndexError:
        error_msg.append("You input an invalid parameter!")
        return {'figure': fig, 'message': error_msg}

    

    dependency_nstd = [[0.8, 0.75],[-0.2, 0.35]]
    mu = 0, 0
    scale = 8, 5

    ax_nstd.axvline(c='grey', lw=1)
    ax_nstd.axhline(c='grey', lw=1)

    x = paraXs[0]
    y = paraYs[0]

    ax_nstd.scatter(x, y, s=0.5)

    confidence_ellipse(x, y, ax_nstd, n_std=1,
                    label=r'$1\sigma$', edgecolor='firebrick')
    confidence_ellipse(x, y, ax_nstd, n_std=2,
                    label=r'$2\sigma$', edgecolor='fuchsia', linestyle='--')
    confidence_ellipse(x, y, ax_nstd, n_std=3,
                    label=r'$3\sigma$', edgecolor='blue', linestyle=':')

    ax_nstd.scatter(mu[0], mu[1], c='red', s=3)
    ax_nstd.set_title(title, fontsize=data.plot_title_font)
    ax_nstd.set_xlabel(data.x_title, fontsize=data.x_font)
    ax_nstd.set_ylabel(data.y_title, fontsize=data.y_font)
    ax_nstd.legend()
    
    # pack result information
    result = {'figure': fig, 'message': missing_msg}
    return result

def confidence_ellipse(x, y, ax, n_std=3.0, facecolor='none', **kwargs):
    """
    Create a plot of the covariance confidence ellipse of *x* and *y*.

    Parameters
    ----------
    x, y : array-like, shape (n, )
        Input data.

    ax : matplotlib.axes.Axes
        The Axes object to draw the ellipse into.

    n_std : float
        The number of standard deviations to determine the ellipse's radiuses.

    **kwargs
        Forwarded to `~matplotlib.patches.Ellipse`

    Returns
    -------
    matplotlib.patches.Ellipse
    """
    if len(x) != len(y):
        raise ValueError("x and y must be the same size")

    cov = np.cov(x, y)
    pearson = cov[0, 1]/np.sqrt(cov[0, 0] * cov[1, 1])
    # Using a special case to obtain the eigenvalues of this
    # two-dimensional dataset.
    ell_radius_x = np.sqrt(1 + pearson)
    ell_radius_y = np.sqrt(1 - pearson)
    ellipse = Ellipse((0, 0), width=ell_radius_x * 2, height=ell_radius_y * 2,
                      facecolor=facecolor, **kwargs)

    # Calculating the standard deviation of x from
    # the squareroot of the variance and multiplying
    # with the given number of standard deviations.
    scale_x = np.sqrt(cov[0, 0]) * n_std
    mean_x = np.mean(x)

    # calculating the standard deviation of y ...
    scale_y = np.sqrt(cov[1, 1]) * n_std
    mean_y = np.mean(y)

    transf = Affine2D() \
        .rotate_deg(45) \
        .scale(scale_x, scale_y) \
        .translate(mean_x, mean_y)

    ellipse.set_transform(transf + ax.transData)
    return ax.add_patch(ellipse)
