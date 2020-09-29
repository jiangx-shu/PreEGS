import networkx as nx


def readdata(path1, path2):
    G1 = nx.Graph()
    G2 = nx.Graph()

    mat = []
    with open(path1) as file:
        for line in file:
            data = line[:-1].split(',')
            mat.append(data)
    for i in range(0, 100):
        for j in range(0, 100):
            if (mat[i][j] != '0'):
                G1.add_edge(i + 1, j + 1)

    mat = []
    with open(path2) as file:
        for line in file:
            data = line[:-1].split(',')
            mat.append(data)
    for i in range(0, 100):
        for j in range(0, 100):
            if (mat[i][j] != '0'):
                G2.add_edge(i + 1, j + 1)
    return G1, G2


if __name__ == '__main__':
    G1, G2 = readdata(
        "/Users/jiaxinlee/Desktop/research/different parameter/rho_0.1-0.5_repeat_10/rho_0.1_1/matrix1.txt",
        '/Users/jiaxinlee/Desktop/research/different parameter/rho_0.1-0.5_repeat_10/rho_0.1_1/matrix1.txt')
    # print (G1.degree())
