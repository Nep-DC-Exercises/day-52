# Problem 3: Write a function called sumZero which accepts a SORTED array of integers. The function should find the first pair where the sum is 0. Return an array that includes both values that sum to zero or undefined if a pair does not exist.
sortArray = [-11, -8, -3, 1, 2, 5, 8, 23]

def sumZero(arr):
    start = 0
    end = len(arr) - 1
    while True:
        if arr[end] + arr[start] == 0:
            return [arr[end], arr[start]]
        elif end == start:
            return "undefined"
        elif arr[end] + arr[start] > 0:
            end -= 1
        elif arr[end] + arr[start] < 0:
            start += 1
    
print(sumZero(sortArray))

# Problem 4: Find the first pair where the sum is 0 given an UNSORTED array. No nested loops. Find a solution without sorting the array.
# Solution: Accidentally solved this if the array is UNSORTED or SORTED. 
unArray = [-2, -3, 1, 8, 14, -6, 7, 3]

def unsortedArr(arr):
    for i in range(len(arr)):
        if (arr[i] < 0 and abs(arr[i]) in arr):
            return [arr[i], abs(arr[i])]
    
    return 'undefined'

# works regardless of unsorted or sorted array
print(unsortedArr(unArray))
print(unsortedArr(sortArray))



