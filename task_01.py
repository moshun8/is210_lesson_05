#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Defining a Function"""


def bool_to_str(bvalue, short=False):
    """Changes True/False to strings Y/N or Yes/No"""
    while short:
        if bvalue is True:
            return "Y"
        else:
            return "N"
            break
    else:
        if bvalue is True:
            return "Yes"
        else:
            return "No"