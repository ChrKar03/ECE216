import numpy as np
global rows, cols
comps = 0

def search(array, rowhalf, colhalf, key):
    global comps

    comps = comps + 1

    if (array[rowhalf][colhalf] == key):  # If key is present at middle
        print("Found ", key, "at", rowhalf, " row ", colhalf, " column (counting from zero)")
        print("Computations: ", comps)

        exit()

    else:

        if (array[rowhalf][colhalf] < key):
            if (rowhalf + 1 < rows):
                search(array, int((rows + rowhalf) / 2), colhalf, key)
            if (colhalf + 1 < cols):
                search(array, rowhalf, int((cols + colhalf) / 2), key)
        #Gia ipopinaka aristera kai pano tou stoxeiou kai pano dexia tou stoixeiou
        else:
            if (rowhalf -1 >= 0):
                search(array, int(rowhalf / 2), int((cols + colhalf) / 2), key)
            if (colhalf - 1 >= 0):
                search(array, rowhalf, int(colhalf/2), key)

            else:

                print("Key not found")
                print("Computations: ", comps)

if __name__ == '__main__':

    rows = int(input("Number of rows:"))
    cols = int(input("Number of columns:"))
    r = int(input("(1) for Random, (2) for input:"))


    if(r == 1):
        arr = np.random.randint(0,1000,size=(rows,cols))
        arr.sort(axis=0)
        arr.sort(axis=1)


    if(r == 2):
        arr = np.zeros((rows,cols))
        print("Input each element one by one and press Enter (row by row)\n")
        for i in range(0,rows):
            print("Input elements from row " + str(i) + '\n')
            for j in range(0,cols):
                arr[i][j] = int(input())
    print(arr)
    key = int(input("Key to search for:"))


    search(arr, int((rows-1)/2), int((cols-1)/2), key)
