import matplotlib.patches as patches
from matplotlib.path import Path
import matplotlib.pyplot as plt

def scatterplot(df, xvar, yvar, color='k',colormap='viridis', size=1, marker='.', ax=None):
    if ax is None:
        fig, ax = plt.subplots()
    if isinstance(xvar, str) and df is not None:
        xdata = df[xvar]
    else:
        xdata = xvar
        
    if isinstance(yvar, str) and df is not None:
        ydata = df[yvar]
    else:
        ydata = yvar
    
    patches_li = []
    for i, (x, y) in enumerate(zip(xdata, ydata)):
        #creating small square for "point"
        verts = [
        (x, y),  #left, bottom
        (x, y + .1),  #left, top
        (x + .1, y + .1),  #right, top
        (x + .1, y),  #right, bottom
        (x, y),  #back to start
        ]

        codes = [
            Path.MOVETO,
            Path.LINETO,
            Path.LINETO,
            Path.LINETO,
            Path.CLOSEPOLY,
        ]
        path = Path(verts, codes)
        patch = patches.PathPatch(path, lw=1)
        patches_li.append(patch)
    
    for patch in patches_li:
        ax.add_patch(patch)
    print(len(patches_li))
    ax.set_xlim(min(xdata), max(xdata))
    ax.set_ylim(min(ydata), max(ydata))
    ax.autoscale()
    plt.show()
    return ax