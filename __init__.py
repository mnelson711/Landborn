import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
import pandas as pd
import numpy as np
from barplot import barplot as barplot


def scatterplot(df, xvar, yvar, color='k',colormap='viridis', size=1, marker='.', ax=None):
    if ax is None:
        fig, ax = plt.subplots()
    if isinstance(xvar, str) and df is not None:
        xdata = df[xvar]
    else:
        xdata = xvar
    


def lineplot(df, x=[], y=[], color='k', size=1, style='-', marker=None, ax=None):
    if ax is None:
        fig, ax = plt.subplots()

    # Check if xvar is a column in df
    if isinstance(x, str) and df is not None:
        xdata = df[x]
    else:
        xdata = x

    # Check if yvar is a column in df
    if isinstance(y, str):
        ydata = df[y]
    else:
        ydata = y

    line = mlines.Line2D(xdata, ydata, color=color, linestyle=style, marker=marker, markersize=size)

    ax.add_line(line)
    ax.autoscale()

    return ax

if __name__=='__main__':
    #Units Tests Below
    df = pd.DataFrame({
    'xvals': np.random.normal(0,1,100),
    'yvals': np.random.normal(0,3,100)
    })
    barplot(df, 'xvals', 'yvals', orientation='vertical')
    print('main file has run')