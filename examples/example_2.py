# -*- coding: utf-8 -*-
"""Example 2: Calculate a lift force
"""
import os

from mypack.utils.io import read_selig
from mypack.calcs import get_lift


def example_2():
    """Run example 2"""

    # script inputs
    mod_path = os.path.dirname(os.path.abspath(__file__))  # current module
    air_path = os.path.join(mod_path, '..',
                            'tests', 'test_utils', 'files', 'demo_selig.dat')
    wsp = 10

    # load coordinates from a a selig-style airfoil file
    air_df = read_selig(air_path)

    # calculate the lift
    lift_force = get_lift(air_df, wsp)
    out_path = os.path.join(mod_path, 'example_2.out')
    with open(out_path, 'w') as f:
        f.write(f'The lift force at {wsp} m/s is {lift_force:.2f} N.')


if __name__ == '__main__':  # call function when run as script
    example_2()