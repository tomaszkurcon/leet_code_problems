def findRelativeRanks(score):
    my_dict = {}
    def partition(A, p, r):
        x = A[r]
        i = p - 1
        for j in range(p, r):
            if A[j] >= x:
                i += 1
                A[j], A[i] = A[i], A[j]
        A[r], A[i + 1] = A[i + 1], A[r]
        return i+1

    def quick_select(A, k, p, r):
        q = partition(A, p, r)
        if q == k:
            return A[q]
        if q < k:
            return quick_select(A, k, q + 1, r)
        else:
            return quick_select(A, k, p, q - 1)

    n = len(score)
    score_copy = score.copy()
    res = ["" for _ in range(n)]
    medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
    for i in range(n):
        my_dict[quick_select(score_copy, i, 0, n - 1)] = i
    for i in range(n):
        place = my_dict.get(score[i])
        if place < 3:
            res[i]=medals[place]
        else:
            res[i] = str(place+1)


def findRelativeRanks2(score):
    n = len(score)
    score_copy = [(score[i], i) for i in range(n)]
    def partition(A, p, r):
        x = A[r][0]
        i = p-1
        for j in range(p,r):
            if(A[j][0]>=x):
                i+=1
                A[i], A[j] = A[j], A[i]
        A[i+1], A[r] = A[r], A[i+1]
        return i+1
    def quickSort(A, p, r):
        while p < r:
            q = partition(A, p, r)
            quickSort(A, p, q-1)
            p=q+1
    quickSort(score_copy, 0, n-1)
    medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
    result = [""]*n
    for i in range(n):
        index = score_copy[i][1]
        if i < 3:
            result[index] = medals[i]
        else:
            result[index]=str(i+1)
    return result
findRelativeRanks2([10,3,8,9,4])