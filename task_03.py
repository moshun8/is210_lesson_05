#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Transforming Data"""


def celsius_to_fahrenheit(temperature):
    """convert C to F"""
    c = temperature
    f = (c * 9) / 5 + 32
    return float(f)


def fahrenheit_to_celsius(temperature):
    """convert F to C"""
    f = temperature
    c = 5 * (f - 32) / 9
    return float(c)


def convert_temperature(temperature, output_format='c'):
    """convert temps"""
    degree_type = temperature[-1].lower()
    temp = float(temperature[:-1])

    if output_format == 'f':
        if degree_type == 'c':
            return celsius_to_fahrenheit(temp)
        elif degree_type == 'f':
            return temp
        else:
            return None
    elif output_format == 'c':
        if degree_type == 'f':
            return fahrenheit_to_celsius(temp)
        elif degree_type == 'c':
            return temp
    else:
        return None