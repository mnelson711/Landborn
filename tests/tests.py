import pytest
import matplotlib.pyplot as plt
import matplotlib.testing.compare as plt_compare
from landborn import lineplot, scatterplot

@pytest.fixture
def sample_data():
    # Generate sample data
    x = [1, 2, 3, 4, 5]
    y = [10, 15, 7, 10, 5]
    return x, y

# @pytest.mark.mpl_image_compare
# def test_barplot(sample_data):
#     x, y = sample_data
#     # Create bar plot
#     barplot(x, y)
#     # Save the plot
#     plt.savefig('test_barplot.png')
#     return plt.gcf()

@pytest.mark.mpl_image_compare
def test_lineplot(sample_data):
    x, y = sample_data
    # Create line plot
    lineplot.lineplot(None,x, y)
    # Save the plot
    plt.savefig('test_lineplot.png')
    assert plt.gcf()

@pytest.mark.mpl_image_compare
def test_scatterplot(sample_data):
    x, y = sample_data
    # Create scatter plot
    save_path = 'test_scatterplot.png'
    scatterplot.scatterplot(None,x, y, save_path=save_path)
    # Save the plot
    assert plt.gcf()
