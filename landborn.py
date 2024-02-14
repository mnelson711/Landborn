import matplotlib.pyplot as plt
import matplotlib.lines as mlines

def test(word):
    print(word + str(5))

def lineplot(df, x=[], y=[],style='-', color='k', save_path=None):
    if ax is None:
        fig, ax = plt.subplots()

    if isinstance(x, str) and df is not None:
        xdata = df[x]
    else:
        xdata = x
    if isinstance(y, str):
        ydata = df[y]
    else:
        ydata = y

    line = mlines.Line2D(xdata, ydata, color=color, linestyle=style, marker=marker, markersize=size)
    ax.add_line(line)
    ax.autoscale()
    
    if save_path:
        plt.savefig(save_path)

    return ax