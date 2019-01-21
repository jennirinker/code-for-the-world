# -*- coding: utf-8 -*-
"""Loading/saving data
"""
import pandas as pd


def read_selig(path):
    """Read a Selig-style airfoil file

    Parameters
    -----------
    path : str
        Path to the Selig-stle .dat file.

    Returns
    -------
    air_df : pd.Dataframe
        Pandas Dataframe containing x- and y-coordinates of airfoil data.
    """
    air_df = pd.read_csv(path, delim_whitespace=True,
                         header=0)
    air_df.columns = ['x', 'y']
    return air_df
