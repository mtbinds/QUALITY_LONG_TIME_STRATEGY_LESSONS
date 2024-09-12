# import math
# import numpy as np
# import matplotlib.pyplot as plt


# def calcul_integrale(y):
#     print(y)
#     x     = x1
#     aire  = 0
#     while x <= x2:
#         y           = y
#         petite_aire = y*dx
#         aire        = aire + petite_aire
#         x           = x + dx

#     print(aire)

# x1      = 1
# x2      = 31
# dx      = abs(x2-x1)/10000

import math
from scipy.stats import rankdata

def auc_u_test(vec, len_A, len_B):
  rank_value = rankdata(vec)
  rank_sum = sum(rank_value[0:len_A])
  u_value = rank_sum - (len_A*(len_A+1))/2
  auc = u_value / (len_A * len_B)
  if auc < 0.50:
    auc = 1.0 - auc
  return(auc)