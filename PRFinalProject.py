
import sys
print(sys.version)

import numpy as np
print('Numpy version:', np.__version__)

import pandas as pd
print('Pandas version:', pd.__version__)

import matplotlib as mpl
import matplotlib.pyplot as plt
print('Matplotlib version:', mpl.__version__)

import seaborn as sns
print('Seaborn version:', sns.__version__)

import datetime
import time
import multiprocessing as mp
import psutil


def duration_to_minutes(s):
    """
    Function that takes a string with the hh:mm:ss format and
    returns the integer equivalent of the total time in minutes,
    or zero for missing values in a Pandas dataframe.
    >>> s='03:44:32'
    >>> duration_to_minutes(s)
    224.53333333333333
    """
    if pd.isnull(s):
        val = 0 #note: this fills with 0 the 38 instances with null (missing) values
    else:
        hms = s.split(':')
        val = int(hms[0])*60 + int(hms[1]) + int(hms[2])/60.0
    return val



from matplotlib.offsetbox import (OffsetImage, AnnotationBbox) #Create image box
from matplotlib._png import read_png #Load png file


def thousands_comma(x, pos):
    """
    Arguments are the value and tick position.
    Returns number with thousands comma and with no decimals.
    """
    return '{:,.0f}'.format(x) #this is the new syntax for formatting

def thousands_format(x, pos):
    """
    Arguments are the value and tick position.
    Returns the number of thousands with one decimal, and K in lieu of 3 zeros.
    """
    return '{:.0f}{}'.format(x * 1e-3, 'K') #old syntax: '%1.0fK' % (x * 1e-3)

def millions_format(x, pos):
    """
    Arguments are the value and tick position.
    Returns number of millions with one decimal, and M in lieu of 6 zeros.
    """
    return '{:.1f}{}'.format(x * 1e-6, 'M')

def millions_currency(x, pos):
    """
    Arguments are the value and tick position.
    Returns number of millions with a $ sign, M in lieu of 6 zeros, and no decimals.
    >>> millions_currency(63457366276, 1)
    '$63457M'
    """
    return '{}{:.0f}{}'.format('$', x * 1e-6, 'M')

def add_event_icon(path,xy, xybox_arg):
    """
    Arguments are the image path,xy, position from xy to lower left corner of box.
    Returns Annotation box to plot the image in the plot.

    >>> annotation_box = add_event_icon('icons/Snow-48.png',['2015-01-27', 25000],(22., 10.))
    >>> annotation_box.axes==1
    False
    """
    #Add icon to indicate Christmas on the plot:
    img = read_png(path)
    imagebox = OffsetImage(img, zoom=0.6)
    ab = AnnotationBbox(imagebox, xy, xybox=xybox_arg, xycoords='data', boxcoords='offset points', pad=0.1, frameon=False)

    return ab

def is_peak_hour(x):
    """
    Function that takes an array(x) with two integers representing
    hour of the day and weekday, respectively, and
    returns 1 if it's peak hour as defined, 0 otherwise.
    >>> x=[7,3,9,16,17,18]
    >>> is_peak_hour(x)
    1
    """
    return 1 if x[0] in (7,8,9,16,17,18) and x[1] < 5 else 0 #total peak hour periods = 6h

def dateParser(s):
    """
    Function that takes a string in the format yyyy-mm-dd hh:mm:ss, and
    returns the same as a datetime object.
    >>> dateParser('2018-07-07 10:30:15')
    datetime.datetime(2018, 7, 7, 10, 0)
    """
    return datetime.datetime(int(s[0:4]), int(s[5:7]), int(s[8:10]), int(s[11:13]))
