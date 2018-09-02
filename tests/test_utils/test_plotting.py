# -*- coding: utf-8 -*-
"""Test the plotting functions in mypack
"""
import os

import matplotlib.pyplot as plt
import numpy as np

import mypack.utils.io as my_io
from mypack.utils.plotting import plot_airfoil


def test_plot_airfoil():
    """Check the correct data is plotter to the figure
    """
    # given
    mod_path = os.path.dirname(os.path.abspath(__file__))
    air_path = os.path.join(mod_path, 'files', 'demo_selig.dat')
    air_df = my_io.read_selig(air_path)
    fig, ax = plt.subplots()
    # when
    plot_airfoil(air_df)
    x_plot, y_plot = ax.lines[0].get_xydata().T
    # then
    np.testing.assert_array_equal(x_plot, air_df.x)
    np.testing.assert_array_equal(y_plot, air_df.y)
