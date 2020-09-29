def cal_ddc(G1,G2):
    max1 = 0
    max2 = 0
    result1 = dict()
    result2 = dict()
    result = dict()
    for x in G1.nodes:
        result1[x] = G1.degree(x)
        max1 = max(result1[x],max1)

    for x in G2.nodes:
        result2[x] = G2.degree(x)
        max2 = max(result2[x], max2)

    for x in result1:
        if (x not in result1):
            result1[x] = 0
        if (x not in result2):
            result2[x] = 0
        result[x] = float(result1[x])/float(max1)

    return result
