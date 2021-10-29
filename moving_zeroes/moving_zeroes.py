'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    current = 0
    count = 1
    while count <= len(arr):
        if arr[current] == 0:
            arr.append(arr.pop(current))
        else:
            current += 1
        count += 1
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")