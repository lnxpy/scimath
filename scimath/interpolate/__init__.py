# (C) Copyright 2005-2021 Enthought, Inc., Austin, TX
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD
# license included in LICENSE.txt and may be redistributed only under
# the conditions described in the aforementioned license. The license
# is also available online at http://www.enthought.com/licenses/BSD.txt
#
# Thanks for using Enthought open source!

""" Specialized interpolation methods for 1-D arrays, much faster than the
    standards linear interpolation in SciPy. Part of the SciMath project of
    the Enthought Tool Suite.
"""
from .interpolate import linear, block_average_above, window_average

from .fitting import DataFit, Spline, Linear, Logarithmic, BlockAverageAbove, \
    Block, EndAverage, WindowAverage, FillNaN
