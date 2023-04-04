import numpy as np
global comps

def UnnaturalMergeSort(array, size):
    global comps
    # if size == 1 ,do nothing
    mergeFinal = np.array(array)

    if (size == 2):
        comps += 1
        if (mergeFinal[0] > mergeFinal[1]):
            temp = mergeFinal[1]
            mergeFinal[1] = mergeFinal[0]
            mergeFinal[0] = temp


    if (size > 2):

        sizeI = int(2 * size / 3)
        sizeII = int(size / 3)

        arr_first = np.array(mergeFinal[0: sizeI])
        arr_rec_first =  np.array(UnnaturalMergeSort(arr_first, arr_first.size))

        arr_last = np.array(mergeFinal[size-sizeI:size])
        arr_rec_last =  np.array(UnnaturalMergeSort(arr_last, arr_last.size))

        arr_fl = np.concatenate((mergeFinal[0:sizeII], array[size-sizeII:size]), axis=None)
        arr_rec_fl =  np.array(UnnaturalMergeSort(arr_fl, arr_fl.size))

        mergeFirst = np.array(mergesort(arr_rec_first, arr_rec_last, arr_rec_first.size, arr_rec_last.size))

        mergeFinal = mergesort(mergeFirst, arr_rec_fl, mergeFirst.size, arr_rec_fl.size)

    return mergeFinal


def mergesort(arrayI, arrayII, sizeI, sizeII):
    global comps
    merged = []
    j1 = j2 = 0

    while j1 < sizeI and j2 < sizeII:
        if arrayI[j1] == arrayII[j2]:
            merged.append(arrayII[j2])
            j1 += 1
            j2 += 1
            comps +=1
        elif arrayI[j1] > arrayII[j2]:
            merged.append(arrayII[j2])
            j2 += 1
            comps +=2
        else:
            merged.append(arrayI[j1])
            j1 += 1
            comps += 2

    # add rest of elements
    if j1 == sizeI:
        merged.extend(arrayII[j2:])
    else:
        merged.extend(arrayI[j1:])

    return merged


if __name__ == '__main__':
    global comps
    comps = 0
    elements = int(input("Number of elements:"))

    arr = np.random.randint(0, 1000, size=(elements))

    print(arr)

    arr_final = UnnaturalMergeSort(arr, elements)

    print(arr_final)
    print(comps)
