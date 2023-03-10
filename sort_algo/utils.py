def is_sorted(A: list) -> bool:
    is_sorted = True
    for i in range(0, len(A)-1):
        if not A[i+1] > A[i]:
            is_sorted = False
    return is_sorted


def swap(A, i, j):
    # Store in multivariable assignement
    #print(f"Swap {A[i]} with {A[j]}")
    # print(A)
    A[i], A[j] = A[j], A[i]
    # print(A)
