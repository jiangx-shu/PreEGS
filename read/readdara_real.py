import networkx as nx


def readdata(path1, path2):
    G1 = nx.DiGraph()
    G2 = nx.DiGraph()

    with open(path1) as file:
        for line in file:
            data = line[:-1].split(' ')
            G1.add_edge(data[0], data[1])

    with open(path2) as file:
        for line in file:
            data = line[:-1].split(' ')
            G2.add_edge(data[0], data[1])
    return G1, G2


if __name__ == '__main__':
    G1, G2 = readdata('/Users/jiaxinlee/Desktop/research/realdata/nhaedges.txt','/Users/jiaxinlee/Desktop/research/realdata/sknshedges.txt')
    # print (G1.degree())
