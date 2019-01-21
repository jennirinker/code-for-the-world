# -*- coding: utf-8 -*-
"""Calculations with airfoils
"""


def get_lift(air_df, wsp, rho=1.225):
    """Determine the lift of an airfoil

    Parameters
    -----------
    air_df : pd.Dataframe
        Pandas Dataframe containing x- and y-coordinates of airfoil data.
    wsp : int, float
        Velocity of air..
    rho : int, float
        Density of air.
    """
    c_l = 0.2  # life coefficeint, this is made-up
    area = (air_df.x.max() - air_df.x.min()) * \
           (air_df.y.max() - air_df.y.min())  # also made up
    lift_force = 0.5 * c_l * rho * wsp**2 * area  # equation for lift force
    return lift_force
