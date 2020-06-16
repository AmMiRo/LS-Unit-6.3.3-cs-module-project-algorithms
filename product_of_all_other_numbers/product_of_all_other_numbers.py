'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # create left, right, and product arrays
    left = [0] * len(arr)
    right = [0] * len(arr)
    prod = [0] * len(arr)

    # 0th of left and -1th of right should be 1
    left[0] = 1
    right[-1] = 1

    # traverse array from 2nd position, left array is populated by product of all preceding items from each index
    for i in range(1, len(arr)):
        left[i] = arr[i-1] * left[i - 1]

    # traverse array backwards from second to last position, right array is populated by product of all succeeding items from each index
    for j in range(len(arr) -2, -1, -1):
        right[j] = arr[j + 1] * right[j + 1]

    # product array is populated by values of left and righ arrays
    for i in range(len(arr)):
        prod[i] = left[i] * right[i]

    return prod

if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
