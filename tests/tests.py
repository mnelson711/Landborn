import pytest
import matplotlib.pyplot as plt
import matplotlib.testing.compare as plt_compare
import numpy as np
import pandas as pd
from landborn import lineplot, scatterplot, barplot


def test_lineplot():
    # Create a DataFrame for testing
    x = [1, 2, 3, 4, 5]
    y = [10, 15, 7, 10, 5]

    lineplot(None,x,y, color='b')
    plot_path = "tests_images/test_lineplot.png"  # Save the plot in a temporary directory
    plt.savefig(plot_path)
    reference_plot_path = "tests_images/test_lineplot_confirmed.png"

    # Assert that the produced plot matches the reference plot
    with open(plot_path, "rb") as plot_file, open(reference_plot_path, "rb") as reference_file:
        assert plot_file.read() == reference_file.read(), "Produced plot differs from reference plot"

def test_barplot():
    # Create a DataFrame for testing
    np.random.seed(123)
    df = pd.DataFrame({
        'data values': np.random.normal(5, 1, 100),
        'categories': np.random.choice(['a', 'b', 'c'], replace=True, size=100)
    })

    barplot.barplot(df, 'categories', 'data values', orientation='vertical', color='b')
    plot_path = "tests_images/test_barplot_vert.png"  # Save the plot in a temporary directory
    plt.savefig(plot_path)
    reference_plot_path = "tests_images/test_barplot_vert_confirmed.png"

    # Assert that the produced plot matches the reference plot
    with open(plot_path, "rb") as plot_file, open(reference_plot_path, "rb") as reference_file:
        assert plot_file.read() == reference_file.read(), "Produced plot differs from reference plot"
        

def test_scatterplot():
    # Create a DataFrame for testing
    x = [1, 2, 3, 4, 5]
    y = [10, 15, 7, 10, 5]

    scatterplot.scatterplot(None,x,y, color='b')
    plot_path = "tests_images/test_scatterplot.png"  # Save the plot in a temporary directory
    plt.savefig(plot_path)
    reference_plot_path = "tests_images/test_scatterplot_confirmed.png"

    # Assert that the produced plot matches the reference plot
    with open(plot_path, "rb") as plot_file, open(reference_plot_path, "rb") as reference_file:
        assert plot_file.read() == reference_file.read(), "Produced plot differs from reference plot"