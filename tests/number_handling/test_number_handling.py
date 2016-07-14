
"""
Python model test-models/tests/number_handling/test_number_handling.py
Translated using PySD version 0.5.1
"""
from __future__ import division
import numpy as np
<<<<<<< HEAD
=======
from pysd import utils
import xarray as xr
>>>>>>> 25bd4206de9f5719aad5a04a2320edc93351758a

from pysd.functions import cache
from pysd import functions

_subscript_dict = {}

_namespace = {
    'INITIAL TIME': 'initial_time',
    'equality': 'equality',
    'quotient target': 'quotient_target',
    'TIME STEP': 'time_step',
    'denominator': 'denominator',
    'numerator': 'numerator',
    'FINAL TIME': 'final_time',
    'SAVEPER': 'saveper',
    'quotient': 'quotient'}


@cache('step')
def equality():
    """
    equality
    --------
    (equality)


<<<<<<< HEAD

=======
>>>>>>> 25bd4206de9f5719aad5a04a2320edc93351758a
    """
    return functions.if_then_else(quotient() == quotient_target(), 1, 0)


@cache('run')
def final_time():
    """
    FINAL TIME
    ----------
    (final_time)
    Month
<<<<<<< HEAD

=======
>>>>>>> 25bd4206de9f5719aad5a04a2320edc93351758a
    The final time for the simulation.
    """
    return 1


@cache('run')
def denominator():
    """
    denominator
    -----------
    (denominator)


<<<<<<< HEAD

=======
>>>>>>> 25bd4206de9f5719aad5a04a2320edc93351758a
    """
    return 4


@cache('run')
def numerator():
    """
    numerator
    ---------
    (numerator)


<<<<<<< HEAD

=======
>>>>>>> 25bd4206de9f5719aad5a04a2320edc93351758a
    """
    return 3


@cache('step')
def saveper():
    """
    SAVEPER
    -------
    (saveper)
    Month [0,?]
<<<<<<< HEAD

=======
>>>>>>> 25bd4206de9f5719aad5a04a2320edc93351758a
    The frequency with which output is stored.
    """
    return time_step()


@cache('run')
def initial_time():
    """
    INITIAL TIME
    ------------
    (initial_time)
    Month
<<<<<<< HEAD

=======
>>>>>>> 25bd4206de9f5719aad5a04a2320edc93351758a
    The initial time for the simulation.
    """
    return 0


@cache('run')
def time_step():
    """
    TIME STEP
    ---------
    (time_step)
    Month [0,?]
<<<<<<< HEAD

=======
>>>>>>> 25bd4206de9f5719aad5a04a2320edc93351758a
    The time step for the simulation.
    """
    return 1


@cache('run')
def quotient_target():
    """
    quotient target
    ---------------
    (quotient_target)


<<<<<<< HEAD

=======
>>>>>>> 25bd4206de9f5719aad5a04a2320edc93351758a
    """
    return 0.75


@cache('step')
def quotient():
    """
    quotient
    --------
    (quotient)


<<<<<<< HEAD

=======
>>>>>>> 25bd4206de9f5719aad5a04a2320edc93351758a
    """
    return numerator() / denominator()


def time():
    return _t
functions.time = time
functions.initial_time = initial_time
