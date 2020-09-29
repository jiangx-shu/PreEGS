#from features import readdata
import networkx as nx
import math


def cal_bc(G1,G2):
    result = dict()
    result1 = nx.betweenness_centrality(G1)
    result2 = nx.betweenness_centrality(G2)
    for x in result1:
        if (x not in result1):
            result1[x] = 0
        if (x not in result2):
            result2[x] = 0
        result[x] = math.fabs(result1[x])
    return result


#if __name__ == '__main__':
    #G = readdata.readdata("/Users/jiaxinlee/Desktop/research/second experiment/features/input.txt")
    #print(cal_bc(G))
