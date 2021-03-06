import networkx as nx
#from features import readdata
import math

def cal_cco(G1, G2):
    result = dict()
    result1 = nx.clustering(G1)
    result2 = nx.clustering(G2)
    for x in result1:
        if (x not in result1):
            result1[x] = 0
        if (x not in result2):
            result2[x] = 0
        result[x] = math.fabs(result2[x] - result1[x])

    return result


# if __name__ == '__main__':
#     G = readdata.readdata("/Users/jiaxinlee/Desktop/research/second experiment/features/input.txt")
#     print(cal_cco(G))
