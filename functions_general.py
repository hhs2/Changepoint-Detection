import numpy as np


# convert column number to time, 0 indexed
def time_convert(column_number, frequency):
    time_per_cycle = 1 / frequency
    time = column_number * time_per_cycle
    return time


def k_function(u):
    a = 1 if abs(u) <= 1 else 0
    K = 0.75 * (1 - (u ** 2)) * a
    return K


def kh_function(a, h):
    K = k_function(a/h) / h
    return K


def k_function_right(u):
    a = 1 if u > 0 else 0
    K_right = 2 * k_function(u) * a
    return K_right


def k_function_left(u):
    a = 1 if u < 0 else 0
    K_left = 2 * k_function(u) * a
    return K_left
