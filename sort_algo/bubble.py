from .utils import swap


def bubbleSort(A):
    """
    les grands valeurs remontent aux derniers position du tableau
    comme des bulles d'air dans l'eau
    """
    #print(f"Before bubble : {A}")
    for i in range(len(A)-1, 0, -1):
        #print(f"Main loop --> {i}")
        for j in range(0, i):
            if A[j+1] <= A[j]:
                swap(A, j+1, j)
    #print(f"After bubble : {A}")
    # print(f"is_sorted => {is_sorted(A)}")
