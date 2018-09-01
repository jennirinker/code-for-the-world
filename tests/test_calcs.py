# -*- coding: utf-8 -*-
"""Test the calculation functions in mypack
"""
from mypack.calcs import get_lift
import numpy as np
import pandas as pd


def test_get_lift():
    """Check that the lift force is calculated correctly
    """
    # given
    h = 0.4
    rho = 1.3
    wsp = 4
    air_df = pd.DataFrame([[1, 0], [0.5, h/2],
                           [0, 0], [0.5, -h/2]],
                          columns=['x', 'y'])
    exp_lift_force = 0.5 * 0.2 * rho * wsp**2 * h  # h is area here
    # when
    calc_lift_force = get_lift(air_df, wsp, rho=rho)
    # then
    np.testing.assert_equal(exp_lift_force, calc_lift_force)
