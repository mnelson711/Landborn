import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
import pandas as pd
import numpy as np

def barplot(df, xvar, yvar, orientation='vertical', color='b', axis=None):
    if axis is None:
        fig, axis = plt.subplots()

    if orientation == 'vertical':
        # Vertical bar plot
        categories = df[xvar].unique()
        x = range(len(categories))
        heights = df.groupby(xvar)[yvar].mean()
        print("the height is: ", heights)
        errors = df.groupby(xvar)[yvar].sem()

        bars = []
        for i, (category, height) in enumerate(zip(categories, heights)):
            rect = mpatches.Rectangle((height - errors[category], y[i] - 0.4), 2 * errors[category], 0.8,facecolor=color, edgecolor='black')

            bars.append(rect)
            axis.add_patch(rect)

        # axis.set_xticks(x)
        # axis.set_xticklabels(categories)
        # axis.set_xlabel(xvar)
        # axis.set_ylabel(yvar)

    elif orientation == 'horizontal':
        # Horizontal bar plot
        categories = df[yvar].unique()
        y = range(len(categories))
        heights = df.groupby(yvar)[xvar].mean()
        errors = df.groupby(yvar)[xvar].sem()

        bars = []
        for i, (category, height) in enumerate(zip(categories, heights)):
            rect = mpatches.Rectangle((height - errors[category], i - 0.4), 2 * errors[category], 0.8,color=color, edgecolor='black')
            bars.append(rect)
            axis.add_patch(rect)

        axis.set_yticks(y)
        axis.set_yticklabels(categories)
        axis.set_ylabel(yvar)
        axis.set_xlabel(xvar)

    return axis