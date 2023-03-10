def insertionSort(A):
    """
    on cherche la place ou va etre positionne l'i_eme element 
    """
    # print(f"Input = {A}")
    for i in range(1, len(A)):
        # print(f"---> i = {i}")
        x = A[i]
        j = i

        while (j > 0 and A[j-1] > x):
            # print(f"------> j = {j}")
            # print(f"Avant swap = {A}")
            #swap(A, j, j-1)
            A[j] = A[j-1]
            j -= 1
            # print(f"Apres swap = {A}")

        A[j] = x
    # print(f"After : {A}")
