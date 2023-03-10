def quick_sort(A):
    iteration = 0
    print(A)
    quick_sort_r(A, 0, len(A)-1, iteration)
    print(A)


def quick_sort_r(A, first, last, iteration):
    # print(f"Called recursive with : {A} - first --> {first} <-- last --> {last} <-- ")
    #print(f"Iteration n° {iteration}")
    iteration += 1
    # On compare les indices envoyé
    # En premier lieu, les indices recus sont 0 et len()-a
    # Si len()-1 = 0 on a donc une liste de taille 1 et il n'y a rien a faire

    if first < last:
        # Si mes indices et j verifient i < j
        #

        pivot = partition(A, first, last)
        quick_sort_r(A, first, pivot-1, iteration)
        quick_sort_r(A, pivot+1, last, iteration)
    # else:
        # print(f"{last} < {first}")


def partition(A, first, last):
    # Apres avoir validé : i < j
    # On calcule le pivot
    pivot = A[first]
    # print(f"The pivot is --> {pivot} <--")
    i = first
    j = last

    # Je balaye a partir de mon pivot car au debut i = first et pivot = A[first]
    while i <= j:
        # Si l'indice a[i] est inferieur au pivot, il est a la bonne place ie, entre l'indice du pivot et i
        if A[i] <= pivot:
            i += 1
        else:
            # Mais s'il est plus grand, sont indices devrait etre entre i et j, on le change bde place
            # Si a[j] > pivot, il est la bonne place
            # On peut donc le laisser ici, ocnsierer que c'est ok
            # On reduit j pour rapprocher de i et finir l algo
            if A[j] > pivot:
                j -= 1
            else:
                A[i], A[j] = A[j], A[i]
    # Maintenant qu'on a classer tout les < pivot entre pivot et i
    # Tous les > p entre i et +
    # Il faut positioner le pivot entre ces deux partitions
    # Note : J dimininue si > stric. Donc au dela de j on est ok. = a j on est plus petit

    A[first], A[j] = A[j], A[first]
    # print(f"----> The new table after sorting around pivot {pivot} --> {A}")
    return j
