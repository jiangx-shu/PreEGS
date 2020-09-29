import networkx as nx
import math

#from features import readdata

def cal_cc(G1,G2):
    result1 = dict()
    result2 = dict()
    result = dict()


    result1 = nx.closeness_centrality(G1)
    result2 = nx.closeness_centrality(G2)


    for x in result1:
        if (x not in result1):
            result1[x] = 0
        if (x not in result2):
            result2[x] = 0
        result[x] = math.fabs(result2[x] - result1[x])

    return result

#
