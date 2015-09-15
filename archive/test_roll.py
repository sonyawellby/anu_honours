"""
Test roll
"""
import numpy as np

from hadisst_prepare import sst_January as dataset

test = np.roll(dataset,1,axis=2)


