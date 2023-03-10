def merge_sort(A):
    """
    l'intelligence se trouve dans la fusion des tableaux
    """
    print(A)
    merge_sort_r(A, 0, len(A))
    print(A)


def merge_sort_r(A, start, end):
    if start < end-1:
        m = int((start+end)/2)
        merge_sort_r(A, start, m)
        merge_sort_r(A, m, end)
        merge(A, start, m, end)


def merge(A, start, middle, end):
    temp = A.copy()
    i = start
    j = middle

    for k in range(start, end):
        if i < middle and j < end:
            if A[i] <= A[j]:
                temp[k] = A[i]
                i += 1
            else:
                temp[k] = A[j]
                j += 1
        else:
            if i < middle:
                temp[k] = A[i]
            else:
                temp[k] = A[j]
    for k in range(start, end):
        A[k] = temp[k]
