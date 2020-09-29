#from features import readdata
import networkx as nx
def cal_dc(G1,G2):
    result1 = dict()
    result2 = dict()
    result = dict()
    for x in G1.nodes:
        result1[x] = G1.degree(x)

    for x in G2.nodes:
        result2[x] = G2.degree(x)

    for x in result1:
        if (x not in result1):
            result1[x] = 0
        if (x not in result2):
            result2[x] = 0
        result[x] = abs(result1[x])

    return result

# if __name__ == '__main__':
#     G = readdata.readdata("/Users/jiaxinlee/Desktop/research/second experiment/features/input.txt")
#     print(cal_dc(G))
