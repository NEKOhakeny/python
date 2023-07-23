class hamming:
    def calc(A,B):
        distCnt = 0
        lengA = len(A)
        lengB = len(B)
        if lengB >= lengA:
            size = lengA
        else:
            size = lengB
        for n in range(size):
            if A[n] != B[n]:
                distCnt += 1
        return distCnt