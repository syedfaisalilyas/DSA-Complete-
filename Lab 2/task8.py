import time
import numpy as np

given_file = open (file = 'words.txt', mode = 'r')
lines = given_file.read()
words = []
arr = lines.split()
for s in arr:
    word = s
    words.append(word)
    
print(words)

  

def InsertionSort(array,start,end):
    for i in range(start+1,end):
        key_value = array[i]
        j = i-1
        while j>=start and key_value<array[j]:
            array[j+1] = array[j]
            j-=1
        array[j+1] = key_value
    
    return array


def MergeSort(array, start, end):
    if start<end:
        mid = int((start + end) / 2)
        MergeSort(array, start, mid)
        MergeSort(array, mid + 1, end)
        return Mergefunc(array, start, mid, end)
    else:
        return array

def Mergefunc(array, start, mid, end):
    left_array = array[start:mid + 1]
    right_array = array[mid + 1:end + 1]

    i = j = 0
    k = start

    while i < len(left_array) and j < len(right_array):
        if left_array[i] <= right_array[j]:
            array[k] = left_array[i]
            k += 1
            i += 1
        else:
            array[k] = right_array[j]
            k += 1
            j += 1

    while i < len(left_array):
        array[k] = left_array[i]
        i += 1
        k += 1

    while j < len(right_array):
        array[k] = right_array[j]
        j += 1
        k += 1

    return array

print("Before:")
start_time = time.time()
sorted_array = MergeSort(words, 0, len(words) - 1)
end_time = time.time()
runtime = end_time - start_time
print("Runtime of MergeSort at",len(words),"is",runtime,"seconds")


start_time = time.time()
sorted_array = InsertionSort(words, 0, len(words) - 1)
end_time = time.time()
runtime = end_time - start_time
print("Runtime of InsertionSort at",len(words),"is",runtime,"seconds")



def ShuffleArray(array,start,end):
    np.random.shuffle(words)

ShuffleArray(words, 0, len(words)-1)

#print(words)
print("After:")
start_time = time.time()
sorted_array = MergeSort(words, 0, len(words) - 1)
end_time = time.time()
runtime = end_time - start_time
print("Runtime of MergeSort at",len(words),"is",runtime,"seconds")


start_time = time.time()
sorted_array = InsertionSort(words, 0, len(words) - 1)
end_time = time.time()
runtime = end_time - start_time
print("Runtime of InsertionSort at",len(words),"is",runtime,"seconds")

print("Result: The time varies when we shuffle it becaues of depending on the order of array before and after suffling it.")















