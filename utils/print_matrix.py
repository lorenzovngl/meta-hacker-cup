def print_matrix(m):
    print("", end="\t")
    for i in range(len(m)):
        print("[{}]".format(i), end='\t')
    print()
    for i in range(len(m)):
        print("[{}]".format(i), end='\t')
        for j in range(len(m[i])):
            print(m[i][j], end='\t')
        print()