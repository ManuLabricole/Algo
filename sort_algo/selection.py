from .utils import swap


def selectionSort(A):
    """
    on cherche l'element qui doit se placer a l'i_eme place
    """
    # print(f"Before = {A}")
    for i in range(len(A)-1):
        # print(f"---> {i}")
        mini = i
        for j in range(i+1, len(A)):
            # print(f"------> {j}")
            if A[j] < A[mini]:
                # print(f"FOUND ==> {A[j]} plus petit que {A[i]}")
                mini = j
        if i != mini:
            # print("SWAPING")
            swap(A, i, mini)
            # print(A)
    # print(f"After = {A}")
