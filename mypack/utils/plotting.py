# -*- coding: utf-8 -*-
"""Plotting data
"""
import matplotlib.pyplot as plt


def plot_airfoil(air_df):
    """Plot an airfoil

    Parameters
    -----------
    air_df : pd.Dataframe
        Pandas Dataframe containing x- and y-coordinates of airfoil data.
    """
    line, = plt.plot(air_df.x, air_df.y)
    plt.axis('equal')
    return line
