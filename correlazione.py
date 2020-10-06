import numpy
from scipy.stats import pearsonr


svm1 = [9.943, -6.290, 3.725, 2.142, 4.855, -2.843, -1.639, 10.333]
lr1 = [0.000, 0.180, 0.649, 0.378, 0.355, 0.344, 2.891, 1.049]
corr1 = pearsonr(svm1, lr1)[0]
print(corr1)

svm2 = [7.536, 17.629, 45.690, 7.550, 9.709, 19.677, 0.073, 1.663, 39.747, 15.369, 33.294, 8.228, 19.824, 7.266, 27.151, 37.588, 14.184, 1.465, 43.081,
        4.833, 77.081, -34.363, 0.594, -59.852]
lr2 = [-66.137, -77.336, -70.905, -56.873, 36.775, -62.386, -62.847, -45.445, 247.539, -67.169, -76.030, -69.079, -60.919, 36.418, -63.766, -70.249, -64.280,
       -79.514, -75.942, -1.457, -1.427, 1.423, -0.003, 77.715]

corr2 = pearsonr(svm2, lr2)[0]
print(corr2)