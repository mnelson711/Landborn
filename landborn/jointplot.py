import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
import scatterplot as scatterplot
import lineplot as lineplot

def jointplot(x, y, kind='scatter', ax=None, color='black', title='Joint Plot', save_path=None):
    fig, axs = plt.subplots(2, 1, figsize=(10, 8), sharex=True) #create two plots

    #top line plot
    axs[0].set_title(title)
    axs[0].tick_params(axis='x',which='both', bottom=False,top=False,labelbottom=False)
    axs[0].spines['bottom'].set_visible(False)
    axs[0].spines['right'].set_visible(False)
    axs[0].spines['top'].set_visible(False)
    lineplot.lineplot(None,x,y, color=color, ax=axs[0])

    #bottom scatterplot
    axs[1].spines['top'].set_visible(False)
    axs[1].spines['right'].set_visible(False)
    axs[1].set_xlabel('X axis')
    scatterplot.scatterplot(None, x,y, color=color, ax=axs[1])
    
    if save_path:
        plt.savefig(save_path)



if __name__ == "__main__":
    x = [1, 2, 3, 4, 5]
    y = [10, 15, 7, 10, 5]
    
    ax = jointplot(x, y, color='blue',save_path="test_jointplot.png")