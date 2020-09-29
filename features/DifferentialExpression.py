from scipy import stats
import numpy as np

def cal_de(dict1,dict2):
    v1 = np.array(dict1)
    v2 = np.array(dict2)
    return stats.ttest_ind(v1,v2).pvalue
