import numpy as np
import functions_general as fg


# INPUTS:
# X = input matrix. Currently working with each row is a given node
# t = time at which you are seeing if left and right sides show different covariance (give as column number)
def covariance_estimator_numerator(vector_A, vector_B, t, frequency, bandwidth):
    X = np.vstack([vector_A, vector_B])
    X_transpose = np.matrix.transpose(X)
    numerator_vector = np.zeros(vector_A.shape)
    for i in range(numerator_vector.shape[0]):
        time = fg.time_convert(i, frequency)
        kh_a = (time - t)
        numerator_vector[i] = (fg.kh_function(kh_a, bandwidth)
                               * np.dot(X[:, i], X_transpose[i, :]))
    numerator = np.sum(numerator_vector)
    return numerator


def covariance_estimator_denominator(t, length, frequency, bandwidth):
    denominator_vector = np.zeros(length)
    for i in range(denominator_vector.shape[0]):
        time = fg.time_convert(i, frequency)
        kh_a = (time - t)
        denominator_vector[i] = fg.kh_function(kh_a, bandwidth)
    denominator = np.sum(denominator_vector)
    return denominator


def covariance_estimator(vector_A, vector_B, t, frequency, bandwidth):
    numerator = covariance_estimator_numerator(vector_A, vector_B, t, frequency, bandwidth)
    denominator = covariance_estimator_denominator(t, vector_A.shape[0], frequency, bandwidth)
    covariance_t = numerator / denominator
    return covariance_t


def covariance_matrix(fldat, frequency, bandwidth):
    cov_matrix = np.zeros([fldat.shape[0], fldat.shape[0]])
    for i in range(fldat.shape[0]):  # for each column
        vector_A = fldat[i, :]
        for j in range(fldat.shape[0]):
            vector_B = fldat[j, :]
            for k in range(fldat.shape[1]):  # for each timepoint
                t = fg.time_convert(k, frequency)
                cov = covariance_estimator(vector_A, vector_B, t, frequency, bandwidth)
                cov_matrix[i, j] = cov
                cov_matrix[j, i] = cov
    return cov_matrix
