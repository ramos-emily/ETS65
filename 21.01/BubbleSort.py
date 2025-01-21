#bubblesort


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                merdinha = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = merdinha
    return arr

lista = [5, 3, 8, 4, 2]
bubble_sort(lista)
print(lista)
