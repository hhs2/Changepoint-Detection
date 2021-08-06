import numpy as np
import covariance_estimator as ce


fldat = np.array([[1, 2, 3], [1, 2, 3], [7, 8, 9],[10, 11, 12]])
frequency = 5
bandwidth = 1

#output = ce.covariance_matrix(fldat, frequency, bandwidth)
#print(output)

a = np.linalg.norm(fldat,ord=1)

print(a)


