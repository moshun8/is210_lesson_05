#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Defining a Function"""

def bool_to_str(bvalue, short = False):
    while short:
        if bvalue == True:
            return "Y"
        else:
            return "N"
    else:
        if bvalue == True:
            return "Yes"
        else:
            return "No"       
print bool_to_str(False) 

    