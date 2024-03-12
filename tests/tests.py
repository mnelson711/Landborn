import pytest
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# from landborn import lineplot as lineplot
# from landborn import scatterplot as scatterplot
# from landborn import barplot as barplot
import landborn
# from '../landborn/lineplot' import lineplot


def test_lineplot():
    x = [1, 2, 3, 4, 5]
    y = [10, 15, 7, 10, 5]

    landborn.lineplot(None,x,y, color='b')
    plot_path = "tests_images/test_lineplot.png"
    plt.savefig(plot_path)
    reference_plot_path = "tests_images/test_lineplot_confirmed.png"

    with open(plot_path, "rb") as plot_file, open(reference_plot_path, "rb") as reference_file:
        assert plot_file.read() == reference_file.read(), "Produced plot differs from reference plot"

def test_barplot():
    np.random.seed(123)
    df = pd.DataFrame({
        'data values': np.random.normal(5, 1, 100),
        'categories': np.random.choice(['a', 'b', 'c'], replace=True, size=100)
    })
    #testing vertical
    landborn.barplot(df, 'categories', 'data values', orientation='vertical', color='b')
    plot_path = "tests_images/test_barplot_vert.png"
    plt.savefig(plot_path)
    reference_plot_path = "tests_images/test_barplot_vert_confirmed.png"

    with open(plot_path, "rb") as plot_file, open(reference_plot_path, "rb") as reference_file:
        assert plot_file.read() == reference_file.read(), "Produced plot differs from reference plot"
        
    #testing horizontal
    landborn.barplot(df, 'data values', 'categories', orientation='horizontal', color='b')
    plot_path = "tests_images/test_barplot_hor.png"
    plt.savefig(plot_path)
    reference_plot_path = "tests_images/test_barplot_hor_confirmed.png"

    with open(plot_path, "rb") as plot_file, open(reference_plot_path, "rb") as reference_file:
        assert plot_file.read() == reference_file.read(), "Produced plot differs from reference plot"
        

def test_scatterplot():
    x = [1, 2, 3, 4, 5]
    y = [10, 15, 7, 10, 5]

    landborn.scatterplot(None,x,y, color='b')
    plot_path = "tests_images/test_scatterplot.png"
    plt.savefig(plot_path)
    reference_plot_path = "tests_images/test_scatterplot_confirmed.png"

    with open(plot_path, "rb") as plot_file, open(reference_plot_path, "rb") as reference_file:
        assert plot_file.read() == reference_file.read(), "Produced plot differs from reference plot"
        
        
def test_jointplot():
    x = [1, 2, 3, 4, 5]
    y = [10, 15, 7, 10, 5]

    landborn.jointplot(x, y, color='blue')
    plot_path = "tests_images/test_jointplot.png"
    plt.savefig(plot_path)
    reference_plot_path = "tests_images/test_jointplot_confirmed.png"

    with open(plot_path, "rb") as plot_file, open(reference_plot_path, "rb") as reference_file:
        assert plot_file.read() == reference_file.read(), "Produced plot differs from reference plot"
        
def test_swarmplot():
    np.random.seed(120)
    data = pd.DataFrame({
    'Category': ['A']*80 + ['B']*80 + ['C']*80,
    'Value': np.concatenate([np.random.randint(0, 20, size=80), np.random.randint(20, 30, size=80), np.random.randint(30, 50, size=80)])
    })
    landborn.swarmplot(data, 'Category', 'Value', r=0.8)
    plot_path = "tests_images/test_swarmplot.png"
    plt.savefig(plot_path)
    reference_plot_path = "tests_images/test_swarmplot_confirmed.png"

    with open(plot_path, "rb") as plot_file, open(reference_plot_path, "rb") as reference_file:
        assert plot_file.read() == reference_file.read(), "Produced plot differs from reference plot"
        

#Tests for Colormaps

def test_plot_colormap_gradient():
    landborn.plot_colormap_gradient('viridis')
    plot_path = "tests_images/test_gradient.png"
    plt.savefig(plot_path)
    reference_plot_path = "tests_images/test_gradient_confirmed.png"

    with open(plot_path, "rb") as plot_file, open(reference_plot_path, "rb") as reference_file:
        assert plot_file.read() == reference_file.read(), "Produced plot differs from reference plot"
        
def test_plot_colormap_in_rgb_space():
    landborn.plot_colormap_in_rgb_space('viridis')
    plot_path = "tests_images/test_rgb_plot.png"
    plt.savefig(plot_path)
    reference_plot_path = "tests_images/test_rgb_plot_confirmed.png"

    with open(plot_path, "rb") as plot_file, open(reference_plot_path, "rb") as reference_file:
        assert plot_file.read() == reference_file.read(), "Produced plot differs from reference plot"

def test_create_custom_colormap():
    my_colormap = landborn.create_custom_colormap(title="Test Colormap")
    landborn.plot_colormap_gradient(my_colormap)
    plot_path = "tests_images/test_custom_colormap.png"
    plt.savefig(plot_path)
    reference_plot_path = "tests_images/test_custom_colormap_confirmed.png"

    with open(plot_path, "rb") as plot_file, open(reference_plot_path, "rb") as reference_file:
        assert plot_file.read() == reference_file.read(), "Produced plot differs from reference plot"

def test_delta_e():
    landborn.delta_e('viridis')
    plot_path = "tests_images/test_delta_e.png"
    plt.savefig(plot_path)
    reference_plot_path = "tests_images/test_delta_e_confirmed.png"

    with open(plot_path, "rb") as plot_file, open(reference_plot_path, "rb") as reference_file:
        assert plot_file.read() == reference_file.read(), "Produced plot differs from reference plot"


def test_delta_e_lightness():
    landborn.delta_e_lightness('viridis')
    plot_path = "tests_images/test_delta_e_lightness.png"
    plt.savefig(plot_path)
    reference_plot_path = "tests_images/test_delta_e_lightness_confirmed.png"

    with open(plot_path, "rb") as plot_file, open(reference_plot_path, "rb") as reference_file:
        assert plot_file.read() == reference_file.read(), "Produced plot differs from reference plot"

def test_convert_colormap_for_colorblindness():
    colorblind = landborn.convert_colormap_for_colorblindness('viridis')
    landborn.plot_colormap_gradient(colorblind)
    plot_path = "tests_images/test_colorblind.png"
    plt.savefig(plot_path)
    reference_plot_path = "tests_images/test_colorblind_confirmed.png"

    with open(plot_path, "rb") as plot_file, open(reference_plot_path, "rb") as reference_file:
        assert plot_file.read() == reference_file.read(), "Produced plot differs from reference plot"
        
def test_compare_colormaps():
    landborn.compare_colormaps('viridis', 'rainbow')
    plot_path = "tests_images/test_compare_colormaps.png"
    plt.savefig(plot_path)
    reference_plot_path = "tests_images/test_compare_colormaps_confirmed.png"

    with open(plot_path, "rb") as plot_file, open(reference_plot_path, "rb") as reference_file:
        assert plot_file.read() == reference_file.read(), "Produced plot differs from reference plot"