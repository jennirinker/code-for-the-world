# -*- coding: utf-8 -*-
"""Test the IO functions in mypack

Author
------
Jenni Rinker
rink@dtu.dk
"""
import os

import mypack.utils.io as my_io
import pandas as pd


def test_read_selig():
    """Check that the selig airfoil is read correctly
    """
    # given
    mod_path = os.path.dirname(os.path.abspath(__file__))
    air_path = os.path.join(mod_path, 'files', 'demo_selig.dat')
    exp_df = pd.DataFrame([[1.000000, 0.001470],
                           [0.997390, 0.002100]],
                          columns=['x', 'y'])
    # when
    snip_df = my_io.read_selig(air_path).iloc[:2, :2]
    # then
    pd.testing.assert_frame_equal(exp_df, snip_df)
