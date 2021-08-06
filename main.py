
import numpy as np
import functions_general  as fg


def changepoint_detection(mat):



def changepoint_detection_master(mat):
    num_rows, num_cols = mat.shape
    final_output = [changepoint_detection(mat[x,y]) for x in range(num_rows) for y in range(num_cols) if x != y]
    return final_output



# ALGORITHM 1


# ALGORITHM 2





