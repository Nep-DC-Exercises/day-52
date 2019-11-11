# Fizz Buzz
# recreate it ourselves


# matrix1 = [[1,2,3], [4,5,6], [7,8,9]]

# def rotate(arr):
#     new_array = []



#     return new_array

# rotate(matrix1)

unArray = [-2, -3, 1, 8, 14, -6, 7]


# def unsortedArr(arr):
#     for i in range(len(arr)):
#         if (arr[i] < 0 and abs(arr[i]) in arr):
#             return [arr[i], abs(arr[i])]
    
#     return 'undefined'

# # print(unsortedArr(unArray))
# print(unsortedArr(sortArray))


sortArray = [-11, -8, -3, 1, 2, 9, 23]

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

