## Reference
## https://github.com/Unidata/MetPy
#Made changes in the function inputs and expected output and more assertions

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pytest

from metpy.testing import assert_array_almost_equal, assert_array_equal, assert_nan
from metpy.units import *
from metpy.units import (check_units, concatenate, 
                         pandas_dataframe_to_unit_arrays, units)

def test_value_unit_concatenation():
    #Test to check if the unit attached to an array is proper for cocatenation.
    result = concatenate((67.8 * units.inches, 78.5*units.inches))
    result1= concatenate((35 , 50 *units.inches))
    assert_array_equal(result, np.array([67.8, 78.5]) * units.inches)
    assert not isinstance(result.m, np.ma.MaskedArray)
    assert_array_equal(result1, np.array([35, 50]) * units.inches)
    assert not isinstance(result1.m, np.ma.MaskedArray)